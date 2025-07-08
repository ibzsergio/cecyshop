"""
Script simple para verificar la funcionalidad del carrito
CecyShop - Desarrollado por Sergio Ibañez
"""

print("🔧 Verificaciones para CecyShop:")
print()

# 1. Verificar que todos los archivos importantes existen
import os

files_to_check = [
    'app.py',
    'static/js/script.js',
    'static/css/style.css',
    'templates/index.html',
    'templates/cart.html',
    'templates/product_detail.html'
]

print("1️⃣ Verificando archivos...")
for file in files_to_check:
    if os.path.exists(file):
        print(f"✅ {file}")
    else:
        print(f"❌ {file} - NO ENCONTRADO")

print()

# 2. Verificar configuración de base de datos
print("2️⃣ Verificando configuración...")
try:
    from app import app, db
    with app.app_context():
        # Intentar conectar
        db.engine.connect()
        print("✅ Conexión a base de datos")
        
        # Verificar tablas
        from app import User, Product, CartItem
        user_count = User.query.count()
        product_count = Product.query.count()
        print(f"✅ {user_count} usuarios, {product_count} productos")
        
except Exception as e:
    print(f"❌ Error de base de datos: {e}")

print()

# 3. Verificar usuario admin
print("3️⃣ Verificando usuario admin...")
try:
    from app import User
    with app.app_context():
        admin = User.query.filter_by(username='admin').first()
        if admin and admin.is_admin:
            print("✅ Usuario admin configurado correctamente")
        else:
            print("❌ Problema con usuario admin")
except Exception as e:
    print(f"❌ Error verificando admin: {e}")

print()
print("🌐 Para probar la aplicación:")
print("1. Ejecuta: python app.py")
print("2. Abre: http://localhost:5000")
print("3. Inicia sesión con: admin / admin123")
print("4. Prueba agregar productos al carrito")
print()
print("📋 Si hay problemas:")
print("- Verifica que MySQL esté ejecutándose")
print("- Verifica que la base de datos 'cecyshop_db' existe")
print("- Revisa la consola del navegador para errores JavaScript")
