"""
Script de inicialización para CecyShop
Este archivo configura la aplicación y crea la base de datos inicial
Desarrollado por: Sergio Ibañez
"""

import os
import sys
from app import app, db
from populate_db import create_sample_data

def init_app():
    """Inicializar la aplicación CecyShop"""
    print("🌱 Inicializando CecyShop...")
    
    # Verificar que MySQL esté disponible
    try:
        with app.app_context():
            # Intentar conectar a la base de datos
            db.engine.connect()
            print("✅ Conexión a MySQL exitosa")
    except Exception as e:
        print(f"❌ Error conectando a MySQL: {e}")
        print("📝 Asegúrate de que MySQL esté ejecutándose y la base de datos esté creada")
        sys.exit(1)
    
    # Crear tablas
    try:
        with app.app_context():
            db.create_all()
            print("✅ Tablas de base de datos creadas")
    except Exception as e:
        print(f"❌ Error creando tablas: {e}")
        sys.exit(1)
    
    # Crear datos de prueba
    try:
        create_sample_data()
        print("✅ Datos de prueba creados")
    except Exception as e:
        print(f"❌ Error creando datos de prueba: {e}")
        sys.exit(1)
    
    print("\n🎉 ¡CecyShop inicializado exitosamente!")
    print("🚀 Ejecuta 'python app.py' para iniciar el servidor")
    print("🌐 La aplicación estará disponible en http://localhost:5000")
    print("\n🔑 Credenciales de administrador:")
    print("   Usuario: admin")
    print("   Contraseña: admin123")

if __name__ == "__main__":
    init_app()
