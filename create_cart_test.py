"""
Script para crear un archivo de prueba simple del carrito
CecyShop - Desarrollado por Sergio Ibañez
"""

# Crear archivo de prueba HTML simple
html_content = '''<!DOCTYPE html>
<html>
<head>
    <title>Prueba Carrito - CecyShop</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
    <style>
        body { font-family: Arial, sans-serif; padding: 20px; }
        .btn { padding: 10px 20px; margin: 10px; cursor: pointer; }
        .btn-primary { background: #27ae60; color: white; border: none; border-radius: 5px; }
        .test-section { margin: 20px 0; padding: 20px; border: 1px solid #ddd; border-radius: 5px; }
        .debug { background: #f8f9fa; padding: 10px; margin: 10px 0; font-family: monospace; font-size: 12px; }
    </style>
</head>
<body>
    <h1>🛒 Prueba de Carrito - CecyShop</h1>
    
    <div class="test-section">
        <h2>Prueba Manual del Carrito</h2>
        <p>Haz clic en los botones para probar la funcionalidad:</p>
        
        <button class="btn btn-primary add-to-cart" data-product-id="1">
            <i class="fas fa-shopping-cart"></i> Agregar Producto 1
        </button>
        
        <button class="btn btn-primary add-to-cart" data-product-id="2">
            <i class="fas fa-shopping-cart"></i> Agregar Producto 2
        </button>
        
        <button class="btn btn-primary" onclick="testCartDirectly()">
            <i class="fas fa-test-tube"></i> Prueba Directa
        </button>
    </div>
    
    <div class="test-section">
        <h2>Debug Information</h2>
        <div id="debug-info" class="debug"></div>
    </div>
    
    <script>
        function log(message) {
            console.log(message);
            const debugDiv = document.getElementById('debug-info');
            debugDiv.innerHTML += new Date().toLocaleTimeString() + ': ' + message + '<br>';
        }
        
        log('Test page loaded');
        
        // Configurar botones
        document.addEventListener('DOMContentLoaded', function() {
            log('DOM loaded, setting up buttons...');
            
            const buttons = document.querySelectorAll('.add-to-cart');
            log('Found ' + buttons.length + ' buttons');
            
            buttons.forEach((button, index) => {
                const productId = button.getAttribute('data-product-id');
                log('Button ' + index + ': Product ID = ' + productId);
                
                button.addEventListener('click', function(e) {
                    e.preventDefault();
                    log('Button clicked for product: ' + productId);
                    addToCart(productId);
                });
            });
        });
        
        // Función para agregar al carrito
        function addToCart(productId) {
            log('Attempting to add product ' + productId + ' to cart...');
            
            fetch('/add_to_cart/' + productId)
                .then(response => {
                    log('Response status: ' + response.status);
                    if (!response.ok) {
                        throw new Error('HTTP ' + response.status);
                    }
                    return response.json();
                })
                .then(data => {
                    log('Success: ' + JSON.stringify(data));
                    alert('Éxito: ' + data.message);
                })
                .catch(error => {
                    log('Error: ' + error.message);
                    alert('Error: ' + error.message);
                });
        }
        
        // Prueba directa
        function testCartDirectly() {
            log('Testing cart directly...');
            fetch('/add_to_cart/1')
                .then(response => response.text())
                .then(text => {
                    log('Raw response: ' + text.substring(0, 200));
                    try {
                        const data = JSON.parse(text);
                        log('Parsed JSON: ' + JSON.stringify(data));
                    } catch (e) {
                        log('Not JSON response: ' + e.message);
                    }
                })
                .catch(error => {
                    log('Fetch error: ' + error.message);
                });
        }
    </script>
</body>
</html>'''

# Escribir archivo
with open('cart_test.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print("✅ Archivo de prueba creado: cart_test.html")
print()
print("🔧 Para probar:")
print("1. Asegúrate de que el servidor esté ejecutándose")
print("2. Abre cart_test.html en tu navegador")
print("3. Abre las herramientas de desarrollador (F12)")
print("4. Ve a la pestaña Console")
print("5. Haz clic en los botones y observa los mensajes")
print()
print("🌐 O visita: http://localhost:5000/cart_test.html")
print("   (si colocas el archivo en la carpeta templates/)")
