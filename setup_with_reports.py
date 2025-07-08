"""
Script completo para configurar CecyShop con reportes
CecyShop - Desarrollado por Sergio Ibañez
"""

from setup_complete import create_database, setup_admin
from create_sample_orders import create_sample_orders

def main():
    """Configuración completa con reportes"""
    print("🚀 Configurando CecyShop con funcionalidad de reportes...")
    
    # Paso 1: Crear base de datos y configurar admin
    print("\n1️⃣ Configurando base de datos y administrador...")
    if not create_database():
        print("❌ Error en la configuración de base de datos")
        return False
    
    if not setup_admin():
        print("❌ Error en la configuración del administrador")
        return False
    
    # Paso 2: Crear pedidos de ejemplo
    print("\n2️⃣ Creando datos de ejemplo para reportes...")
    if not create_sample_orders():
        print("❌ Error creando datos de ejemplo")
        return False
    
    print("\n🎉 ¡Configuración completada exitosamente!")
    print("\n✨ Nuevas funcionalidades disponibles:")
    print("   📊 Reportes de ventas")
    print("   📋 Reportes de productos")
    print("   📈 Gráficos interactivos")
    print("   🖨️ Función de impresión")
    
    print("\n🔑 Credenciales de administrador:")
    print("   Usuario: admin")
    print("   Contraseña: admin123")
    
    print("\n🌐 URLs disponibles:")
    print("   Panel Admin: http://localhost:5000/admin")
    print("   Reportes: http://localhost:5000/admin/reports")
    print("   Ventas: http://localhost:5000/admin/reports/sales")
    print("   Productos: http://localhost:5000/admin/reports/products")
    
    print("\n🚀 Ejecuta 'python app.py' para iniciar el servidor")
    
    return True

if __name__ == '__main__':
    main()
