Jose Velasquez

## Requisitos previos
- Docker y Docker Compose instalados
- (Opcional) Python 3.11 para ejecutar proyectos localmente

## Pasos rápidos (desarrollo con Docker)
1. Copiar `.env` en cada servicio y configurar claves y variables (SECRET_KEY, DB creds).
2. Ejecutar: `docker compose build` y luego `docker compose up`
3. Acceder al API Gateway en `http://localhost:8080` y llamar a rutas como `/auth/register/`.

## Notas importantes
- Cada microservicio es un proyecto Django independiente. Debe ejecutar `python manage.py migrate` dentro de cada contenedor la primera vez.
- En este scaffold las comunicaciones entre servicios se realizan por HTTP (API REST). Para eventos asíncronos use RabbitMQ y defina consumidores/productores en los servicios.
- Protección: use HTTPS, gestione secretos con un vault y no exponga bases de datos directamente en producción.
