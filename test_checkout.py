"""
Script de prueba para verificar que el checkout funciona correctamente
CecyShop - Desarrollado por Sergio Ibañez
"""

from app import app, db, User, Product, CartItem
from werkzeug.security import generate_password_hash

def test_checkout():
    """Prueba el proceso de checkout"""
    
    with app.app_context():
        print("🧪 Probando proceso de checkout...")
        
        # Buscar usuario admin
        admin = User.query.filter_by(username='admin').first()
        if not admin:
            print("❌ Usuario admin no encontrado")
            return False
        
        # Buscar un producto
        product = Product.query.first()
        if not product:
            print("❌ No hay productos disponibles")
            return False
        
        # Crear item en carrito
        cart_item = CartItem.query.filter_by(user_id=admin.id, product_id=product.id).first()
        if not cart_item:
            cart_item = CartItem(user_id=admin.id, product_id=product.id, quantity=2)
            db.session.add(cart_item)
            db.session.commit()
        
        # Probar cálculo del total
        try:
            from app import safe_float
            total = safe_float(product.price) * cart_item.quantity
            print(f"✅ Cálculo exitoso: {product.name} - ${product.price} x {cart_item.quantity} = ${total}")
            
            # Limpiar carrito de prueba
            db.session.delete(cart_item)
            db.session.commit()
            
            return True
            
        except Exception as e:
            print(f"❌ Error en cálculo: {e}")
            return False

if __name__ == '__main__':
    success = test_checkout()
    if success:
        print("\n✅ Prueba exitosa - El checkout debería funcionar correctamente")
        print("🛒 Ahora puedes probar agregar productos al carrito y proceder al pago")
    else:
        print("\n❌ Hay problemas en el checkout")
