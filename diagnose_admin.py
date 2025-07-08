"""
Script para diagnosticar y resolver problemas de login del administrador
CecyShop - Desarrollado por Sergio Ibañez
"""

import pymysql
from app import app, db, User
from werkzeug.security import generate_password_hash, check_password_hash

def create_database_if_not_exists():
    """Crear la base de datos si no existe"""
    try:
        # Conectar a MySQL sin especificar base de datos
        connection = pymysql.connect(
            host='localhost',
            user='root',
            password='',
            charset='utf8mb4'
        )
        
        cursor = connection.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS cecyshop_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci")
        cursor.close()
        connection.close()
        
        print("✅ Base de datos cecyshop_db creada o ya existe")
        return True
        
    except Exception as e:
        print(f"❌ Error creando base de datos: {e}")
        return False

def diagnose_and_fix_admin():
    """Diagnosticar y arreglar problemas del administrador"""
    
    print("🔍 Diagnosticando problemas de login del administrador...")
    
    # 1. Crear base de datos si no existe
    if not create_database_if_not_exists():
        return False
    
    # 2. Trabajar con la aplicación Flask
    with app.app_context():
        try:
            # Crear todas las tablas
            db.create_all()
            print("✅ Tablas creadas correctamente")
            
            # Buscar usuario admin
            admin = User.query.filter_by(username='admin').first()
            
            if admin:
                print("📋 Usuario admin encontrado:")
                print(f"   ID: {admin.id}")
                print(f"   Username: {admin.username}")
                print(f"   Email: {admin.email}")
                print(f"   Es Admin: {admin.is_admin}")
                
                # Verificar contraseña actual
                password_correct = check_password_hash(admin.password_hash, 'admin123')
                print(f"   Contraseña correcta: {'✅' if password_correct else '❌'}")
                
                if not password_correct or not admin.is_admin:
                    print("🔧 Actualizando usuario admin...")
                    admin.password_hash = generate_password_hash('admin123')
                    admin.is_admin = True
                    admin.email = 'admin@cecyshop.com'
                    db.session.commit()
                    print("✅ Usuario admin actualizado")
                    
            else:
                print("➕ Creando usuario administrador...")
                admin = User(
                    username='admin',
                    email='admin@cecyshop.com',
                    password_hash=generate_password_hash('admin123'),
                    is_admin=True
                )
                db.session.add(admin)
                db.session.commit()
                print("✅ Usuario administrador creado")
            
            # Verificación final
            admin = User.query.filter_by(username='admin').first()
            final_check = check_password_hash(admin.password_hash, 'admin123')
            
            print(f"\n🎯 Verificación final:")
            print(f"   Usuario existe: {'✅' if admin else '❌'}")
            print(f"   Es admin: {'✅' if admin.is_admin else '❌'}")
            print(f"   Contraseña válida: {'✅' if final_check else '❌'}")
            
            if admin and admin.is_admin and final_check:
                print(f"\n🎉 ¡Problema resuelto!")
                print(f"🔑 Puedes iniciar sesión con:")
                print(f"   Usuario: admin")
                print(f"   Contraseña: admin123")
                return True
            else:
                print(f"\n❌ Aún hay problemas")
                return False
                
        except Exception as e:
            print(f"❌ Error en el proceso: {e}")
            return False

if __name__ == '__main__':
    success = diagnose_and_fix_admin()
    
    if not success:
        print("\n💡 Posibles soluciones:")
        print("1. Verifica que XAMPP esté ejecutándose")
        print("2. Verifica que MySQL esté activo en XAMPP")
        print("3. Reinicia XAMPP y vuelve a intentar")
    else:
        print("\n🚀 Ahora puedes ejecutar 'python app.py' y probar el login")
