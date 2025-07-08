"""
Script para arreglar el usuario administrador
CecyShop - Desarrollado por Sergio Ibañez
"""

from app import app, db, User
from werkzeug.security import generate_password_hash

def fix_admin_user():
    """Arreglar o crear el usuario administrador con las credenciales correctas"""
    
    with app.app_context():
        print("🔧 Arreglando usuario administrador...")
        
        # Buscar usuario admin existente
        admin = User.query.filter_by(username='admin').first()
        
        if admin:
            print("📝 Usuario admin encontrado, actualizando...")
            # Actualizar usuario existente
            admin.email = 'admin@cecyshop.com'
            admin.password_hash = generate_password_hash('admin123')
            admin.is_admin = True
        else:
            print("➕ Creando nuevo usuario admin...")
            # Crear nuevo usuario admin
            admin = User(
                username='admin',
                email='admin@cecyshop.com',
                password_hash=generate_password_hash('admin123'),
                is_admin=True
            )
            db.session.add(admin)
        
        # Guardar cambios
        try:
            db.session.commit()
            print("✅ Usuario administrador configurado correctamente!")
            print("\n🔑 Credenciales de acceso:")
            print("   Usuario: admin")
            print("   Contraseña: admin123")
            print("   Email: admin@cecyshop.com")
            
            # Verificar que funciona
            from werkzeug.security import check_password_hash
            password_ok = check_password_hash(admin.password_hash, 'admin123')
            print(f"   Verificación de contraseña: {'✅ OK' if password_ok else '❌ ERROR'}")
            
        except Exception as e:
            print(f"❌ Error guardando cambios: {e}")
            db.session.rollback()

if __name__ == '__main__':
    try:
        fix_admin_user()
    except Exception as e:
        print(f"❌ Error: {e}")
        print("💡 Asegúrate de que MySQL esté ejecutándose y la base de datos exista")
