// Script simplificado para CecyShop - Debug del carrito
console.log('CecyShop cart debug script loaded');

// Función simple de alerta
function showMessage(message, type = 'info') {
    alert(message);
    console.log(`${type.toUpperCase()}: ${message}`);
}

// Función principal para agregar al carrito
function addProductToCart(productId) {
    console.log('Adding product to cart:', productId);
    
    fetch(`/add_to_cart/${productId}`)
        .then(response => {
            console.log('Response status:', response.status);
            if (!response.ok) {
                throw new Error(`HTTP ${response.status}`);
            }
            return response.json();
        })
        .then(data => {
            console.log('Response data:', data);
            if (data.success) {
                showMessage(data.message, 'success');
                updateCartDisplay();
            } else {
                showMessage(data.message || 'Error desconocido', 'error');
            }
        })
        .catch(error => {
            console.error('Error:', error);
            showMessage('Error de conexión: ' + error.message, 'error');
        });
}

// Configurar botones cuando el DOM esté listo
document.addEventListener('DOMContentLoaded', function() {
    console.log('DOM loaded, setting up cart buttons...');
    
    // Buscar todos los botones de agregar al carrito
    const buttons = document.querySelectorAll('.add-to-cart');
    console.log(`Found ${buttons.length} cart buttons`);
    
    // Configurar cada botón
    buttons.forEach((button, index) => {
        const productId = button.getAttribute('data-product-id');
        console.log(`Button ${index}: Product ID = ${productId}`);
        
        if (productId) {
            button.addEventListener('click', function(e) {
                e.preventDefault();
                console.log(`Clicked button for product ${productId}`);
                
                // Cambiar texto del botón
                const originalText = this.innerHTML;
                this.innerHTML = '<i class="fas fa-spinner fa-spin"></i> Agregando...';
                this.disabled = true;
                
                // Agregar al carrito
                addProductToCart(productId);
                
                // Restaurar botón después de 2 segundos
                setTimeout(() => {
                    this.innerHTML = originalText;
                    this.disabled = false;
                }, 2000);
            });
        } else {
            console.warn(`Button ${index} has no product ID`);
        }
    });
    
    // Si no se encontraron botones, mostrar información de debug
    if (buttons.length === 0) {
        console.log('No cart buttons found. Checking page content...');
        console.log('Page content:', document.body.innerHTML.substring(0, 500));
    }
});

// Función para actualizar contador del carrito
function updateCartDisplay() {
    console.log('Updating cart display...');
    
    // Buscar el contador del carrito
    const cartCount = document.getElementById('cartCount');
    if (cartCount) {
        // En una implementación real, esto se obtendría del servidor
        const currentCount = parseInt(cartCount.textContent) || 0;
        cartCount.textContent = currentCount + 1;
        cartCount.style.display = 'inline-block';
        console.log('Cart count updated to:', currentCount + 1);
    }
}

// Función de prueba manual
function testCart() {
    console.log('Testing cart functionality...');
    const buttons = document.querySelectorAll('.add-to-cart');
    
    if (buttons.length > 0) {
        const firstButton = buttons[0];
        const productId = firstButton.getAttribute('data-product-id');
        console.log('Testing with first button, product ID:', productId);
        addProductToCart(productId);
    } else {
        console.log('No buttons to test');
    }
}

// Exponer función de prueba globalmente
window.testCart = testCart;

console.log('Cart debug script setup complete. Use testCart() in console to test manually.');
