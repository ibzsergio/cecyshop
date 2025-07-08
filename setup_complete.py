"""
Script para crear la base de datos y resolver problemas de acceso
CecyShop - Desarrollado por Sergio Ibañez
"""

import pymysql
from app import app, db, User, Product
from werkzeug.security import generate_password_hash, check_password_hash

def create_database():
    """Crear la base de datos cecyshop_db"""
    try:
        # Conectar a MySQL sin especificar base de datos
        connection = pymysql.connect(
            host='localhost',
            user='root',
            password='',
            charset='utf8mb4'
        )
        
        with connection.cursor() as cursor:
            # Crear base de datos si no existe
            cursor.execute("CREATE DATABASE IF NOT EXISTS cecyshop_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci")
            print("✅ Base de datos 'cecyshop_db' creada/verificada")
        
        connection.close()
        return True
        
    except Exception as e:
        print(f"❌ Error creando base de datos: {e}")
        return False

def setup_admin():
    """Configurar el usuario administrador"""
    try:
        with app.app_context():
            # Crear tablas
            db.create_all()
            print("✅ Tablas creadas/verificadas")
            
            # Buscar o crear usuario admin
            admin = User.query.filter_by(username='admin').first()
            
            if admin:
                print("📝 Usuario admin encontrado, actualizando...")
                # Actualizar datos del admin
                admin.email = 'admin@cecyshop.com'
                admin.password_hash = generate_password_hash('admin123')
                admin.is_admin = True
            else:
                print("➕ Creando nuevo usuario admin...")
                admin = User(
                    username='admin',
                    email='admin@cecyshop.com',
                    password_hash=generate_password_hash('admin123'),
                    is_admin=True
                )
                db.session.add(admin)
            
            db.session.commit()
            
            # Verificar que funciona
            admin_check = User.query.filter_by(username='admin').first()
            password_ok = check_password_hash(admin_check.password_hash, 'admin123')
            
            print(f"✅ Usuario admin configurado:")
            print(f"   Username: {admin_check.username}")
            print(f"   Email: {admin_check.email}")
            print(f"   Es Admin: {admin_check.is_admin}")
            print(f"   Contraseña válida: {'✅' if password_ok else '❌'}")
            
            # Crear algunos productos si no existen
            if Product.query.count() == 0:
                print("➕ Creando productos de muestra...")
                products = [
                    Product(
                        name='Smartphone Verde Eco',
                        description='Smartphone amigable con el medio ambiente.',
                        price=299.99,
                        stock=15,
                        category='Electrónicos',
                        image_url='https://images.unsplash.com/photo-1511707171634-5f897ff02aa9?w=400'
                    ),
                    Product(
                        name='Camiseta Orgánica',
                        description='Camiseta 100% algodón orgánico.',
                        price=29.99,
                        stock=25,
                        category='Ropa',
                        image_url='https://images.unsplash.com/photo-1521572163474-6864f9cf17ab?w=400'
                    ),
                    Product(
                        name='Laptop Sostenible',
                        description='Laptop de alta performance.',
                        price=899.99,
                        stock=8,
                        category='Electrónicos',
                        image_url='https://images.unsplash.com/photo-1496181133206-80ce9b88a853?w=400'
                    )
                ]
                
                for product in products:
                    db.session.add(product)
                
                db.session.commit()
                print(f"✅ {len(products)} productos creados")
            
            return True
            
    except Exception as e:
        print(f"❌ Error configurando admin: {e}")
        return False

def main():
    """Función principal"""
    print("🚀 Configurando CecyShop...")
    
    # Paso 1: Crear base de datos
    if not create_database():
        print("❌ No se pudo crear la base de datos")
        return
    
    # Paso 2: Configurar administrador
    if not setup_admin():
        print("❌ No se pudo configurar el administrador")
        return
    
    print("\n🎉 ¡Configuración completada exitosamente!")
    print("\n🔑 Credenciales de administrador:")
    print("   Usuario: admin")
    print("   Contraseña: admin123")
    print("\n🌐 Ahora puedes ejecutar:")
    print("   python app.py")
    print("   Y acceder a http://localhost:5000")

if __name__ == '__main__':
    main()
