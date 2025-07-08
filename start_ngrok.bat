@echo off
echo ================================
echo    CecyShop - Ngrok Setup
echo ================================
echo.

echo 1. Iniciando servidor Flask...
start /B python app.py

echo 2. Esperando que el servidor inicie...
timeout /t 5 /nobreak > nul

echo 3. Iniciando Ngrok (asegurate de tener ngrok instalado)...
echo    Descarga ngrok desde: https://ngrok.com/download
echo.
echo 4. Ejecuta este comando en otra terminal:
echo    ngrok http 5000
echo.
echo 5. Ngrok te dara una URL publica como:
echo    https://abc123.ngrok.io
echo.
echo ¡Comparte esa URL para acceder desde cualquier dispositivo!
echo.
pause
