"""
Script para crear datos de ejemplo para reportes
CecyShop - Desarrollado por Sergio Ibañez
"""

from app import app, db, User, Product, Order, OrderItem
from datetime import datetime, timedelta
import random

def create_sample_orders():
    """Crear pedidos de ejemplo para demostrar los reportes"""
    
    with app.app_context():
        # Verificar que existan usuarios y productos
        users = User.query.all()
        products = Product.query.all()
        
        if not users or not products:
            print("❌ Se necesitan usuarios y productos para crear pedidos")
            return False
        
        # Crear pedidos de ejemplo para los últimos 30 días
        print("➕ Creando pedidos de ejemplo...")
        
        orders_created = 0
        
        for i in range(50):  # Crear 50 pedidos
            # Fecha aleatoria en los últimos 30 días
            days_ago = random.randint(1, 30)
            order_date = datetime.now() - timedelta(days=days_ago)
            
            # Usuario aleatorio
            user = random.choice(users)
            
            # Crear orden
            order = Order(
                user_id=user.id,
                total=0,  # Se calculará después
                status=random.choice(['completed', 'pending', 'cancelled']),
                created_at=order_date
            )
            db.session.add(order)
            db.session.flush()  # Para obtener el ID
            
            # Agregar items aleatorios
            order_total = 0
            num_items = random.randint(1, 5)
            
            for j in range(num_items):
                product = random.choice(products)
                quantity = random.randint(1, 3)
                
                order_item = OrderItem(
                    order_id=order.id,
                    product_id=product.id,
                    quantity=quantity,
                    price=product.price
                )
                db.session.add(order_item)
                order_total += product.price * quantity
            
            # Actualizar total de la orden
            order.total = order_total
            orders_created += 1
        
        db.session.commit()
        print(f"✅ {orders_created} pedidos de ejemplo creados")
        return True

def main():
    """Función principal"""
    print("🚀 Creando datos de ejemplo para reportes...")
    
    if create_sample_orders():
        print("\n🎉 ¡Datos de ejemplo creados exitosamente!")
        print("📊 Ahora puedes ver los reportes en el panel de administración")
        print("🌐 Accede a: http://localhost:5000/admin/reports")
    else:
        print("\n❌ Error creando datos de ejemplo")

if __name__ == '__main__':
    main()
