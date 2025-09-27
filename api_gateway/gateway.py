import os
from fastapi import FastAPI, Request, Response
from fastapi.responses import HTMLResponse
import httpx

app = FastAPI()

# ===== Definición de servicios =====
SERVICE_MAP = {
    '/auth': os.environ.get('AUTH_URL', 'http://auth_service:8000'),
    '/roles': os.environ.get('ROLES_URL', 'http://roles_service:8000'),
    '/fields': os.environ.get('FIELDS_URL', 'http://fields_service:8000'),
    '/bookings': os.environ.get('BOOKINGS_URL', 'http://bookings_service:8000'),
    '/admin': os.environ.get('ADMIN_URL', 'http://admin_dashboard:8000'),
}

# ===== Ruta principal: muestra el login de auth_service =====
@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    auth_url = SERVICE_MAP['/auth'] + '/'  # URL de login del auth_service
    async with httpx.AsyncClient() as client:
        # Sobrescribimos el header Host para evitar DisallowedHost en Django
        headers = {'Host': 'auth_service'}  
        resp = await client.get(auth_url, headers=headers)
    return HTMLResponse(content=resp.text, status_code=resp.status_code)

# ===== Proxy específico para /auth/* =====
@app.api_route('/auth/{path:path}', methods=['GET','POST','PUT','PATCH','DELETE'])
async def auth_proxy(path: str, request: Request):
    target_base = SERVICE_MAP['/auth']
    url = target_base + '/' + path

    async with httpx.AsyncClient() as client:
        headers = dict(request.headers)
        headers['Host'] = 'auth_service'  # evita DisallowedHost
        body = await request.body()
        resp = await client.request(
            request.method,
            url,
            headers=headers,
            content=body,
            params=request.query_params
        )

    return Response(
        content=resp.content,
        status_code=resp.status_code,
        headers=resp.headers
    )

# ===== Proxy genérico para otros servicios =====
@app.api_route('/{path:path}', methods=['GET','POST','PUT','PATCH','DELETE'])
async def proxy(path: str, request: Request):
    full_path = '/' + path
    target_base = None
    prefix = None

    for p, target in SERVICE_MAP.items():
        if full_path.startswith(p):
            prefix = p
            target_base = target
            break

    if not target_base:
        return Response(content='Service not found', status_code=404)

    forwarded_path = full_path
    if prefix:
        forwarded_path = full_path[len(prefix):]
        if not forwarded_path.startswith('/'):
            forwarded_path = '/' + forwarded_path

    url = target_base + forwarded_path

    async with httpx.AsyncClient() as client:
        headers = dict(request.headers)
        # Si el target es auth_service, sobrescribimos Host
        if prefix == '/auth':
            headers['Host'] = 'auth_service'
        body = await request.body()
        resp = await client.request(
            request.method,
            url,
            headers=headers,
            content=body,
            params=request.query_params
        )

    return Response(
        content=resp.content,
        status_code=resp.status_code,
        headers=resp.headers
    )
