# 🛍️ CecyShop - Despliegue Web

## 🚀 Opciones Rápidas para Publicar tu Sitio

### 1. 💨 Opción MÁS RÁPIDA (Ngrok - 2 minutos)

```bash
# 1. Descarga ngrok desde https://ngrok.com/download
# 2. Ejecuta:
python quick_deploy.py
```

**Resultado**: URL pública inmediata como `https://abc123.ngrok.io`

### 2. 🌐 Opción PERMANENTE (Railway - 10 minutos)

1. **Sube tu código a GitHub**:
   ```bash
   git init
   git add .
   git commit -m "CecyShop inicial"
   git remote add origin https://github.com/tu-usuario/cecyshop.git
   git push -u origin main
   ```

2. **Desplegar en Railway**:
   - Ve a https://railway.app
   - Conecta tu repositorio GitHub
   - Railway detecta automáticamente Flask
   - ¡Listo! URL como `https://cecyshop.up.railway.app`

### 3. 📋 Otras Opciones

Ver archivo `DEPLOYMENT_GUIDE.md` para más plataformas:
- Render (gratis)
- Heroku (pago)
- PythonAnywhere (gratis limitado)

## 🔧 Configuración

### Variables de Entorno para Producción:
```env
SECRET_KEY=tu_clave_super_secreta
DEBUG=False
DATABASE_URL=mysql+pymysql://usuario:pass@host/bd
```

## 📱 Acceso Universal

Una vez desplegado, tu CecyShop funcionará en:
- ✅ Computadoras (Windows/Mac/Linux)
- ✅ Smartphones (Android/iPhone)  
- ✅ Tablets
- ✅ Smart TVs
- ✅ Cualquier dispositivo con internet

## 🎯 Recomendación

**Para comenzar YA**: Usa `python quick_deploy.py` con Ngrok
**Para uso permanente**: Usa Railway o Render

## 🆘 Problemas Comunes

### "Ngrok no encontrado"
Descarga desde https://ngrok.com/download y agrégalo al PATH

### "Error de base de datos"
Para pruebas locales con ngrok, la BD local funcionará bien

### "Archivos estáticos no cargan"
Asegúrate de que la carpeta `static/` esté incluida en tu repositorio

---

## 🎉 ¡En 2 minutos tu CecyShop estará en internet!

Ejecuta: `python quick_deploy.py` y comparte la URL con el mundo! 🌍
