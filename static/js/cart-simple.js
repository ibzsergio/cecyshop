// Script simplificado para CecyShop - Solo funcionalidad del carrito
console.log('CecyShop - Carrito script loaded');

// Esperar a que el DOM esté listo
document.addEventListener('DOMContentLoaded', function() {
    console.log('DOM loaded - Setting up cart buttons...');
    
    // Encontrar todos los botones de agregar al carrito
    const addToCartButtons = document.querySelectorAll('.add-to-cart');
    console.log(`Found ${addToCartButtons.length} add-to-cart buttons`);
    
    // Configurar cada botón
    addToCartButtons.forEach((button, index) => {
        const productId = button.getAttribute('data-product-id');
        console.log(`Button ${index}: Product ID = ${productId}`);
        
        // Agregar event listener
        button.addEventListener('click', function(e) {
            e.preventDefault();
            console.log(`CLICK DETECTED - Product: ${productId}`);
            
            // Deshabilitar botón
            button.disabled = true;
            const originalText = button.innerHTML;
            button.innerHTML = '<i class="fas fa-spinner fa-spin"></i> Agregando...';
            
            // Hacer petición al servidor
            fetch(`/add_to_cart/${productId}`)
                .then(response => {
                    console.log(`Response status: ${response.status}`);
                    if (!response.ok) {
                        throw new Error(`HTTP ${response.status}`);
                    }
                    return response.json();
                })
                .then(data => {
                    console.log('Response data:', data);
                    
                    // Restaurar botón
                    button.disabled = false;
                    button.innerHTML = originalText;
                    
                    if (data.success) {
                        alert('✅ ' + data.message);
                        // Actualizar contador del carrito
                        updateCartCount();
                    } else {
                        alert('❌ ' + (data.message || 'Error al agregar producto'));
                    }
                })
                .catch(error => {
                    console.error('Error:', error);
                    
                    // Restaurar botón
                    button.disabled = false;
                    button.innerHTML = originalText;
                    
                    alert('❌ Error de conexión: ' + error.message);
                });
        });
    });
    
    // Función para actualizar el contador del carrito
    function updateCartCount() {
        const cartCount = document.getElementById('cartCount');
        if (cartCount) {
            fetch('/api/cart/count')
                .then(response => response.json())
                .then(data => {
                    cartCount.textContent = data.count || 0;
                    cartCount.style.display = data.count > 0 ? 'inline-block' : 'none';
                })
                .catch(error => {
                    console.error('Error updating cart count:', error);
                });
        }
    }
    
    // Actualizar contador al cargar la página
    updateCartCount();
});

// Función global para actualizar cantidades en el carrito
function updateQuantity(itemId, change) {
    console.log(`Updating quantity for item ${itemId} by ${change}`);
    
    const quantityElement = document.getElementById(`qty-${itemId}`);
    const totalElement = document.getElementById(`total-${itemId}`);
    
    if (!quantityElement) {
        console.error('No se encontró el elemento de cantidad');
        alert('Error: No se encontró el elemento de cantidad');
        return;
    }
    
    let currentQuantity = parseInt(quantityElement.textContent);
    let newQuantity = Math.max(1, currentQuantity + change);
    
    console.log(`Current quantity: ${currentQuantity}, New quantity: ${newQuantity}`);
    
    // Actualizar en el servidor
    fetch('/api/cart/update', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            item_id: itemId,
            quantity: newQuantity
        })
    })
    .then(response => {
        console.log(`Update response status: ${response.status}`);
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        return response.json();
    })
    .then(data => {
        console.log('Update response data:', data);
        
        if (data.success) {
            // Actualizar cantidad en la interfaz
            quantityElement.textContent = newQuantity;
            
            // Actualizar total del item
            if (totalElement && data.item_total) {
                const formattedTotal = `$${parseFloat(data.item_total).toFixed(2)} MXN`;
                totalElement.textContent = formattedTotal;
            }
            
            // Actualizar totales generales
            updateCartTotals();
            
            // Mostrar mensaje de éxito
            alert('✅ Cantidad actualizada');
        } else {
            alert('❌ ' + (data.message || 'Error al actualizar cantidad'));
        }
    })
    .catch(error => {
        console.error('Error updating quantity:', error);
        alert('❌ Error al actualizar cantidad: ' + error.message);
    });
}

// Función para actualizar totales del carrito
function updateCartTotals() {
    const subtotalElement = document.getElementById('subtotal');
    const grandTotalElement = document.getElementById('grandTotal');
    
    if (!subtotalElement) return;
    
    let subtotal = 0;
    const totalElements = document.querySelectorAll('[id^="total-"]');
    
    totalElements.forEach(element => {
        const value = parseFloat(element.textContent.replace(/[$,MXN\s]/g, ''));
        if (!isNaN(value)) {
            subtotal += value;
        }
    });
    
    const formattedSubtotal = `$${subtotal.toFixed(2)} MXN`;
    subtotalElement.textContent = formattedSubtotal;
    if (grandTotalElement) {
        grandTotalElement.textContent = formattedSubtotal;
    }
}

console.log('CecyShop - Cart script setup complete');
