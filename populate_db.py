from app import app, db, User, Product
from werkzeug.security import generate_password_hash

def create_sample_data():
    """Crear datos de prueba para CecyShop - Desarrollado por Sergio Ibañez"""
    
    with app.app_context():
        # Crear tablas si no existen
        db.create_all()
        
        # Crear usuario administrador si no existe
        admin = User.query.filter_by(username='admin').first()
        if not admin:
            admin = User(
                username='admin',
                email='admin@cecyshop.com',
                password_hash=generate_password_hash('admin123'),
                is_admin=True
            )
            db.session.add(admin)
        
        # Crear usuario de prueba
        test_user = User.query.filter_by(username='usuario_prueba').first()
        if not test_user:
            test_user = User(
                username='usuario_prueba',
                email='usuario@cecyshop.com',
                password_hash=generate_password_hash('123456'),
                is_admin=False
            )
            db.session.add(test_user)
        
        # Verificar si ya existen productos
        if Product.query.count() == 0:
            # Crear productos de muestra
            productos = [
                {
                    'name': 'Smartphone Verde Eco',
                    'description': 'Smartphone amigable con el medio ambiente, fabricado con materiales reciclados y diseño minimalista.',
                    'price': 299.99,
                    'stock': 15,
                    'category': 'Electrónicos',
                    'image_url': 'https://images.unsplash.com/photo-1511707171634-5f897ff02aa9?w=400'
                },
                {
                    'name': 'Camiseta Orgánica',
                    'description': 'Camiseta 100% algodón orgánico, suave y cómoda. Perfecta para el día a día.',
                    'price': 29.99,
                    'stock': 25,
                    'category': 'Ropa',
                    'image_url': 'https://images.unsplash.com/photo-1521572163474-6864f9cf17ab?w=400'
                },
                {
                    'name': 'Laptop Sostenible',
                    'description': 'Laptop de alta performance con certificación de sostenibilidad y diseño elegante.',
                    'price': 899.99,
                    'stock': 8,
                    'category': 'Electrónicos',
                    'image_url': 'https://images.unsplash.com/photo-1496181133206-80ce9b88a853?w=400'
                },
                {
                    'name': 'Zapatillas Eco',
                    'description': 'Zapatillas deportivas hechas con materiales reciclados y suela biodegradable.',
                    'price': 79.99,
                    'stock': 20,
                    'category': 'Deportes',
                    'image_url': 'https://images.unsplash.com/photo-1542291026-7eec264c27ff?w=400'
                },
                {
                    'name': 'Botella de Agua Reutilizable',
                    'description': 'Botella de acero inoxidable, libre de BPA, mantiene la temperatura por 24 horas.',
                    'price': 24.99,
                    'stock': 50,
                    'category': 'Hogar',
                    'image_url': 'https://images.unsplash.com/photo-1602143407151-7111542de6e8?w=400'
                },
                {
                    'name': 'Libro: Vida Sostenible',
                    'description': 'Guía completa para adoptar un estilo de vida más sostenible y consciente.',
                    'price': 19.99,
                    'stock': 30,
                    'category': 'Libros',
                    'image_url': 'https://images.unsplash.com/photo-1544947950-fa07a98d237f?w=400'
                },
                {
                    'name': 'Auriculares Inalámbricos',
                    'description': 'Auriculares con cancelación de ruido y batería de larga duración.',
                    'price': 159.99,
                    'stock': 12,
                    'category': 'Electrónicos',
                    'image_url': 'https://images.unsplash.com/photo-1505740420928-5e560c06d30e?w=400'
                },
                {
                    'name': 'Jeans Sostenibles',
                    'description': 'Jeans fabricados con algodón orgánico y proceso de teñido ecológico.',
                    'price': 89.99,
                    'stock': 18,
                    'category': 'Ropa',
                    'image_url': 'https://images.unsplash.com/photo-1541099649105-f69ad21f3246?w=400'
                },
                {
                    'name': 'Reloj Inteligente Verde',
                    'description': 'Smartwatch con funciones de salud y fitness, carga solar disponible.',
                    'price': 249.99,
                    'stock': 10,
                    'category': 'Electrónicos',
                    'image_url': 'https://images.unsplash.com/photo-1523275335684-37898b6baf30?w=400'
                },
                {
                    'name': 'Mochila Ecológica',
                    'description': 'Mochila resistente al agua hecha con botellas plásticas recicladas.',
                    'price': 59.99,
                    'stock': 22,
                    'category': 'Deportes',
                    'image_url': 'https://images.unsplash.com/photo-1553062407-98eeb64c6a62?w=400'
                },
                {
                    'name': 'Kit de Cosméticos Naturales',
                    'description': 'Set completo de productos de belleza 100% naturales y cruelty-free.',
                    'price': 69.99,
                    'stock': 15,
                    'category': 'Belleza',
                    'image_url': 'https://images.unsplash.com/photo-1596462502278-27bfdc403348?w=400'
                },
                {
                    'name': 'Tabla de Cortar Bambú',
                    'description': 'Tabla de cortar antibacteriana hecha de bambú sostenible.',
                    'price': 34.99,
                    'stock': 35,
                    'category': 'Hogar',
                    'image_url': 'https://images.unsplash.com/photo-1584464491033-06628f3a6b7b?w=400'
                },
                {
                    'name': 'Cargador Solar Portátil',
                    'description': 'Cargador solar resistente al agua, perfecto para actividades al aire libre.',
                    'price': 49.99,
                    'stock': 20,
                    'category': 'Electrónicos',
                    'image_url': 'https://images.unsplash.com/photo-1593941707882-a5bac6861d75?w=400'
                },
                {
                    'name': 'Sudadera Orgánica',
                    'description': 'Sudadera con capucha de algodón orgánico, cómoda y duradera.',
                    'price': 54.99,
                    'stock': 16,
                    'category': 'Ropa',
                    'image_url': 'https://images.unsplash.com/photo-1556821840-3a63f95609a7?w=400'
                },
                {
                    'name': 'Set de Yoga Sostenible',
                    'description': 'Mat de yoga de corcho natural con accesorios incluidos.',
                    'price': 89.99,
                    'stock': 12,
                    'category': 'Deportes',
                    'image_url': 'https://images.unsplash.com/photo-1544367567-0f2fcb009e0b?w=400'
                },
                {
                    'name': 'Plantas Purificadoras',
                    'description': 'Set de 3 plantas que purifican el aire de tu hogar naturalmente.',
                    'price': 39.99,
                    'stock': 25,
                    'category': 'Hogar',
                    'image_url': 'https://images.unsplash.com/photo-1416879595882-3373a0480b5b?w=400'
                },
                {
                    'name': 'Cámara Eco Digital',
                    'description': 'Cámara digital compacta con carcasa de materiales reciclados.',
                    'price': 199.99,
                    'stock': 8,
                    'category': 'Electrónicos',
                    'image_url': 'https://images.unsplash.com/photo-1516035069371-29a1b244cc32?w=400'
                },
                {
                    'name': 'Juego Educativo Verde',
                    'description': 'Juego de mesa educativo sobre sostenibilidad para toda la familia.',
                    'price': 29.99,
                    'stock': 30,
                    'category': 'Juguetes',
                    'image_url': 'https://images.unsplash.com/photo-1606092195730-5d7b9af1efc5?w=400'
                },
                {
                    'name': 'Termo Inteligente',
                    'description': 'Termo con control de temperatura via app y materiales 100% reciclables.',
                    'price': 79.99,
                    'stock': 14,
                    'category': 'Hogar',
                    'image_url': 'https://images.unsplash.com/photo-1571019613454-1cb2f99b2d8b?w=400'
                },
                {
                    'name': 'Bicicleta Urbana Eco',
                    'description': 'Bicicleta urbana con marco de aluminio reciclado y diseño minimalista.',
                    'price': 499.99,
                    'stock': 5,
                    'category': 'Deportes',
                    'image_url': 'https://images.unsplash.com/photo-1558618666-fcd25c85cd64?w=400'
                }
            ]
            
            for producto_data in productos:
                producto = Product(**producto_data)
                db.session.add(producto)
        
        # Guardar todos los cambios
        db.session.commit()
        print("✅ Datos de prueba creados exitosamente!")
        print(f"📦 Se crearon {Product.query.count()} productos")
        print(f"👥 Se crearon {User.query.count()} usuarios")
        print("\n🔑 Credenciales de administrador:")
        print("Usuario: admin")
        print("Contraseña: admin123")
        print("\n🔑 Credenciales de usuario de prueba:")
        print("Usuario: usuario_prueba")
        print("Contraseña: 123456")

if __name__ == '__main__':
    create_sample_data()
