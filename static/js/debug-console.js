// Script de debug para CecyShop - Ejecutar en consola del navegador
console.log('=== CecyShop Debug Script ===');

// Verificar si los botones existen
const buttons = document.querySelectorAll('.add-to-cart');
console.log(`Botones encontrados: ${buttons.length}`);

buttons.forEach((btn, index) => {
    const productId = btn.getAttribute('data-product-id');
    console.log(`Botón ${index}: ID del producto = ${productId}`);
    
    // Agregar listener de debug
    btn.addEventListener('click', function(e) {
        e.preventDefault();
        console.log(`CLICK DETECTADO - Producto: ${productId}`);
        alert(`Botón clickeado para producto: ${productId}`);
        
        // Hacer petición al servidor
        fetch(`/add_to_cart/${productId}`)
            .then(response => {
                console.log('Response:', response);
                return response.json();
            })
            .then(data => {
                console.log('Data:', data);
                alert(JSON.stringify(data));
            })
            .catch(error => {
                console.error('Error:', error);
                alert('Error: ' + error.message);
            });
    });
});

// Verificar el estado del DOM
console.log('DOM readyState:', document.readyState);
console.log('Scripts cargados:', document.scripts.length);

// Verificar si las funciones están definidas
console.log('setupCartFunctionality exists:', typeof setupCartFunctionality);
console.log('addToCart exists:', typeof addToCart);

// Función manual para agregar al carrito
window.testAddToCart = function(productId) {
    console.log('Testing add to cart for product:', productId);
    
    fetch(`/add_to_cart/${productId}`)
        .then(response => response.json())
        .then(data => {
            console.log('Response:', data);
            alert(data.message || 'Respuesta recibida');
        })
        .catch(error => {
            console.error('Error:', error);
            alert('Error: ' + error.message);
        });
};

console.log('=== Script de debug cargado ===');
console.log('Puedes usar testAddToCart(1) para probar manualmente');
