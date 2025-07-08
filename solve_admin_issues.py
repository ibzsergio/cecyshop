"""
Script de solución completa para problemas de administrador
CecyShop - Desarrollado por Sergio Ibañez
"""

import os
import sys
from app import app, db, User, Product
from werkzeug.security import generate_password_hash, check_password_hash

def solve_admin_issues():
    """Resolver todos los problemas relacionados con el acceso de administrador"""
    
    print("🔧 Resolviendo problemas de administrador en CecyShop...")
    
    with app.app_context():
        try:
            # 1. Verificar conexión a la base de datos
            print("\n1️⃣ Verificando conexión a la base de datos...")
            db.engine.connect()
            print("✅ Conexión exitosa")
            
        except Exception as e:
            if "Unknown database" in str(e):
                print("❌ La base de datos 'cecyshop_db' no existe")
                print("💡 Ejecuta primero: python create_database.py")
                return False
            else:
                print(f"❌ Error de conexión: {e}")
                print("💡 Verifica que MySQL esté ejecutándose en XAMPP")
                return False
        
        try:
            # 2. Crear tablas si no existen
            print("\n2️⃣ Verificando estructura de base de datos...")
            db.create_all()
            print("✅ Tablas verificadas/creadas")
            
            # 3. Buscar usuario admin
            print("\n3️⃣ Verificando usuario administrador...")
            admin = User.query.filter_by(username='admin').first()
            
            if admin:
                print("📝 Usuario admin encontrado, verificando configuración...")
                
                # Verificar si necesita actualización
                needs_update = False
                
                if admin.email != 'admin@cecyshop.com':
                    print("   - Actualizando email...")
                    admin.email = 'admin@cecyshop.com'
                    needs_update = True
                
                if not admin.is_admin:
                    print("   - Activando privilegios de administrador...")
                    admin.is_admin = True
                    needs_update = True
                
                # Verificar contraseña
                if not check_password_hash(admin.password_hash, 'admin123'):
                    print("   - Actualizando contraseña...")
                    admin.password_hash = generate_password_hash('admin123')
                    needs_update = True
                
                if needs_update:
                    db.session.commit()
                    print("✅ Usuario admin actualizado")
                else:
                    print("✅ Usuario admin ya está configurado correctamente")
                    
            else:
                print("➕ Creando nuevo usuario administrador...")
                admin = User(
                    username='admin',
                    email='admin@cecyshop.com',
                    password_hash=generate_password_hash('admin123'),
                    is_admin=True
                )
                db.session.add(admin)
                db.session.commit()
                print("✅ Usuario administrador creado")
            
            # 4. Verificar usuario de prueba
            print("\n4️⃣ Verificando usuario de prueba...")
            test_user = User.query.filter_by(username='usuario_prueba').first()
            
            if not test_user:
                print("➕ Creando usuario de prueba...")
                test_user = User(
                    username='usuario_prueba',
                    email='usuario@cecyshop.com',
                    password_hash=generate_password_hash('123456'),
                    is_admin=False
                )
                db.session.add(test_user)
                db.session.commit()
                print("✅ Usuario de prueba creado")
            else:
                print("✅ Usuario de prueba ya existe")
            
            # 5. Verificar productos (crear algunos si no existen)
            print("\n5️⃣ Verificando productos...")
            product_count = Product.query.count()
            
            if product_count == 0:
                print("➕ Creando productos de muestra...")
                sample_products = [
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
                        description='Laptop de alta performance con certificación de sostenibilidad.',
                        price=899.99,
                        stock=8,
                        category='Electrónicos',
                        image_url='https://images.unsplash.com/photo-1496181133206-80ce9b88a853?w=400'
                    )
                ]
                
                for product in sample_products:
                    db.session.add(product)
                
                db.session.commit()
                print(f"✅ {len(sample_products)} productos de muestra creados")
            else:
                print(f"✅ {product_count} productos encontrados en la base de datos")
            
            # 6. Verificación final
            print("\n6️⃣ Verificación final...")
            
            # Recargar usuario admin para verificar
            admin = User.query.filter_by(username='admin').first()
            password_ok = check_password_hash(admin.password_hash, 'admin123')
            
            print(f"   Usuario: {admin.username}")
            print(f"   Email: {admin.email}")
            print(f"   Es Admin: {admin.is_admin}")
            print(f"   Contraseña válida: {'✅' if password_ok else '❌'}")
            
            # Estadísticas
            total_users = User.query.count()
            total_products = Product.query.count()
            
            print(f"\n📊 Estadísticas de la base de datos:")
            print(f"   Total usuarios: {total_users}")
            print(f"   Total productos: {total_products}")
            
            print(f"\n🎉 ¡Todos los problemas resueltos!")
            print(f"\n🔑 Credenciales de administrador:")
            print(f"   Usuario: admin")
            print(f"   Contraseña: admin123")
            print(f"   URL Admin: http://localhost:5000/admin")
            
            return True
            
        except Exception as e:
            print(f"❌ Error durante la configuración: {e}")
            db.session.rollback()
            return False

if __name__ == '__main__':
    success = solve_admin_issues()
    if not success:
        print("\n💡 Posibles soluciones:")
        print("   1. Verifica que MySQL esté ejecutándose")
        print("   2. Asegúrate de que la base de datos 'cecyshop_db' existe")
        print("   3. Ejecuta 'pip install pymysql' si hay problemas de conexión")
        sys.exit(1)
    else:
        print("\n🚀 ¡Ahora puedes iniciar la aplicación con 'python app.py'!")
