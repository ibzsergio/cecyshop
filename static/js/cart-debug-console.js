// Debug script para verificar funciones del carrito
console.log('=== DEBUG CARRITO ===');

// Verificar que las funciones existan
setTimeout(() => {
    console.log('Verificando funciones...');
    console.log('updateQuantity exists:', typeof updateQuantity);
    console.log('updateCartTotals exists:', typeof updateCartTotals);
    
    // Verificar elementos del DOM
    const qtyElements = document.querySelectorAll('[id^="qty-"]');
    console.log('Elementos de cantidad encontrados:', qtyElements.length);
    
    qtyElements.forEach(el => {
        console.log('Elemento:', el.id, 'Valor:', el.textContent);
    });
    
    const totalElements = document.querySelectorAll('[id^="total-"]');
    console.log('Elementos de total encontrados:', totalElements.length);
    
    totalElements.forEach(el => {
        console.log('Total:', el.id, 'Valor:', el.textContent);
    });
    
    // Verificar botones
    const qtyButtons = document.querySelectorAll('.qty-btn');
    console.log('Botones de cantidad encontrados:', qtyButtons.length);
    
    qtyButtons.forEach((btn, index) => {
        console.log(`Botón ${index}:`, btn.onclick);
    });
    
}, 1000);

// Función de prueba manual
window.testQuantityUpdate = function(itemId, change) {
    console.log(`Testing quantity update: item ${itemId}, change ${change}`);
    
    if (typeof updateQuantity === 'function') {
        updateQuantity(itemId, change);
    } else {
        console.error('updateQuantity function not found!');
    }
};

console.log('Debug script loaded. Use testQuantityUpdate(itemId, change) to test manually.');
