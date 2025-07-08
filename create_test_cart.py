#!/usr/bin/env python3
"""
Script para crear datos de prueba en el carrito
"""
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from app import app, db, User, Product, CartItem
from flask_login import login_user

def create_test_cart():
    with app.app_context():
        # Buscar usuario admin
        admin_user = User.query.filter_by(is_admin=True).first()
        if not admin_user:
            print("No se encontró usuario admin")
            return
        
        # Buscar productos
        products = Product.query.limit(3).all()
        if not products:
            print("No se encontraron productos")
            return
        
        # Limpiar carrito existente
        CartItem.query.filter_by(user_id=admin_user.id).delete()
        
        # Crear items de prueba en el carrito
        for i, product in enumerate(products):
            cart_item = CartItem(
                user_id=admin_user.id,
                product_id=product.id,
                quantity=i + 1  # 1, 2, 3 cantidades
            )
            db.session.add(cart_item)
        
        db.session.commit()
        print(f"✅ Carrito creado para usuario {admin_user.username}")
        print(f"✅ Agregados {len(products)} productos al carrito")
        
        # Mostrar contenido del carrito
        cart_items = CartItem.query.filter_by(user_id=admin_user.id).all()
        print("\n📦 Contenido del carrito:")
        for item in cart_items:
            print(f"  - {item.product.name} (ID: {item.id}) - Cantidad: {item.quantity}")

if __name__ == '__main__':
    create_test_cart()
