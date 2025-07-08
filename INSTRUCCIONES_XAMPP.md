# 🚀 INSTRUCCIONES PARA XAMPP - CecyShop

## Pasos para configurar CecyShop con XAMPP:

### 1. INICIAR XAMPP
- Abre el **Panel de Control de XAMPP**
- Inicia **Apache** y **MySQL**
- Verifica que ambos servicios estén en verde (ejecutándose)

### 2. ACCEDER A phpMyAdmin
- Abre tu navegador
- Ve a: `http://localhost/phpmyadmin`
- Deberías ver la interfaz de phpMyAdmin

### 3. EJECUTAR EL SCRIPT SQL
- En phpMyAdmin, haz clic en la pestaña **"SQL"**
- Abre el archivo `setup_database.sql` en un editor de texto
- **Copia todo el contenido** del archivo
- **Pega el contenido** en el área de texto de phpMyAdmin
- Haz clic en el botón **"Continuar"** o **"Go"**

### 4. VERIFICAR LA CREACIÓN
Después de ejecutar el script, deberías ver:
- ✅ Base de datos `ecommerce_db` creada
- ✅ 5 tablas creadas (user, product, cart_item, order, order_item)
- ✅ 2 usuarios insertados
- ✅ 22 productos de muestra insertados

### 5. INSTALAR DEPENDENCIAS DE PYTHON
Abre una terminal/PowerShell en la carpeta del proyecto y ejecuta:
```bash
pip install -r requirements.txt
```

### 6. EJECUTAR LA APLICACIÓN
```bash
python app.py
```

### 7. ACCEDER A LA APLICACIÓN
- Abre tu navegador
- Ve a: `http://localhost:5000`
- ¡Tu tienda CecyShop estará funcionando!

## 🔑 CREDENCIALES DE ACCESO:

### Administrador:
- **Usuario:** `admin`
- **Contraseña:** `admin123`

### Usuario de Prueba:
- **Usuario:** `usuario_prueba`
- **Contraseña:** `123456`

## 🛠️ CONFIGURACIÓN DE XAMPP:

### Si MySQL no inicia:
1. Ve a la pestaña **"Config"** → **"my.ini"**
2. Busca la línea: `#innodb_force_recovery = 1`
3. Descomenta la línea (quita el #)
4. Reinicia MySQL

### Si el puerto 3306 está ocupado:
1. Ve a **"Config"** → **"my.ini"**
2. Cambia `port = 3306` por `port = 3307`
3. Actualiza la conexión en `app.py`:
   ```python
   app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost:3307/ecommerce_db'
   ```

## 📊 VERIFICAR DATOS:

En phpMyAdmin, puedes verificar que todo esté correcto:

### Tabla `user`:
```sql
SELECT * FROM user;
```
Debería mostrar 2 usuarios (admin y usuario_prueba)

### Tabla `product`:
```sql
SELECT name, price, category FROM product;
```
Debería mostrar 22 productos en diferentes categorías

### Contar productos por categoría:
```sql
SELECT category, COUNT(*) as cantidad 
FROM product 
GROUP BY category;
```

## 🚨 SOLUCIÓN DE PROBLEMAS:

### Error "Access denied for user 'root'":
- XAMPP por defecto no tiene contraseña para root
- Verifica que la conexión sea: `mysql://root:@localhost/ecommerce_db`

### Error "Unknown database 'ecommerce_db'":
- Ejecuta nuevamente el script SQL
- Verifica que la primera línea sea: `CREATE DATABASE IF NOT EXISTS ecommerce_db`

### Error "No module named 'pymysql'":
```bash
pip install pymysql
```

### Error de puerto:
- Verifica que MySQL esté ejecutándose en el puerto correcto
- Por defecto XAMPP usa el puerto 3306

## 📱 PROBAR LA APLICACIÓN:

1. **Página principal:** Deberías ver 22 productos
2. **Login como admin:** Acceso al panel de administración
3. **Agregar productos:** Funcionalidad completa de CRUD
4. **Carrito de compras:** Agregar/quitar productos
5. **Checkout:** Proceso completo de compra

¡Tu aplicación CecyShop está lista para usar! 🌱
