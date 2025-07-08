"""
Script de diagnóstico para verificar el usuario administrador
CecyShop - Desarrollado por Sergio Ibañez
"""

from app import app, db, User
from werkzeug.security import check_password_hash

def check_admin_user():
    """Verificar si el usuario administrador existe y está configurado correctamente"""
    
    with app.app_context():
        print("🔍 Verificando usuario administrador...")
        
        # Buscar usuario admin
        admin = User.query.filter_by(username='admin').first()
        
        if not admin:
            print("❌ Usuario admin NO existe")
            return False
        
        print(f"✅ Usuario admin encontrado:")
        print(f"   ID: {admin.id}")
        print(f"   Username: {admin.username}")
        print(f"   Email: {admin.email}")
        print(f"   Es Admin: {admin.is_admin}")
        print(f"   Fecha creación: {admin.created_at}")
        
        # Verificar contraseña
        password_ok = check_password_hash(admin.password_hash, 'admin123')
        print(f"   Contraseña correcta: {'✅ Sí' if password_ok else '❌ No'}")
        
        # Verificar todos los usuarios
        print(f"\n📊 Total de usuarios en la base de datos: {User.query.count()}")
        
        all_users = User.query.all()
        for user in all_users:
            print(f"   - {user.username} ({user.email}) - Admin: {user.is_admin}")
        
        return admin.is_admin and password_ok

if __name__ == '__main__':
    try:
        check_admin_user()
    except Exception as e:
        print(f"❌ Error: {e}")
        print("💡 Asegúrate de que MySQL esté ejecutándose y la base de datos exista")
