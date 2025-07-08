import os
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename
from sqlalchemy import Numeric
import os
from datetime import datetime
import secrets

app = Flask(__name__)

# Configuración
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', secrets.token_hex(16))

# Configuración de base de datos
database_url = os.getenv('DATABASE_URL')
if database_url:
    app.config['SQLALCHEMY_DATABASE_URI'] = database_url
else:
    # Configuración local por defecto para XAMPP
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/cecyshop_db'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['UPLOAD_FOLDER'] = 'static/uploads'

# Inicializar extensiones
db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

# Crear directorio de uploads si no existe
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Modelos de base de datos
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    is_admin = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    price = db.Column(Numeric(10, 2), nullable=False)
    image_url = db.Column(db.String(255))
    stock = db.Column(db.Integer, default=0)
    category = db.Column(db.String(50))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

class CartItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    quantity = db.Column(db.Integer, default=1)
    product = db.relationship('Product')

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    total = db.Column(Numeric(10, 2), nullable=False)
    status = db.Column(db.String(20), default='pending')
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    user = db.relationship('User')
    order_items = db.relationship('OrderItem', backref='order', lazy=True)

class OrderItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey('order.id'), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    price = db.Column(Numeric(10, 2), nullable=False)
    product = db.relationship('Product')

# Filtro personalizado para formatear precios en pesos mexicanos
@app.template_filter('mxn')
def format_mxn(value):
    """Formatear precio en pesos mexicanos"""
    if value is None:
        return "$0.00 MXN"
    try:
        # Convertir a float si es necesario
        if hasattr(value, '__float__'):
            value = float(value)
        return f"${value:,.2f} MXN"
    except (ValueError, TypeError):
        return "$0.00 MXN"

# Función auxiliar para cálculos
def safe_float(value):
    """Convertir Decimal a float de manera segura"""
    return float(value) if value is not None else 0.0

# Rutas principales
@app.route('/')
def index():
    products = Product.query.limit(20).all()
    return render_template('index.html', products=products)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        
        if user and check_password_hash(user.password_hash, password):
            login_user(user)
            # Redirigir a admin si es administrador
            if user.is_admin:
                flash(f'Bienvenido administrador {user.username}')
                return redirect(url_for('admin_dashboard'))
            else:
                flash(f'Bienvenido {user.username}')
                return redirect(url_for('index'))
        else:
            flash('Usuario o contraseña incorrectos')
    
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        
        if User.query.filter_by(username=username).first():
            flash('El usuario ya existe')
            return render_template('register.html')
        
        user = User(
            username=username,
            email=email,
            password_hash=generate_password_hash(password)
        )
        db.session.add(user)
        db.session.commit()
        
        flash('Registro exitoso')
        return redirect(url_for('login'))
    
    return render_template('register.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/product/<int:id>')
def product_detail(id):
    product = Product.query.get_or_404(id)
    return render_template('product_detail.html', product=product)

@app.route('/add_to_cart/<int:product_id>')
@login_required
def add_to_cart(product_id):
    try:
        # Verificar que el producto existe
        product = Product.query.get(product_id)
        if not product:
            return jsonify({'success': False, 'message': 'Producto no encontrado'})
        
        # Verificar stock
        if product.stock <= 0:
            return jsonify({'success': False, 'message': 'Producto sin stock'})
        
        cart_item = CartItem.query.filter_by(user_id=current_user.id, product_id=product_id).first()
        
        if cart_item:
            # Verificar que no exceda el stock
            if cart_item.quantity + 1 > product.stock:
                return jsonify({'success': False, 'message': 'Stock insuficiente'})
            cart_item.quantity += 1
        else:
            cart_item = CartItem(user_id=current_user.id, product_id=product_id, quantity=1)
            db.session.add(cart_item)
        
        db.session.commit()
        return jsonify({'success': True, 'message': 'Producto agregado al carrito'})
        
    except Exception as e:
        db.session.rollback()
        return jsonify({'success': False, 'message': f'Error: {str(e)}'})

@app.route('/cart')
@login_required
def cart():
    cart_items = CartItem.query.filter_by(user_id=current_user.id).all()
    total = sum(safe_float(item.product.price) * item.quantity for item in cart_items)
    return render_template('cart.html', cart_items=cart_items, total=total)

@app.route('/remove_from_cart/<int:item_id>')
@login_required
def remove_from_cart(item_id):
    cart_item = CartItem.query.get_or_404(item_id)
    if cart_item.user_id == current_user.id:
        db.session.delete(cart_item)
        db.session.commit()
    return redirect(url_for('cart'))

@app.route('/checkout', methods=['GET', 'POST'])
@login_required
def checkout():
    cart_items = CartItem.query.filter_by(user_id=current_user.id).all()
    
    if not cart_items:
        flash('Tu carrito está vacío')
        return redirect(url_for('cart'))
    
    if request.method == 'POST':
        total = sum(safe_float(item.product.price) * item.quantity for item in cart_items)
        
        # Crear orden
        order = Order(user_id=current_user.id, total=total, status='completed')
        db.session.add(order)
        db.session.flush()
        
        # Crear items de la orden
        for item in cart_items:
            order_item = OrderItem(
                order_id=order.id,
                product_id=item.product_id,
                quantity=item.quantity,
                price=safe_float(item.product.price)
            )
            db.session.add(order_item)
        
        # Limpiar carrito
        CartItem.query.filter_by(user_id=current_user.id).delete()
        db.session.commit()
        
        flash('Compra realizada exitosamente')
        return redirect(url_for('orders'))
    
    total = sum(safe_float(item.product.price) * item.quantity for item in cart_items)
    return render_template('checkout.html', cart_items=cart_items, total=total)

@app.route('/orders')
@login_required
def orders():
    user_orders = Order.query.filter_by(user_id=current_user.id).order_by(Order.created_at.desc()).all()
    return render_template('orders.html', orders=user_orders)

@app.route('/api/cart/update', methods=['POST'])
@login_required
def update_cart_quantity():
    """API para actualizar cantidad de items en el carrito"""
    try:
        data = request.get_json()
        item_id = data.get('item_id')
        quantity = data.get('quantity', 1)
        
        # Validar cantidad
        if quantity < 1:
            return jsonify({'success': False, 'message': 'Cantidad debe ser mayor a 0'})
        
        # Buscar el item del carrito
        cart_item = CartItem.query.filter_by(id=item_id, user_id=current_user.id).first()
        
        if not cart_item:
            return jsonify({'success': False, 'message': 'Item no encontrado'})
        
        # Actualizar cantidad
        cart_item.quantity = quantity
        db.session.commit()
        
        # Calcular nuevo total del item
        item_total = safe_float(cart_item.product.price) * quantity
        
        # Calcular total del carrito
        cart_items = CartItem.query.filter_by(user_id=current_user.id).all()
        cart_total = sum(safe_float(item.product.price) * item.quantity for item in cart_items)
        
        return jsonify({
            'success': True,
            'item_total': item_total,
            'cart_total': cart_total,
            'message': 'Cantidad actualizada correctamente'
        })
        
    except Exception as e:
        return jsonify({'success': False, 'message': f'Error: {str(e)}'})

# API para obtener el conteo del carrito
@app.route('/api/cart/count')
@login_required
def get_cart_count():
    count = CartItem.query.filter_by(user_id=current_user.id).count()
    return jsonify({'count': count})

# Panel de administración
@app.route('/admin')
@login_required
def admin_dashboard():
    if not current_user.is_admin:
        flash('Acceso denegado')
        return redirect(url_for('index'))
    
    products = Product.query.all()
    orders = Order.query.order_by(Order.created_at.desc()).all()
    return render_template('admin/dashboard.html', products=products, orders=orders)

@app.route('/admin/products')
@login_required
def admin_products():
    if not current_user.is_admin:
        return redirect(url_for('index'))
    
    products = Product.query.all()
    return render_template('admin/products.html', products=products)

@app.route('/admin/product/add', methods=['GET', 'POST'])
@login_required
def admin_add_product():
    if not current_user.is_admin:
        return redirect(url_for('index'))
    
    if request.method == 'POST':
        product = Product(
            name=request.form['name'],
            description=request.form['description'],
            price=float(request.form['price']),
            image_url=request.form['image_url'],
            stock=int(request.form['stock']),
            category=request.form['category']
        )
        db.session.add(product)
        db.session.commit()
        flash('Producto agregado exitosamente')
        return redirect(url_for('admin_products'))
    
    return render_template('admin/add_product.html')

@app.route('/admin/product/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def admin_edit_product(id):
    if not current_user.is_admin:
        return redirect(url_for('index'))
    
    product = Product.query.get_or_404(id)
    
    if request.method == 'POST':
        product.name = request.form['name']
        product.description = request.form['description']
        product.price = float(request.form['price'])
        product.image_url = request.form['image_url']
        product.stock = int(request.form['stock'])
        product.category = request.form['category']
        db.session.commit()
        flash('Producto actualizado exitosamente')
        return redirect(url_for('admin_products'))
    
    return render_template('admin/edit_product.html', product=product)

@app.route('/admin/product/delete/<int:id>')
@login_required
def admin_delete_product(id):
    if not current_user.is_admin:
        return redirect(url_for('index'))
    
    product = Product.query.get_or_404(id)
    db.session.delete(product)
    db.session.commit()
    flash('Producto eliminado exitosamente')
    return redirect(url_for('admin_products'))

# Rutas para reportes
@app.route('/admin/reports')
@login_required
def admin_reports():
    if not current_user.is_admin:
        return redirect(url_for('index'))
    
    # Obtener estadísticas generales
    total_products = Product.query.count()
    total_orders = Order.query.count()
    total_users = User.query.count()
    total_revenue = db.session.query(db.func.sum(Order.total)).scalar() or 0
    
    # Productos más vendidos
    top_products = db.session.query(
        Product.name,
        Product.price,
        db.func.sum(OrderItem.quantity).label('total_sold')
    ).join(OrderItem).group_by(Product.id).order_by(db.desc('total_sold')).limit(10).all()
    
    # Ventas por mes (últimos 12 meses)
    from datetime import datetime, timedelta
    twelve_months_ago = datetime.now() - timedelta(days=365)
    
    monthly_sales = db.session.query(
        db.func.date_format(Order.created_at, '%Y-%m').label('month'),
        db.func.sum(Order.total).label('total')
    ).filter(Order.created_at >= twelve_months_ago).group_by('month').order_by('month').all()
    
    # Pedidos recientes
    recent_orders = Order.query.order_by(Order.created_at.desc()).limit(10).all()
    
    return render_template('admin/reports.html', 
                         total_products=total_products,
                         total_orders=total_orders,
                         total_users=total_users,
                         total_revenue=total_revenue,
                         top_products=top_products,
                         monthly_sales=monthly_sales,
                         recent_orders=recent_orders)

@app.route('/admin/reports/sales')
@login_required
def admin_sales_report():
    if not current_user.is_admin:
        return redirect(url_for('index'))
    
    # Obtener filtros de fecha
    from datetime import datetime, timedelta
    end_date = request.args.get('end_date', datetime.now().strftime('%Y-%m-%d'))
    start_date = request.args.get('start_date', (datetime.now() - timedelta(days=30)).strftime('%Y-%m-%d'))
    
    # Convertir a datetime
    start_datetime = datetime.strptime(start_date, '%Y-%m-%d')
    end_datetime = datetime.strptime(end_date, '%Y-%m-%d') + timedelta(days=1)
    
    # Obtener pedidos en el rango de fechas
    orders = Order.query.filter(
        Order.created_at >= start_datetime,
        Order.created_at < end_datetime
    ).order_by(Order.created_at.desc()).all()
    
    # Calcular totales
    total_sales = sum(safe_float(order.total) for order in orders)
    total_orders = len(orders)
    
    return render_template('admin/sales_report.html',
                         orders=orders,
                         total_sales=total_sales,
                         total_orders=total_orders,
                         start_date=start_date,
                         end_date=end_date)

@app.route('/admin/reports/products')
@login_required
def admin_products_report():
    if not current_user.is_admin:
        return redirect(url_for('index'))
    
    # Productos con stock bajo
    low_stock_products = Product.query.filter(Product.stock < 10).all()
    
    # Productos más vendidos
    top_products = db.session.query(
        Product.name,
        Product.price,
        Product.stock,
        db.func.sum(OrderItem.quantity).label('total_sold'),
        db.func.sum(OrderItem.quantity * OrderItem.price).label('total_revenue')
    ).join(OrderItem).group_by(Product.id).order_by(db.desc('total_sold')).all()
    
    # Productos nunca vendidos
    never_sold = db.session.query(Product).outerjoin(OrderItem).filter(OrderItem.id == None).all()
    
    return render_template('admin/products_report.html',
                         low_stock_products=low_stock_products,
                         top_products=top_products,
                         never_sold=never_sold)

@app.route('/admin/reports/print/<report_type>')
@login_required
def print_report(report_type):
    if not current_user.is_admin:
        return redirect(url_for('index'))
    
    if report_type == 'sales':
        return redirect(url_for('admin_sales_report') + '?print=true')
    elif report_type == 'products':
        return redirect(url_for('admin_products_report') + '?print=true')
    else:
        return redirect(url_for('admin_reports') + '?print=true')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        
        # Crear usuario administrador si no existe
        admin = User.query.filter_by(username='admin').first()
        if not admin:
            admin = User(
                username='admin',
                email='admin@cecyshop.com',
                password_hash=generate_password_hash('admin123'),
                is_admin=True
            )
            db.session.add(admin)
            db.session.commit()
    
    # Usar puerto de la variable de entorno o 5000 por defecto
    port = int(os.getenv('PORT', 5000))
    debug_mode = os.getenv('DEBUG', 'True').lower() == 'true'
    
    app.run(host='0.0.0.0', port=port, debug=debug_mode)
