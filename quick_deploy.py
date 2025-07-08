#!/usr/bin/env python3
"""
Script para configurar rápidamente CecyShop con Ngrok
"""
import subprocess
import sys
import time
import os

def check_ngrok():
    """Verificar si ngrok está instalado"""
    try:
        subprocess.run(['ngrok', 'version'], capture_output=True, check=True)
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        return False

def install_requirements():
    """Instalar dependencias"""
    print("📦 Instalando dependencias...")
    subprocess.run([sys.executable, '-m', 'pip', 'install', '-r', 'requirements.txt'])

def start_flask():
    """Iniciar servidor Flask"""
    print("🚀 Iniciando servidor Flask...")
    env = os.environ.copy()
    env['DEBUG'] = 'True'
    return subprocess.Popen([sys.executable, 'app.py'], env=env)

def start_ngrok():
    """Iniciar ngrok"""
    print("🌐 Iniciando Ngrok...")
    return subprocess.Popen(['ngrok', 'http', '5000'])

def main():
    print("=" * 40)
    print("    🛍️  CecyShop - Despliegue Rápido")
    print("=" * 40)
    print()
    
    # Verificar ngrok
    if not check_ngrok():
        print("❌ Ngrok no está instalado.")
        print("📥 Descarga ngrok desde: https://ngrok.com/download")
        print("💡 O usa una de las otras opciones en DEPLOYMENT_GUIDE.md")
        return
    
    print("✅ Ngrok encontrado")
    
    # Instalar dependencias
    install_requirements()
    
    # Iniciar Flask
    flask_process = start_flask()
    
    # Esperar a que Flask inicie
    print("⏳ Esperando que Flask inicie...")
    time.sleep(5)
    
    # Iniciar ngrok
    ngrok_process = start_ngrok()
    
    print("\n🎉 ¡CecyShop está ejecutándose!")
    print("📱 Tu sitio web estará disponible en una URL como:")
    print("   https://abc123.ngrok.io")
    print("\n💡 Consejos:")
    print("   - Comparte la URL con amigos/familia")
    print("   - Funciona en cualquier dispositivo con internet")
    print("   - Usuario admin: admin / admin123")
    print("\n⏹️  Presiona Ctrl+C para detener")
    
    try:
        # Mantener ambos procesos corriendo
        flask_process.wait()
    except KeyboardInterrupt:
        print("\n🛑 Deteniendo servicios...")
        flask_process.terminate()
        ngrok_process.terminate()

if __name__ == '__main__':
    main()
