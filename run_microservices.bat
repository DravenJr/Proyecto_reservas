@echo off
REM Script para levantar el scaffold de microservicios de fútbol


echo Copiando archivos .env de ejemplo
copy auth_service\.env.example auth_service\.env
copy roles_service\.env.example roles_service\.env
copy fields_service\.env.example fields_service\.env
copy bookings_service\.env.example bookings_service\.env
copy admin_dashboard\.env.example admin_dashboard\.env
copy api_gateway\.env.example api_gateway\.env

echo.
echo  Construyendo contenedores Docker 
docker compose build

echo.
echo Levantando contenedores 
docker compose up -d

echo.
echo Ejecutando migraciones
docker compose exec auth_service python manage.py migrate
docker compose exec roles_service python manage.py migrate
docker compose exec fields_service python manage.py migrate
docker compose exec bookings_service python manage.py migrate
docker compose exec admin_dashboard python manage.py migrate

echo.
echo Accede al API Gateway en http://localhost:8080
pause
