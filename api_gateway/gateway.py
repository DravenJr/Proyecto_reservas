from fastapi import FastAPI, Request, Response
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import httpx
import os

app = FastAPI()
templates = Jinja2Templates(directory="templates")

# Servir la página principal
@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# Mapa de servicios para el proxy
SERVICE_MAP = {
    '/auth': os.environ.get('AUTH_URL', 'http://auth_service:8000'),
    '/roles': os.environ.get('ROLES_URL', 'http://roles_service:8000'),
    '/fields': os.environ.get('FIELDS_URL', 'http://fields_service:8000'),
    '/bookings': os.environ.get('BOOKINGS_URL', 'http://bookings_service:8000'),
    '/admin': os.environ.get('ADMIN_URL', 'http://admin_dashboard:8000'),
}

# Proxy genérico para todos los servicios
@app.api_route('/{path:path}', methods=['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
async def proxy(path: str, request: Request):
    full_path = '/' + path
    target_base = None
    prefix = None

    # Encontrar el servicio correspondiente
    for p, target in SERVICE_MAP.items():
        if full_path.startswith(p):
            prefix = p
            target_base = target
            break

    if not target_base:
        return Response(content='Service not found', status_code=404)

    # Ajustar la ruta a enviar al servicio
    forwarded_path = full_path[len(prefix):] if prefix else full_path
    if not forwarded_path.startswith('/'):
        forwarded_path = '/' + forwarded_path

    url = target_base + forwarded_path

    # Reenviar la solicitud
    async with httpx.AsyncClient() as client:
        headers = dict(request.headers)
        body = await request.body()
        resp = await client.request(
            request.method,
            url,
            headers=headers,
            content=body,
            params=request.query_params
        )

    # Devolver la respuesta tal cual
    return Response(
        content=resp.content,
        status_code=resp.status_code,
        headers=resp.headers
    )
