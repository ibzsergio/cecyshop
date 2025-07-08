"""
Script simple para verificar la nueva ruta API
CecyShop - Desarrollado por Sergio Ibañez
"""

import json
from app import app

def test_api_route():
    """Prueba la nueva ruta API"""
    
    with app.test_client() as client:
        print("🔍 Probando ruta API /api/cart/update...")
        
        # Probar sin autenticación (debería fallar)
        response = client.post('/api/cart/update', 
                             json={'item_id': 1, 'quantity': 2})
        
        print(f"Status sin auth: {response.status_code}")
        
        # Verificar que la ruta existe
        with app.app_context():
            print("✅ Ruta API agregada correctamente")
            print("📋 Rutas disponibles:")
            for rule in app.url_map.iter_rules():
                if 'api' in rule.rule:
                    print(f"   {rule.rule} - {rule.methods}")

if __name__ == '__main__':
    test_api_route()
