"""
Script de prueba para verificar funcionalidad del carrito
CecyShop - Desarrollado por Sergio Ibañez
"""

from app import app, db, User, Product, CartItem
from werkzeug.security import generate_password_hash

def test_cart_functionality():
    """Prueba la funcionalidad del carrito"""
    
    with app.app_context():
        print("🛒 Probando funcionalidad del carrito...")
        
        # Buscar usuario admin
        admin = User.query.filter_by(username='admin').first()
        if not admin:
            print("❌ Usuario admin no encontrado")
            return False
        
        # Buscar productos
        products = Product.query.limit(2).all()
        if len(products) < 2:
            print("❌ No hay suficientes productos")
            return False
        
        # Limpiar carrito existente
        CartItem.query.filter_by(user_id=admin.id).delete()
        db.session.commit()
        
        # Agregar productos al carrito
        for i, product in enumerate(products):
            cart_item = CartItem(
                user_id=admin.id,
                product_id=product.id,
                quantity=i + 1  # 1, 2, etc.
            )
            db.session.add(cart_item)
        
        db.session.commit()
        
        # Verificar carrito
        cart_items = CartItem.query.filter_by(user_id=admin.id).all()
        
        print(f"✅ Carrito creado con {len(cart_items)} items:")
        total = 0
        for item in cart_items:
            item_total = float(item.product.price) * item.quantity
            total += item_total
            print(f"   - {item.product.name}: {item.quantity} x ${item.product.price} = ${item_total:.2f} MXN")
        
        print(f"   Total: ${total:.2f} MXN")
        
        # Probar actualización de cantidad
        first_item = cart_items[0]
        new_quantity = first_item.quantity + 1
        
        print(f"\n🔄 Probando actualización de cantidad...")
        print(f"   Item: {first_item.product.name}")
        print(f"   Cantidad original: {first_item.quantity}")
        print(f"   Nueva cantidad: {new_quantity}")
        
        # Simular actualización
        first_item.quantity = new_quantity
        db.session.commit()
        
        # Verificar actualización
        updated_item = CartItem.query.get(first_item.id)
        if updated_item.quantity == new_quantity:
            print("✅ Actualización exitosa")
        else:
            print("❌ Error en actualización")
            return False
        
        # Limpiar carrito de prueba
        CartItem.query.filter_by(user_id=admin.id).delete()
        db.session.commit()
        
        return True

if __name__ == '__main__':
    success = test_cart_functionality()
    if success:
        print("\n✅ Funcionalidad del carrito probada exitosamente")
        print("🌐 Ahora puedes probar en el navegador:")
        print("   1. Inicia sesión como admin")
        print("   2. Agrega productos al carrito")
        print("   3. Prueba los botones +/- de cantidad")
    else:
        print("\n❌ Hay problemas en la funcionalidad del carrito")
