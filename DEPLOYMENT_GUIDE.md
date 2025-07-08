# Guía de Despliegue - CecyShop

## Opciones de Hosting para CecyShop

### 1. 🚀 Railway (Recomendado - Gratis)

**Railway** es una plataforma moderna que facilita el despliegue de aplicaciones Python.

#### Pasos para Railway:

1. **Crear cuenta en Railway**
   - Ve a https://railway.app
   - Regístrate con GitHub o email

2. **Preparar tu proyecto**
   ```bash
   # Subir a GitHub primero
   git init
   git add .
   git commit -m "Initial commit"
   git remote add origin https://github.com/tu-usuario/cecyshop.git
   git push -u origin main
   ```

3. **Desplegar en Railway**
   - Conecta tu repositorio GitHub
   - Railway detectará automáticamente que es una app Flask
   - Configura las variables de entorno:
     - `SECRET_KEY`: tu_clave_secreta_segura
     - `DEBUG`: False
     - `DATABASE_URL`: (Railway puede proveer una BD MySQL)

4. **URL pública**: Railway te dará una URL como `https://cecyshop.up.railway.app`

---

### 2. 🌐 Render (Alternativa Gratis)

#### Pasos para Render:

1. **Crear cuenta en Render**
   - Ve a https://render.com
   - Conecta tu GitHub

2. **Crear Web Service**
   - Conecta tu repositorio
   - Configuración:
     - Build Command: `pip install -r requirements.txt`
     - Start Command: `gunicorn app:app`

3. **Variables de entorno**:
   - `SECRET_KEY`: tu_clave_secreta
   - `DEBUG`: False

---

### 3. ☁️ Heroku (Opción Paga)

#### Pasos para Heroku:

1. **Instalar Heroku CLI**
   ```bash
   # Crear app
   heroku create cecyshop-tu-nombre
   
   # Configurar variables
   heroku config:set SECRET_KEY=tu_clave_secreta
   heroku config:set DEBUG=False
   
   # Desplegar
   git push heroku main
   ```

---

### 4. 🏠 PythonAnywhere (Gratis con limitaciones)

#### Pasos para PythonAnywhere:

1. **Crear cuenta gratis en pythonanywhere.com**
2. **Subir archivos via Files o Git**
3. **Configurar Web App**:
   - Python 3.8+
   - Framework: Flask
   - Código fuente: `/home/tu-usuario/cecyshop`

---

### 5. 💻 Servidor Propio con Ngrok (Para pruebas)

#### Opción rápida para mostrar desde tu PC:

1. **Instalar ngrok**
   - Descarga desde https://ngrok.com
   - Crear cuenta gratuita

2. **Ejecutar tu app localmente**
   ```bash
   python app.py
   ```

3. **Exponer con ngrok**
   ```bash
   ngrok http 5000
   ```

4. **URL pública temporal**: `https://abc123.ngrok.io`

---

## 🗄️ Base de Datos para Producción

### Opciones de BD MySQL:

1. **Railway MySQL** (Incluido con Railway)
2. **PlanetScale** (Gratis hasta 1GB)
3. **FreeSQLDatabase.com** (MySQL gratis)
4. **ClearDB** (Heroku addon)

### Configuración de BD:

En tu archivo `.env` de producción:
```env
DATABASE_URL=mysql+pymysql://usuario:password@host:puerto/nombre_bd
SECRET_KEY=clave_super_secreta_cambiar_en_produccion
DEBUG=False
```

---

## 🚦 Preparación Final

### Antes del despliegue, asegúrate de:

1. ✅ Cambiar `DEBUG=False` en producción
2. ✅ Usar una `SECRET_KEY` segura y única
3. ✅ Configurar base de datos de producción
4. ✅ Probar localmente con `gunicorn app:app`
5. ✅ Subir archivos estáticos (imágenes, CSS, JS)

### Comando para probar localmente:
```bash
# Instalar dependencias
pip install -r requirements.txt

# Probar con gunicorn
gunicorn app:app

# Acceder en http://localhost:8000
```

---

## 📱 Acceso desde Cualquier Dispositivo

Una vez desplegado, tu sitio será accesible desde:
- ✅ Computadoras (Windows, Mac, Linux)
- ✅ Smartphones (Android, iPhone)
- ✅ Tablets
- ✅ Smart TVs con navegador
- ✅ Cualquier dispositivo con internet

### URL típicas según plataforma:
- **Railway**: `https://cecyshop.up.railway.app`
- **Render**: `https://cecyshop.onrender.com`
- **Heroku**: `https://cecyshop-app.herokuapp.com`
- **PythonAnywhere**: `https://tu-usuario.pythonanywhere.com`

---

## 🆘 Solución de Problemas

### Error común: "Application Error"
- Verificar logs de la plataforma
- Comprobar variables de entorno
- Verificar que `requirements.txt` esté actualizado

### Error de BD:
- Verificar `DATABASE_URL` en variables de entorno
- Comprobar credenciales de base de datos
- Verificar que la BD esté creada

### Archivos estáticos no cargan:
- Verificar que la carpeta `static/` esté incluida
- Comprobar rutas en templates
- Verificar configuración de archivos estáticos

---

## 💡 Recomendación Final

**Para comenzar rápidamente**: Usa **Railway** o **Ngrok**
- Railway para despliegue permanente
- Ngrok para pruebas rápidas y demos

¡Tu CecyShop estará disponible en internet en menos de 10 minutos! 🎉
