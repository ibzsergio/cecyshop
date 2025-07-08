// Funcionalidad principal de CecyShop
document.addEventListener('DOMContentLoaded', function() {
    console.log('DOM loaded - Initializing CecyShop...');
    initializeApp();
});

function initializeApp() {
    console.log('Initializing app...');
    setupNavigation();
    setupAlerts();
    setupModals();
    setupCartFunctionality();
    setupFormValidation();
    updateCartCount();
    console.log('App initialized successfully!');
}

// Navegación
function setupNavigation() {
    const navToggle = document.getElementById('navToggle');
    const navMenu = document.getElementById('navMenu');
    
    if (navToggle && navMenu) {
        navToggle.addEventListener('click', function() {
            navMenu.classList.toggle('active');
        });
        
        // Cerrar menú al hacer clic fuera
        document.addEventListener('click', function(e) {
            if (!navToggle.contains(e.target) && !navMenu.contains(e.target)) {
                navMenu.classList.remove('active');
            }
        });
    }
    
    // Scroll suave para enlaces internos
    const smoothScrollLinks = document.querySelectorAll('a[href^="#"]');
    smoothScrollLinks.forEach(link => {
        link.addEventListener('click', function(e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });
}

// Sistema de alertas
function setupAlerts() {
    const alerts = document.querySelectorAll('.alert');
    
    alerts.forEach(alert => {
        const closeBtn = alert.querySelector('.alert-close');
        if (closeBtn) {
            closeBtn.addEventListener('click', function() {
                closeAlert(alert);
            });
        }
        
        // Auto-cerrar después de 5 segundos
        setTimeout(() => {
            if (alert.parentNode) {
                closeAlert(alert);
            }
        }, 5000);
    });
}

function closeAlert(alert) {
    alert.style.animation = 'slideOut 0.3s ease forwards';
    setTimeout(() => {
        if (alert.parentNode) {
            alert.parentNode.removeChild(alert);
        }
    }, 300);
}

function showAlert(message, type = 'info') {
    const alertContainer = document.querySelector('.alert-container') || createAlertContainer();
    
    const alertElement = document.createElement('div');
    alertElement.className = `alert alert-${type}`;
    alertElement.innerHTML = `
        <i class="fas fa-${getAlertIcon(type)}"></i>
        ${message}
        <button class="alert-close">&times;</button>
    `;
    
    alertContainer.appendChild(alertElement);
    
    // Configurar cierre
    const closeBtn = alertElement.querySelector('.alert-close');
    closeBtn.addEventListener('click', () => closeAlert(alertElement));
    
    setTimeout(() => closeAlert(alertElement), 5000);
}

function createAlertContainer() {
    const container = document.createElement('div');
    container.className = 'alert-container';
    document.body.appendChild(container);
    return container;
}

function getAlertIcon(type) {
    const icons = {
        'info': 'info-circle',
        'success': 'check-circle',
        'warning': 'exclamation-triangle',
        'error': 'times-circle'
    };
    return icons[type] || 'info-circle';
}

// Sistema de modales
function setupModals() {
    const modals = document.querySelectorAll('.modal');
    
    modals.forEach(modal => {
        const closeButtons = modal.querySelectorAll('.modal-close');
        
        closeButtons.forEach(btn => {
            btn.addEventListener('click', () => closeModal(modal));
        });
        
        // Cerrar al hacer clic en el overlay
        modal.addEventListener('click', function(e) {
            if (e.target === modal) {
                closeModal(modal);
            }
        });
    });
    
    // Cerrar modales con Escape
    document.addEventListener('keydown', function(e) {
        if (e.key === 'Escape') {
            const openModal = document.querySelector('.modal.show');
            if (openModal) {
                closeModal(openModal);
            }
        }
    });
}

function showModal(modalId) {
    const modal = document.getElementById(modalId);
    if (modal) {
        modal.classList.add('show');
        document.body.style.overflow = 'hidden';
    }
}

function closeModal(modal) {
    modal.classList.remove('show');
    document.body.style.overflow = '';
}

// Funcionalidad del carrito
function setupCartFunctionality() {
    console.log('Setting up cart functionality...');
    
    // Botones de agregar al carrito
    const addToCartButtons = document.querySelectorAll('.add-to-cart');
    console.log(`Found ${addToCartButtons.length} add-to-cart buttons`);
    
    addToCartButtons.forEach((button, index) => {
        const productId = button.getAttribute('data-product-id');
        console.log(`Button ${index}: product ID = ${productId}`);
        
        button.addEventListener('click', function(e) {
            e.preventDefault();
            console.log(`Clicked add to cart for product: ${productId}`);
            
            // Deshabilitar botón temporalmente
            this.disabled = true;
            this.innerHTML = '<i class="fas fa-spinner fa-spin"></i> Agregando...';
            
            addToCart(productId, this);
        });
    });
    
    if (addToCartButtons.length === 0) {
        console.log('No add-to-cart buttons found on this page');
    }
}

async function addToCart(productId, button = null) {
    console.log(`Adding product ${productId} to cart...`);
    
    try {
        const response = await fetch(`/add_to_cart/${productId}`, {
            method: 'GET',
            headers: {
                'Accept': 'application/json',
            }
        });
        
        console.log(`Response status: ${response.status}`);
        
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        
        const data = await response.json();
        console.log('Response data:', data);
        
        if (data.success) {
            showAlert(data.message, 'success');
            updateCartCount();
            
            // Restaurar botón
            if (button) {
                button.disabled = false;
                button.innerHTML = '<i class="fas fa-shopping-cart"></i> Agregar';
            }
            
            // Mostrar modal si existe
            const modal = document.getElementById('addedToCartModal');
            if (modal) {
                showModal('addedToCartModal');
            }
        } else {
            showAlert(data.message || 'Error al agregar producto al carrito', 'error');
            
            // Restaurar botón
            if (button) {
                button.disabled = false;
                button.innerHTML = '<i class="fas fa-shopping-cart"></i> Agregar';
            }
        }
    } catch (error) {
        console.error('Error adding to cart:', error);
        showAlert('Error de conexión. Verifica que hayas iniciado sesión.', 'error');
        
        // Restaurar botón
        if (button) {
            button.disabled = false;
            button.innerHTML = '<i class="fas fa-shopping-cart"></i> Agregar';
        }
    }
}

function updateCartCount() {
    // Simular conteo del carrito (en una implementación real, esto vendría del servidor)
    const cartCount = document.getElementById('cartCount');
    if (cartCount) {
        // Obtener cantidad actual del carrito via AJAX
        fetch('/api/cart/count')
            .then(response => response.json())
            .then(data => {
                cartCount.textContent = data.count || 0;
                cartCount.style.display = data.count > 0 ? 'inline-block' : 'none';
            })
            .catch(() => {
                // Fallback: contar items en la página si estamos en el carrito
                const cartItems = document.querySelectorAll('.cart-item');
                cartCount.textContent = cartItems.length;
                cartCount.style.display = cartItems.length > 0 ? 'inline-block' : 'none';
            });
    }
}

function updateQuantity(itemId, change) {
    const quantityElement = document.getElementById(`qty-${itemId}`);
    const totalElement = document.getElementById(`total-${itemId}`);
    
    if (!quantityElement) {
        console.error('No se encontró el elemento de cantidad');
        return;
    }
    
    let currentQuantity = parseInt(quantityElement.textContent);
    let newQuantity = Math.max(1, currentQuantity + change);
    
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
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        return response.json();
    })
    .then data => {
        if (data.success) {
            quantityElement.textContent = newQuantity;
            if (totalElement) {
                totalElement.textContent = `$${data.item_total.toFixed(2)} MXN`;
            }
            updateCartTotals();
            showAlert('Cantidad actualizada', 'success');
        } else {
            showAlert(data.message || 'Error al actualizar cantidad', 'error');
        }
    })
    .catch(error => {
        console.error('Error updating quantity:', error);
        showAlert('Error al actualizar cantidad. Intenta recargar la página.', 'error');
    });
}

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

// Validación de formularios
function setupFormValidation() {
    const forms = document.querySelectorAll('form');
    
    forms.forEach(form => {
        form.addEventListener('submit', function(e) {
            if (!validateForm(form)) {
                e.preventDefault();
            }
        });
        
        // Validación en tiempo real
        const inputs = form.querySelectorAll('input, select, textarea');
        inputs.forEach(input => {
            input.addEventListener('blur', () => validateField(input));
        });
    });
    
    // Formateo de tarjeta de crédito
    const cardNumber = document.getElementById('cardNumber');
    if (cardNumber) {
        cardNumber.addEventListener('input', formatCardNumber);
    }
    
    const expiryDate = document.getElementById('expiryDate');
    if (expiryDate) {
        expiryDate.addEventListener('input', formatExpiryDate);
    }
    
    const cvv = document.getElementById('cvv');
    if (cvv) {
        cvv.addEventListener('input', formatCVV);
    }
}

function validateForm(form) {
    const inputs = form.querySelectorAll('input[required], select[required], textarea[required]');
    let isValid = true;
    
    inputs.forEach(input => {
        if (!validateField(input)) {
            isValid = false;
        }
    });
    
    return isValid;
}

function validateField(field) {
    const value = field.value.trim();
    let isValid = true;
    let message = '';
    
    // Validación requerida
    if (field.hasAttribute('required') && !value) {
        isValid = false;
        message = 'Este campo es requerido';
    }
    
    // Validaciones específicas por tipo
    if (value && field.type === 'email') {
        const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        if (!emailRegex.test(value)) {
            isValid = false;
            message = 'Email inválido';
        }
    }
    
    if (value && field.type === 'tel') {
        const phoneRegex = /^[\d\s\-\+\(\)]+$/;
        if (!phoneRegex.test(value)) {
            isValid = false;
            message = 'Teléfono inválido';
        }
    }
    
    showFieldValidation(field, isValid, message);
    return isValid;
}

function showFieldValidation(field, isValid, message) {
    // Remover validación anterior
    const existingError = field.parentNode.querySelector('.field-error');
    if (existingError) {
        existingError.remove();
    }
    
    field.classList.remove('error', 'success');
    
    if (!isValid && message) {
        field.classList.add('error');
        const errorElement = document.createElement('div');
        errorElement.className = 'field-error';
        errorElement.textContent = message;
        field.parentNode.appendChild(errorElement);
    } else if (field.value.trim()) {
        field.classList.add('success');
    }
}

// Formateo de campos de pago
function formatCardNumber(e) {
    let value = e.target.value.replace(/\s/g, '').replace(/[^0-9]/gi, '');
    let formattedValue = value.match(/.{1,4}/g)?.join(' ') || value;
    
    if (formattedValue !== e.target.value) {
        e.target.value = formattedValue;
    }
}

function formatExpiryDate(e) {
    let value = e.target.value.replace(/\D/g, '');
    if (value.length >= 2) {
        value = value.substring(0, 2) + '/' + value.substring(2, 4);
    }
    e.target.value = value;
}

function formatCVV(e) {
    e.target.value = e.target.value.replace(/\D/g, '').substring(0, 4);
}

// Funciones de utilidad
function debounce(func, wait) {
    let timeout;
    return function executedFunction(...args) {
        const later = () => {
            clearTimeout(timeout);
            func(...args);
        };
        clearTimeout(timeout);
        timeout = setTimeout(later, wait);
    };
}

function throttle(func, limit) {
    let inThrottle;
    return function() {
        const args = arguments;
        const context = this;
        if (!inThrottle) {
            func.apply(context, args);
            inThrottle = true;
            setTimeout(() => inThrottle = false, limit);
        }
    };
}

// Animaciones y efectos
function animateOnScroll() {
    const elements = document.querySelectorAll('.animate-on-scroll');
    
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('animated');
            }
        });
    });
    
    elements.forEach(element => observer.observe(element));
}

// Inicializar animaciones
document.addEventListener('DOMContentLoaded', animateOnScroll);

// Lazy loading de imágenes
function setupLazyLoading() {
    const images = document.querySelectorAll('img[loading="lazy"]');
    
    if ('IntersectionObserver' in window) {
        const imageObserver = new IntersectionObserver((entries, observer) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    const img = entry.target;
                    img.src = img.dataset.src || img.src;
                    img.classList.remove('lazy');
                    observer.unobserve(img);
                }
            });
        });
        
        images.forEach(img => imageObserver.observe(img));
    }
}

// Búsqueda de productos
function setupProductSearch() {
    const searchInput = document.getElementById('productSearch');
    if (!searchInput) return;
    
    const searchProducts = debounce(function(query) {
        const products = document.querySelectorAll('.product-card');
        
        products.forEach(product => {
            const name = product.querySelector('.product-name').textContent.toLowerCase();
            const category = product.querySelector('.product-category').textContent.toLowerCase();
            
            if (name.includes(query.toLowerCase()) || category.includes(query.toLowerCase())) {
                product.style.display = 'block';
            } else {
                product.style.display = 'none';
            }
        });
    }, 300);
    
    searchInput.addEventListener('input', (e) => searchProducts(e.target.value));
}

// Filtros de productos
function setupProductFilters() {
    const categoryFilter = document.getElementById('categoryFilter');
    const priceFilter = document.getElementById('priceFilter');
    
    if (categoryFilter) {
        categoryFilter.addEventListener('change', filterProducts);
    }
    
    if (priceFilter) {
        priceFilter.addEventListener('change', filterProducts);
    }
}

function filterProducts() {
    const categoryFilter = document.getElementById('categoryFilter');
    const priceFilter = document.getElementById('priceFilter');
    
    const selectedCategory = categoryFilter ? categoryFilter.value : '';
    const selectedPriceRange = priceFilter ? priceFilter.value : '';
    
    const products = document.querySelectorAll('.product-card');
    
    products.forEach(product => {
        let showProduct = true;
        
        // Filtro por categoría
        if (selectedCategory) {
            const productCategory = product.querySelector('.product-category').textContent;
            if (productCategory !== selectedCategory) {
                showProduct = false;
            }
        }
        
        // Filtro por precio
        if (selectedPriceRange && showProduct) {
            const priceText = product.querySelector('.price').textContent;
            const price = parseFloat(priceText.replace('$', ''));
            
            switch (selectedPriceRange) {
                case '0-25':
                    showProduct = price <= 25;
                    break;
                case '25-50':
                    showProduct = price > 25 && price <= 50;
                    break;
                case '50-100':
                    showProduct = price > 50 && price <= 100;
                    break;
                case '100+':
                    showProduct = price > 100;
                    break;
            }
        }
        
        product.style.display = showProduct ? 'block' : 'none';
    });
}

// Función de alerta simplificada para debugging
function simpleAlert(message) {
    alert(message);
    console.log('Alert:', message);
}

// Función de prueba del carrito
function testAddToCart(productId) {
    console.log('Testing add to cart with product ID:', productId);
    
    fetch(`/add_to_cart/${productId}`)
        .then(response => {
            console.log('Response received:', response);
            return response.json();
        })
        .then(data => {
            console.log('Data received:', data);
            simpleAlert(data.message || 'Respuesta recibida');
        })
        .catch(error => {
            console.error('Error:', error);
            simpleAlert('Error: ' + error.message);
        });
}

// Función de debug para verificar botones
function debugButtons() {
    const buttons = document.querySelectorAll('.add-to-cart');
    console.log('Debug - Found buttons:', buttons.length);
    
    buttons.forEach((btn, index) => {
        const productId = btn.getAttribute('data-product-id');
        console.log(`Button ${index}: ID=${productId}, element:`, btn);
        
        // Agregar evento de click simple para debug
        btn.onclick = function(e) {
            e.preventDefault();
            console.log('Button clicked!');
            simpleAlert(`Producto ${productId} - funciona!`);
            testAddToCart(productId);
        };
    });
}

// Ejecutar debug al cargar
document.addEventListener('DOMContentLoaded', function() {
    setTimeout(debugButtons, 1000); // Esperar 1 segundo
});

// Inicializar funcionalidades adicionales cuando el DOM esté listo
document.addEventListener('DOMContentLoaded', function() {
    setupLazyLoading();
    setupProductSearch();
    setupProductFilters();
});

// Agregar estilos CSS adicionales para validación
const additionalStyles = `
    .field-error {
        color: var(--danger-color);
        font-size: 0.875rem;
        margin-top: 5px;
    }
    
    input.error, select.error, textarea.error {
        border-color: var(--danger-color);
    }
    
    input.success, select.success, textarea.success {
        border-color: var(--success-color);
    }
    
    .animate-on-scroll {
        opacity: 0;
        transform: translateY(20px);
        transition: opacity 0.6s ease, transform 0.6s ease;
    }
    
    .animate-on-scroll.animated {
        opacity: 1;
        transform: translateY(0);
    }
    
    .lazy {
        opacity: 0;
        transition: opacity 0.3s;
    }
    
    @keyframes slideOut {
        to {
            transform: translateX(100%);
            opacity: 0;
        }
    }
`;

// Agregar estilos al documento
const styleSheet = document.createElement('style');
styleSheet.textContent = additionalStyles;
document.head.appendChild(styleSheet);
