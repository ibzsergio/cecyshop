"""
Script para crear la base de datos CecyShop
Este script crea la base de datos y luego ejecuta la configuración inicial
Desarrollado por: Sergio Ibañez
"""

import pymysql
import sys
from sqlalchemy import create_engine

def create_database():
    """Crear la base de datos cecyshop_db si no existe"""
    
    print("🗄️ Creando base de datos CecyShop...")
    
    try:
        # Conectar a MySQL sin especificar base de datos
        connection = pymysql.connect(
            host='localhost',
            user='root',
            password='',  # Sin contraseña por defecto en XAMPP
            charset='utf8mb4'
        )
        
        print("✅ Conexión a MySQL exitosa")
        
        with connection.cursor() as cursor:
            # Crear la base de datos si no existe
            cursor.execute("CREATE DATABASE IF NOT EXISTS cecyshop_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci")
            print("✅ Base de datos 'cecyshop_db' creada/verificada")
            
            # Verificar que la base de datos existe
            cursor.execute("SHOW DATABASES LIKE 'cecyshop_db'")
            result = cursor.fetchone()
            
            if result:
                print("✅ Base de datos confirmada")
                return True
            else:
                print("❌ Error: No se pudo crear la base de datos")
                return False
                
    except Exception as e:
        print(f"❌ Error conectando a MySQL: {e}")
        print("\n💡 Soluciones posibles:")
        print("   1. Asegúrate de que XAMPP esté ejecutándose")
        print("   2. Verifica que MySQL esté activo en XAMPP")
        print("   3. Confirma que no hay contraseña configurada para root")
        return False
    
    finally:
        if 'connection' in locals():
            connection.close()

def test_database_connection():
    """Probar la conexión a la base de datos creada"""
    
    print("\n🔍 Probando conexión a la base de datos...")
    
    try:
        engine = create_engine('mysql+pymysql://root:@localhost/cecyshop_db')
        with engine.connect() as conn:
            result = conn.execute("SELECT 1")
            print("✅ Conexión a cecyshop_db exitosa")
            return True
    except Exception as e:
        print(f"❌ Error conectando a cecyshop_db: {e}")
        return False

if __name__ == '__main__':
    print("🚀 Configuración inicial de CecyShop")
    print("=====================================")
    
    # Crear la base de datos
    if create_database():
        # Probar la conexión
        if test_database_connection():
            print("\n🎉 ¡Base de datos lista!")
            print("📝 Ahora puedes ejecutar:")
            print("   python solve_admin_issues.py")
        else:
            print("\n❌ Error en la conexión final")
            sys.exit(1)
    else:
        print("\n❌ No se pudo crear la base de datos")
        sys.exit(1)
