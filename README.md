# 🌱 CecyShop - E-commerce Minimalista

CecyShop es una aplicación web completa de comercio electrónico desarrollada con Flask, MySQL y diseño minimalista en tonos verdes. Incluye funcionalidades de carrito de compras, panel de administración, sistema de autenticación y procesamiento de pagos.

## 📋 Tabla de Contenidos

- [Características](#características)
- [Tecnologías Utilizadas](#tecnologías-utilizadas)
- [Instalación](#instalación)
- [Configuración](#configuración)
- [Uso](#uso)
- [Estructura del Proyecto](#estructura-del-proyecto)
- [API Endpoints](#api-endpoints)
- [Base de Datos](#base-de-datos)
- [Funcionalidades](#funcionalidades)
- [Seguridad](#seguridad)
- [Responsive Design](#responsive-design)
- [Contribuir](#contribuir)
- [Licencia](#licencia)

## ✨ Características

### 🛍️ Para Clientes
- **Catálogo de productos** con más de 20 productos de muestra
- **Carrito de compras** interactivo y persistente
- **Proceso de checkout** completo con validación
- **Sistema de autenticación** seguro (registro/login)
- **Historial de pedidos** personalizado
- **Interfaz responsive** para móviles y desktop
- **Búsqueda y filtros** de productos

### 👨‍💼 Para Administradores
- **Panel de administración** completo
- **Gestión de productos** (crear, editar, eliminar)
- **Dashboard con estadísticas** de ventas
- **Gestión de pedidos** y estados
- **Control de inventario** automático
- **Subida de imágenes** para productos

### 🎨 Diseño
- **Interfaz minimalista** en tonos verdes
- **Menú flotante** atractivo y funcional
- **Animaciones suaves** y transiciones
- **Diseño totalmente responsive**
- **UX optimizada** para conversiones

## 🛠️ Tecnologías Utilizadas

### Backend
- **Flask** 2.3.3 - Framework web de Python
- **Flask-SQLAlchemy** - ORM para base de datos
- **Flask-Login** - Gestión de sesiones de usuario
- **MySQL** - Base de datos relacional
- **PyMySQL** - Conector MySQL para Python
- **Werkzeug** - Herramientas WSGI

### Frontend
- **HTML5** - Estructura semántica
- **CSS3** - Estilos con variables CSS y Flexbox/Grid
- **JavaScript ES6+** - Interactividad y AJAX
- **Font Awesome** - Iconografía
- **Responsive Design** - Mobile-first approach

### Herramientas
- **Jinja2** - Motor de plantillas
- **Python-dotenv** - Gestión de variables de entorno

## 📦 Instalación

### Prerrequisitos
- Python 3.8 o superior
- MySQL Server 8.0 o superior
- pip (gestor de paquetes de Python)

### Paso 1: Clonar el repositorio
```bash
git clone https://github.com/tu-usuario/cecyshop.git
cd cecyshop
```

### Paso 2: Crear entorno virtual
```bash
python -m venv venv

# Windows
venv\Scripts\activate

# macOS/Linux
source venv/bin/activate
```

### Paso 3: Instalar dependencias
```bash
pip install -r requirements.txt
```

### Paso 4: Configurar MySQL
```sql
-- Conectar a MySQL como root
mysql -u root -p

-- Crear base de datos
CREATE DATABASE ecommerce_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- Crear usuario (opcional)
CREATE USER 'ecommerce_user'@'localhost' IDENTIFIED BY 'tu_password';
GRANT ALL PRIVILEGES ON ecommerce_db.* TO 'ecommerce_user'@'localhost';
FLUSH PRIVILEGES;
```

### Paso 5: Configurar variables de entorno
```bash
# Copiar archivo de ejemplo
cp .env.example .env

# Editar .env con tus configuraciones
# DATABASE_URL=mysql://root:password@localhost/ecommerce_db
```

### Paso 6: Inicializar base de datos y datos de prueba
```bash
python populate_db.py
```

### Paso 7: Ejecutar aplicación
```bash
python app.py
```

La aplicación estará disponible en: `http://localhost:5000`

## ⚙️ Configuración

### Variables de Entorno
Crea un archivo `.env` basado en `.env.example`:

```env
SECRET_KEY=tu_clave_secreta_muy_segura
DATABASE_URL=mysql://root:password@localhost/ecommerce_db
DEBUG=True
UPLOAD_FOLDER=static/uploads
```

### Configuración de Base de Datos
La aplicación soporta diferentes configuraciones de MySQL:

```python
# Configuración básica (app.py)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:password@localhost/ecommerce_db'

# Con usuario personalizado
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://usuario:password@localhost/ecommerce_db'

# Con puerto personalizado
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:password@localhost:3307/ecommerce_db'
```

## 📖 Uso

### Credenciales por Defecto

**Administrador:**
- Usuario: `admin`
- Contraseña: `admin123`

**Usuario de Prueba:**
- Usuario: `usuario_prueba`
- Contraseña: `123456`

### Flujo de Usuario

1. **Registro/Login:** Los usuarios pueden crear cuenta o iniciar sesión
2. **Explorar productos:** Navegar por el catálogo de 20+ productos
3. **Agregar al carrito:** Seleccionar productos y cantidades
4. **Checkout:** Completar información de envío y pago
5. **Confirmación:** Recibir confirmación de pedido

### Flujo de Administrador

1. **Login como admin:** Usar credenciales de administrador
2. **Dashboard:** Ver estadísticas de ventas y productos
3. **Gestionar productos:** Crear, editar y eliminar productos
4. **Ver pedidos:** Monitorear pedidos de clientes

## 📁 Estructura del Proyecto

```
cecyshop/
├── app.py                 # Aplicación principal Flask
├── requirements.txt       # Dependencias de Python
├── populate_db.py        # Script para datos de prueba
├── database_setup.sql    # Configuración de MySQL
├── .env.example          # Plantilla de variables de entorno
├── README.md             # Documentación
├── templates/            # Plantillas HTML
│   ├── base.html         # Plantilla base
│   ├── index.html        # Página principal
│   ├── login.html        # Página de login
│   ├── register.html     # Página de registro
│   ├── cart.html         # Carrito de compras
│   ├── checkout.html     # Proceso de pago
│   ├── orders.html       # Historial de pedidos
│   ├── product_detail.html # Detalle de producto
│   └── admin/            # Plantillas de administración
│       ├── dashboard.html
│       ├── products.html
│       ├── add_product.html
│       └── edit_product.html
├── static/               # Archivos estáticos
│   ├── css/
│   │   └── style.css     # Estilos CSS principales
│   ├── js/
│   │   └── script.js     # JavaScript principal
│   ├── images/           # Imágenes del proyecto
│   └── uploads/          # Imágenes subidas por usuarios
```

## 🔌 API Endpoints

### Rutas Principales
```
GET  /                    # Página principal con productos
GET  /login               # Página de login
POST /login               # Procesar login
GET  /register            # Página de registro
POST /register            # Procesar registro
GET  /logout              # Cerrar sesión
```

### Rutas de Productos
```
GET  /product/<id>        # Detalle de producto
GET  /add_to_cart/<id>    # Agregar producto al carrito
```

### Rutas de Carrito y Compras
```
GET  /cart                # Ver carrito
GET  /remove_from_cart/<id> # Eliminar del carrito
GET  /checkout            # Página de checkout
POST /checkout            # Procesar compra
GET  /orders              # Historial de pedidos
```

### Rutas de Administración
```
GET  /admin               # Dashboard de administración
GET  /admin/products      # Lista de productos
GET  /admin/product/add   # Formulario agregar producto
POST /admin/product/add   # Crear producto
GET  /admin/product/edit/<id> # Formulario editar producto
POST /admin/product/edit/<id> # Actualizar producto
GET  /admin/product/delete/<id> # Eliminar producto
```

## 🗄️ Base de Datos

### Modelo de Datos

#### Tabla `user`
```sql
id              INT PRIMARY KEY AUTO_INCREMENT
username        VARCHAR(80) UNIQUE NOT NULL
email           VARCHAR(120) UNIQUE NOT NULL
password_hash   VARCHAR(255) NOT NULL
is_admin        BOOLEAN DEFAULT FALSE
created_at      DATETIME DEFAULT CURRENT_TIMESTAMP
```

#### Tabla `product`
```sql
id              INT PRIMARY KEY AUTO_INCREMENT
name            VARCHAR(100) NOT NULL
description     TEXT
price           DECIMAL(10,2) NOT NULL
image_url       VARCHAR(255)
stock           INT DEFAULT 0
category        VARCHAR(50)
created_at      DATETIME DEFAULT CURRENT_TIMESTAMP
```

#### Tabla `cart_item`
```sql
id              INT PRIMARY KEY AUTO_INCREMENT
user_id         INT FOREIGN KEY REFERENCES user(id)
product_id      INT FOREIGN KEY REFERENCES product(id)
quantity        INT DEFAULT 1
```

#### Tabla `order`
```sql
id              INT PRIMARY KEY AUTO_INCREMENT
user_id         INT FOREIGN KEY REFERENCES user(id)
total           DECIMAL(10,2) NOT NULL
status          VARCHAR(20) DEFAULT 'pending'
created_at      DATETIME DEFAULT CURRENT_TIMESTAMP
```

#### Tabla `order_item`
```sql
id              INT PRIMARY KEY AUTO_INCREMENT
order_id        INT FOREIGN KEY REFERENCES order(id)
product_id      INT FOREIGN KEY REFERENCES product(id)
quantity        INT NOT NULL
price           DECIMAL(10,2) NOT NULL
```

## 🔧 Funcionalidades

### Sistema de Autenticación
- **Registro de usuarios** con validación de email
- **Login seguro** con hash de contraseñas
- **Gestión de sesiones** con Flask-Login
- **Protección de rutas** administrativas

### Carrito de Compras
- **Persistencia de carrito** por usuario
- **Actualización de cantidades** en tiempo real
- **Cálculo automático** de totales
- **Validación de stock** disponible

### Panel de Administración
- **Dashboard con métricas** de ventas
- **CRUD completo** de productos
- **Gestión de inventario** automática
- **Estadísticas visuales** de negocio

### Procesamiento de Pagos
- **Formulario de checkout** completo
- **Validación de datos** de pago
- **Simulación de procesamiento** (listo para integrar payment gateway)
- **Confirmación de pedidos** automática

## 🔒 Seguridad

### Medidas Implementadas
- **Hash de contraseñas** con Werkzeug
- **Protección CSRF** con tokens
- **Validación de formularios** en cliente y servidor
- **Sanitización de entradas** automática con SQLAlchemy
- **Sesiones seguras** con Flask-Login
- **Variables de entorno** para datos sensibles

### Configuración de Seguridad
```python
# Configuración de seguridad en app.py
app.config['SECRET_KEY'] = secrets.token_hex(16)
app.config['WTF_CSRF_ENABLED'] = True
app.config['WTF_CSRF_TIME_LIMIT'] = None
```

## 📱 Responsive Design

### Breakpoints
- **Desktop:** > 1200px - Layout completo
- **Tablet:** 768px - 1200px - Grid adaptado
- **Mobile:** < 768px - Layout de una columna
- **Small Mobile:** < 480px - Interfaz optimizada

### Características Responsive
- **Menú hamburguesa** en móviles
- **Grid de productos** adaptativo
- **Formularios optimizados** para touch
- **Navegación simplificada** en pantallas pequeñas

## 🎨 Personalización

### Colores Principales (CSS Variables)
```css
:root {
    --primary-color: #27ae60;      /* Verde principal */
    --primary-dark: #229954;       /* Verde oscuro */
    --primary-light: #58d68d;      /* Verde claro */
    --secondary-color: #2c3e50;    /* Gris oscuro */
    --accent-color: #f39c12;       /* Naranja de acento */
}
```

### Tipografía
- **Fuente principal:** Arial, sans-serif
- **Tamaños responsivos** con rem
- **Jerarquía clara** de headings

## 🚀 Deployment

### Preparación para Producción
1. **Configurar variables de entorno**
2. **Usar base de datos remota**
3. **Configurar servidor web** (Nginx + Gunicorn)
4. **Activar SSL/HTTPS**
5. **Configurar dominio personalizado**

### Docker (Opcional)
```dockerfile
FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 5000
CMD ["python", "app.py"]
```

## 📊 Performance

### Optimizaciones Implementadas
- **Lazy loading** de imágenes
- **Minificación** de CSS/JS
- **Compresión** de imágenes
- **Cache** de consultas frecuentes
- **CDN** para Font Awesome

## 🧪 Testing

### Datos de Prueba
El script `populate_db.py` crea:
- **20+ productos** de muestra
- **Usuarios de prueba** con diferentes roles
- **Categorías diversas** de productos
- **Datos realistas** para testing

## 🤝 Contribuir

1. **Fork** el proyecto
2. **Crear rama** para nueva funcionalidad
3. **Commit** cambios con mensajes descriptivos
4. **Push** a la rama
5. **Crear Pull Request**

### Guías de Contribución
- Seguir **PEP 8** para Python
- **Comentar código** complejo
- **Probar funcionalidades** antes de PR
- **Actualizar documentación** si es necesario

## 📝 Notas de Desarrollo

### Próximas Mejoras
- [ ] Integración con **payment gateway real**
- [ ] **Sistema de reviews** de productos
- [ ] **Wishlist** de usuarios
- [ ] **Notificaciones email** automáticas
- [ ] **API REST** completa
- [ ] **Dashboard analytics** avanzado
- [ ] **Multi-idioma** (i18n)
- [ ] **PWA** (Progressive Web App)

### Problemas Conocidos
- Integración de pagos es **simulada**
- Imágenes de productos usan **URLs externas**
- No hay **sistema de envío** real
- **Cache** no implementado para producción

## 📄 Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo `LICENSE` para más detalles.

## 📞 Soporte

Para soporte técnico o preguntas:
- **Email:** soporte@cecyshop.com
- **Issues:** GitHub Issues
- **Documentación:** Este README

---

**Desarrollado con 💚 por Sergio Ibañez**

*¿Te gusta el proyecto? ¡Dale una ⭐ en GitHub!*
