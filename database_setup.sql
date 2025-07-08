# Configuración de la base de datos MySQL

# 1. Instalar MySQL Server si no está instalado
# 2. Crear la base de datos ejecutando los siguientes comandos en MySQL:

CREATE DATABASE ecommerce_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

# 3. Crear un usuario para la aplicación (opcional, pero recomendado):
CREATE USER 'ecommerce_user'@'localhost' IDENTIFIED BY 'tu_password_segura';
GRANT ALL PRIVILEGES ON ecommerce_db.* TO 'ecommerce_user'@'localhost';
FLUSH PRIVILEGES;

# 4. Actualizar la cadena de conexión en app.py si usas usuario personalizado:
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://ecommerce_user:tu_password_segura@localhost/ecommerce_db'

# Comandos para Windows con XAMPP:
# - Iniciar Apache y MySQL desde el panel de control de XAMPP
# - Acceder a phpMyAdmin en http://localhost/phpmyadmin
# - Crear la base de datos 'ecommerce_db' desde la interfaz web

# Para instalar dependencias de Python:
# pip install pymysql

# También puedes usar mysql-connector-python como alternativa:
# pip install mysql-connector-python
