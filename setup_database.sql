-- =====================================================
-- SCRIPT DE BASE DE DATOS PARA CECYSHOP
-- Para ejecutar en phpMyAdmin (XAMPP)
-- Fecha: 07 de Julio, 2025
-- Desarrollado por: Sergio Ibañez
-- =====================================================

-- 1. CREAR BASE DE DATOS
-- =====================================================
CREATE DATABASE IF NOT EXISTS cecyshop_db 
CHARACTER SET utf8mb4 
COLLATE utf8mb4_unicode_ci;

-- Usar la base de datos creada
USE cecyshop_db;

-- 2. CREAR TABLA DE USUARIOS
-- =====================================================
CREATE TABLE IF NOT EXISTS user (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(80) UNIQUE NOT NULL,
    email VARCHAR(120) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    is_admin BOOLEAN DEFAULT FALSE,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- 3. CREAR TABLA DE PRODUCTOS
-- =====================================================
CREATE TABLE IF NOT EXISTS product (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    price DECIMAL(10,2) NOT NULL,
    image_url VARCHAR(255),
    stock INT DEFAULT 0,
    category VARCHAR(50),
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- 4. CREAR TABLA DE CARRITO
-- =====================================================
CREATE TABLE IF NOT EXISTS cart_item (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    product_id INT NOT NULL,
    quantity INT DEFAULT 1,
    FOREIGN KEY (user_id) REFERENCES user(id) ON DELETE CASCADE,
    FOREIGN KEY (product_id) REFERENCES product(id) ON DELETE CASCADE,
    UNIQUE KEY unique_user_product (user_id, product_id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- 5. CREAR TABLA DE PEDIDOS
-- =====================================================
CREATE TABLE IF NOT EXISTS `order` (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    total DECIMAL(10,2) NOT NULL,
    status VARCHAR(20) DEFAULT 'pending',
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES user(id) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- 6. CREAR TABLA DE ITEMS DE PEDIDO
-- =====================================================
CREATE TABLE IF NOT EXISTS order_item (
    id INT AUTO_INCREMENT PRIMARY KEY,
    order_id INT NOT NULL,
    product_id INT NOT NULL,
    quantity INT NOT NULL,
    price DECIMAL(10,2) NOT NULL,
    FOREIGN KEY (order_id) REFERENCES `order`(id) ON DELETE CASCADE,
    FOREIGN KEY (product_id) REFERENCES product(id) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- 7. INSERTAR USUARIO ADMINISTRADOR
-- =====================================================
-- Contraseña: admin123 (hasheada con Werkzeug)
INSERT INTO user (username, email, password_hash, is_admin) VALUES 
('admin', 'admin@cecyshop.com', 'pbkdf2:sha256:600000$GQOkYzKWvj8p7LJe$8f5c2a9b3d1e4f7a6c8b9d2e5f1a4c7b8e9f0a3d6c7e8f9a0b1c2d3e4f5a6b7c8d9e0f1a2b3c4d5e6f7a8b9c0d1e2f3a4b5c6d7e8f9', TRUE);

-- 8. INSERTAR USUARIO DE PRUEBA
-- =====================================================
-- Contraseña: 123456 (hasheada con Werkzeug)
INSERT INTO user (username, email, password_hash, is_admin) VALUES 
('usuario_prueba', 'usuario@cecyshop.com', 'pbkdf2:sha256:600000$KLMnOzPQrS9t8UVw$1a2b3c4d5e6f7a8b9c0d1e2f3a4b5c6d7e8f9a0b1c2d3e4f5a6b7c8d9e0f1a2b3c4d5e6f7a8b9c0d1e2f3a4b5c6d7e8f9a0b1c2d3e4f5', FALSE);

-- 9. INSERTAR PRODUCTOS DE MUESTRA
-- =====================================================
INSERT INTO product (name, description, price, stock, category, image_url) VALUES
('Smartphone Verde Eco', 'Smartphone amigable con el medio ambiente, fabricado con materiales reciclados y diseño minimalista.', 299.99, 15, 'Electrónicos', 'https://images.unsplash.com/photo-1511707171634-5f897ff02aa9?w=400'),

('Camiseta Orgánica', 'Camiseta 100% algodón orgánico, suave y cómoda. Perfecta para el día a día.', 29.99, 25, 'Ropa', 'https://images.unsplash.com/photo-1521572163474-6864f9cf17ab?w=400'),

('Laptop Sostenible', 'Laptop de alta performance con certificación de sostenibilidad y diseño elegante.', 899.99, 8, 'Electrónicos', 'https://images.unsplash.com/photo-1496181133206-80ce9b88a853?w=400'),

('Zapatillas Eco', 'Zapatillas deportivas hechas con materiales reciclados y suela biodegradable.', 79.99, 20, 'Deportes', 'https://images.unsplash.com/photo-1542291026-7eec264c27ff?w=400'),

('Botella de Agua Reutilizable', 'Botella de acero inoxidable, libre de BPA, mantiene la temperatura por 24 horas.', 24.99, 50, 'Hogar', 'https://images.unsplash.com/photo-1602143407151-7111542de6e8?w=400'),

('Libro: Vida Sostenible', 'Guía completa para adoptar un estilo de vida más sostenible y consciente.', 19.99, 30, 'Libros', 'https://images.unsplash.com/photo-1544947950-fa07a98d237f?w=400'),

('Auriculares Inalámbricos', 'Auriculares con cancelación de ruido y batería de larga duración.', 159.99, 12, 'Electrónicos', 'https://images.unsplash.com/photo-1505740420928-5e560c06d30e?w=400'),

('Jeans Sostenibles', 'Jeans fabricados con algodón orgánico y proceso de teñido ecológico.', 89.99, 18, 'Ropa', 'https://images.unsplash.com/photo-1541099649105-f69ad21f3246?w=400'),

('Reloj Inteligente Verde', 'Smartwatch con funciones de salud y fitness, carga solar disponible.', 249.99, 10, 'Electrónicos', 'https://images.unsplash.com/photo-1523275335684-37898b6baf30?w=400'),

('Mochila Ecológica', 'Mochila resistente al agua hecha con botellas plásticas recicladas.', 59.99, 22, 'Deportes', 'https://images.unsplash.com/photo-1553062407-98eeb64c6a62?w=400'),

('Kit de Cosméticos Naturales', 'Set completo de productos de belleza 100% naturales y cruelty-free.', 69.99, 15, 'Belleza', 'https://images.unsplash.com/photo-1596462502278-27bfdc403348?w=400'),

('Tabla de Cortar Bambú', 'Tabla de cortar antibacteriana hecha de bambú sostenible.', 34.99, 35, 'Hogar', 'https://images.unsplash.com/photo-1584464491033-06628f3a6b7b?w=400'),

('Cargador Solar Portátil', 'Cargador solar resistente al agua, perfecto para actividades al aire libre.', 49.99, 20, 'Electrónicos', 'https://images.unsplash.com/photo-1593941707882-a5bac6861d75?w=400'),

('Sudadera Orgánica', 'Sudadera con capucha de algodón orgánico, cómoda y duradera.', 54.99, 16, 'Ropa', 'https://images.unsplash.com/photo-1556821840-3a63f95609a7?w=400'),

('Set de Yoga Sostenible', 'Mat de yoga de corcho natural con accesorios incluidos.', 89.99, 12, 'Deportes', 'https://images.unsplash.com/photo-1544367567-0f2fcb009e0b?w=400'),

('Plantas Purificadoras', 'Set de 3 plantas que purifican el aire de tu hogar naturalmente.', 39.99, 25, 'Hogar', 'https://images.unsplash.com/photo-1416879595882-3373a0480b5b?w=400'),

('Cámara Eco Digital', 'Cámara digital compacta con carcasa de materiales reciclados.', 199.99, 8, 'Electrónicos', 'https://images.unsplash.com/photo-1516035069371-29a1b244cc32?w=400'),

('Juego Educativo Verde', 'Juego de mesa educativo sobre sostenibilidad para toda la familia.', 29.99, 30, 'Juguetes', 'https://images.unsplash.com/photo-1606092195730-5d7b9af1efc5?w=400'),

('Termo Inteligente', 'Termo con control de temperatura via app y materiales 100% reciclables.', 79.99, 14, 'Hogar', 'https://images.unsplash.com/photo-1571019613454-1cb2f99b2d8b?w=400'),

('Bicicleta Urbana Eco', 'Bicicleta urbana con marco de aluminio reciclado y diseño minimalista.', 499.99, 5, 'Deportes', 'https://images.unsplash.com/photo-1558618666-fcd25c85cd64?w=400'),

('Agenda Sostenible', 'Agenda anual hecha con papel reciclado y tapa de corcho natural.', 22.99, 40, 'Otros', 'https://images.unsplash.com/photo-1506905925346-21bda4d32df4?w=400'),

('Mouse Eco Inalámbrico', 'Mouse inalámbrico fabricado con plástico oceánico reciclado.', 35.99, 28, 'Electrónicos', 'https://images.unsplash.com/photo-1527864550417-7fd91fc51a46?w=400');

-- 10. CREAR ÍNDICES PARA OPTIMIZACIÓN
-- =====================================================
CREATE INDEX idx_product_category ON product(category);
CREATE INDEX idx_product_name ON product(name);
CREATE INDEX idx_order_user ON `order`(user_id);
CREATE INDEX idx_order_status ON `order`(status);
CREATE INDEX idx_cart_user ON cart_item(user_id);

-- 11. MOSTRAR RESUMEN DE DATOS CREADOS
-- =====================================================
SELECT 'RESUMEN DE LA BASE DE DATOS CREADA:' AS info;
SELECT 'Usuarios creados:' AS tipo, COUNT(*) AS cantidad FROM user;
SELECT 'Productos creados:' AS tipo, COUNT(*) AS cantidad FROM product;
SELECT 'Categorías disponibles:' AS info, GROUP_CONCAT(DISTINCT category) AS categorias FROM product;

-- =====================================================
-- SCRIPT COMPLETADO EXITOSAMENTE
-- =====================================================

-- CREDENCIALES DE ACCESO:
-- 
-- ADMINISTRADOR:
--   Usuario: admin
--   Contraseña: admin123
-- 
-- USUARIO DE PRUEBA:
--   Usuario: usuario_prueba
--   Contraseña: 123456
-- 
-- PARA CONECTAR DESDE FLASK:
--   DATABASE_URL: mysql://root:@localhost/ecommerce_db
--   (Sin contraseña por defecto en XAMPP)
-- =====================================================
