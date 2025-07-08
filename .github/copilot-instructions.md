<!-- Use this file to provide workspace-specific custom instructions to Copilot. For more details, visit https://code.visualstudio.com/docs/copilot/copilot-customization#_use-a-githubcopilotinstructionsmd-file -->

# CecyShop - E-commerce Application

Este es un proyecto de e-commerce completo desarrollado con Flask, MySQL y diseño minimalista.

## Contexto del Proyecto

CecyShop es una aplicación web de comercio electrónico que incluye:
- Sistema de autenticación de usuarios
- Carrito de compras funcional
- Panel de administración completo
- Gestión de productos e inventario
- Procesamiento de pedidos
- Diseño responsive minimalista en tonos verdes

## Tecnologías Utilizadas

- **Backend**: Flask, SQLAlchemy, Flask-Login
- **Base de datos**: MySQL
- **Frontend**: HTML5, CSS3, JavaScript ES6+
- **Estilos**: CSS personalizado con variables, Flexbox y Grid
- **Iconos**: Font Awesome

## Estructura de Archivos

- `app.py`: Aplicación principal Flask con todas las rutas
- `templates/`: Plantillas HTML con Jinja2
- `static/css/style.css`: Estilos CSS principales
- `static/js/script.js`: JavaScript para interactividad
- `populate_db.py`: Script para poblar la base de datos con datos de prueba

## Instrucciones para Copilot

Cuando trabajes en este proyecto:

1. **Mantén el estilo minimalista**: Usa la paleta de colores verde definida en las variables CSS
2. **Sigue las convenciones de Flask**: Usa blueprints si agregar nuevas rutas complejas
3. **Diseño responsive**: Asegúrate de que nuevas funcionalidades sean mobile-friendly
4. **Seguridad**: Siempre valida datos de entrada y usa autenticación apropiada
5. **Base de datos**: Usa SQLAlchemy ORM para todas las operaciones de base de datos
6. **Consistencia**: Mantén el mismo patrón de nomenclatura y estructura de archivos

## Patrones de Código

- Las rutas principales están en `app.py`
- Las plantillas extienden `base.html`
- Los estilos usan variables CSS definidas en `:root`
- JavaScript está modularizado en funciones específicas
- Los formularios incluyen validación cliente y servidor

## Variables CSS Principales

```css
--primary-color: #27ae60;    /* Verde principal */
--primary-dark: #229954;     /* Verde oscuro */
--secondary-color: #2c3e50;  /* Gris oscuro */
--light-bg: #f8f9fa;         /* Fondo claro */
```

Al generar código para este proyecto, mantén estos patrones y asegúrate de que las nuevas funcionalidades se integren bien con la arquitectura existente.
