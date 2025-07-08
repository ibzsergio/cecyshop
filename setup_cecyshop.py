"""
Script maestro para configurar CecyShop completamente
Este script maneja todo el proceso de configuración automáticamente
Desarrollado por: Sergio Ibañez
"""

import os
import sys
import subprocess

def run_command(command, description):
    """Ejecutar un comando y mostrar el resultado"""
    print(f"\n🔄 {description}...")
    try:
        result = subprocess.run([sys.executable, command], 
                              capture_output=True, text=True, cwd=os.getcwd())
        
        if result.returncode == 0:
            print("✅ Éxito!")
            if result.stdout:
                print(result.stdout)
            return True
        else:
            print("❌ Error!")
            if result.stderr:
                print(result.stderr)
            return False
    except Exception as e:
        print(f"❌ Error ejecutando {command}: {e}")
        return False

def main():
    """Función principal para configurar CecyShop"""
    
    print("🚀 CONFIGURACIÓN COMPLETA DE CECYSHOP")
    print("=====================================")
    print("Desarrollado por: Sergio Ibañez")
    print("Fecha: 7 de Julio, 2025")
    print("=====================================")
    
    # Verificar que los archivos necesarios existen
    required_files = [
        'create_database.py',
        'solve_admin_issues.py',
        'app.py'
    ]
    
    for file in required_files:
        if not os.path.exists(file):
            print(f"❌ Error: {file} no encontrado")
            sys.exit(1)
    
    print("✅ Archivos necesarios encontrados")
    
    # Paso 1: Crear la base de datos
    print("\n" + "="*50)
    print("PASO 1: CREANDO BASE DE DATOS")
    print("="*50)
    
    if not run_command('create_database.py', 'Creando base de datos cecyshop_db'):
        print("\n❌ Error: No se pudo crear la base de datos")
        print("💡 Asegúrate de que XAMPP esté ejecutándose")
        sys.exit(1)
    
    # Paso 2: Configurar usuarios y datos
    print("\n" + "="*50)
    print("PASO 2: CONFIGURANDO USUARIOS Y DATOS")
    print("="*50)
    
    if not run_command('solve_admin_issues.py', 'Configurando usuarios y datos'):
        print("\n❌ Error: No se pudo configurar la aplicación")
        sys.exit(1)
    
    # Paso 3: Información final
    print("\n" + "="*50)
    print("🎉 ¡CONFIGURACIÓN COMPLETADA!")
    print("="*50)
    
    print("\n🔑 CREDENCIALES DE ACCESO:")
    print("   👑 Administrador:")
    print("      Usuario: admin")
    print("      Contraseña: admin123")
    print("      URL: http://localhost:5000/admin")
    
    print("\n   👤 Usuario de prueba:")
    print("      Usuario: usuario_prueba")
    print("      Contraseña: 123456")
    
    print("\n🚀 PARA INICIAR LA APLICACIÓN:")
    print("   python app.py")
    
    print("\n🌐 URLS IMPORTANTES:")
    print("   Tienda: http://localhost:5000")
    print("   Login: http://localhost:5000/login")
    print("   Panel Admin: http://localhost:5000/admin")
    
    print("\n📋 PASOS SIGUIENTES:")
    print("   1. Ejecuta: python app.py")
    print("   2. Abre tu navegador en http://localhost:5000")
    print("   3. Inicia sesión con las credenciales de administrador")
    print("   4. Accede al panel de administración")
    
    print("\n✨ ¡CecyShop está listo para usar!")

if __name__ == '__main__':
    main()
