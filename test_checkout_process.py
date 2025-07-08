#!/usr/bin/env python3
"""
Script para probar el proceso de checkout
"""
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from app import app, db, User, Product, CartItem, Order, OrderItem

def test_checkout_process():
    with app.app_context():
        # Buscar usuario admin
        admin_user = User.query.filter_by(is_admin=True).first()
        if not admin_user:
            print("❌ No se encontró usuario admin")
            return
        
        # Verificar que hay items en el carrito
        cart_items = CartItem.query.filter_by(user_id=admin_user.id).all()
        if not cart_items:
            print("❌ No hay items en el carrito")
            return
        
        print(f"✅ Usuario: {admin_user.username}")
        print(f"✅ Items en carrito: {len(cart_items)}")
        
        # Simular el proceso de checkout
        total = sum(float(item.product.price) * item.quantity for item in cart_items)
        print(f"✅ Total de la orden: ${total:.2f}")
        
        # Crear orden de prueba
        order = Order(user_id=admin_user.id, total=total, status='completed')
        db.session.add(order)
        db.session.flush()
        
        print(f"✅ Orden creada con ID: {order.id}")
        
        # Crear items de la orden
        for item in cart_items:
            order_item = OrderItem(
                order_id=order.id,
                product_id=item.product_id,
                quantity=item.quantity,
                price=float(item.product.price)
            )
            db.session.add(order_item)
            print(f"  - OrderItem: {item.product.name} x{item.quantity}")
        
        db.session.commit()
        
        # Verificar que la orden se creó correctamente
        created_order = Order.query.get(order.id)
        print(f"✅ Orden verificada: ID {created_order.id}")
        print(f"✅ Items en la orden: {len(created_order.order_items)}")
        
        # Mostrar detalles de la orden
        print("\n📦 Detalles de la orden:")
        for item in created_order.order_items:
            print(f"  - {item.product.name} x{item.quantity} = ${float(item.price):.2f}")
        
        print(f"\n💰 Total: ${float(created_order.total):.2f}")
        print(f"📅 Fecha: {created_order.created_at}")
        print(f"📋 Estado: {created_order.status}")

if __name__ == '__main__':
    test_checkout_process()
