from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .models import Product, Customer, Order, DiscountCode, User
from .forms import CustomerRegistrationForm, UserRegistrationForm, UserPasswordChangeForm
from django.contrib.auth.decorators import user_passes_test
import datetime

def home(request):
    return render(request, 'main/home.html')

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        print(request.POST)
        user = authenticate(request, username=username, password=password)
        print(user)
        if user is not None:
            login(request, user)
            if user.role == User.ADMIN:
                return redirect('admin_panel')
            elif user.role == User.CUSTOMER:
                return redirect('customer_panel')
            else:
                messages.error(request, 'Invalid user role.')
                return redirect('login')
        else:
            messages.error(request, 'Invalid username or password.')
            return redirect('login')
    else:
        return render(request, 'main/login.html')

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registration successful.')
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request, 'main/register.html', {'form': form})

@login_required
def customer_panel(request):
    if request.user.role != User.CUSTOMER:
        return redirect('main/admin_panel.html')  # Redirect non-customers to another view

    #wallet_balance = request.user.extrainfos.wallet_balance
    return render(request, 'main/customer_panel.html', {'wallet_balance': 0})#wallet_balance})

@login_required
def new_order(request):
    if request.user.role != User.CUSTOMER:
        return redirect('admin_panel')
    products = Product.objects.all()
    customer = Customer.objects.get(user=request.user)
    if request.method == 'POST':
        product_id = request.POST['product_id']
        quantity = int(request.POST['quantity'])
        product = Product.objects.get(id=product_id)
        if product.stock < quantity:
            messages.error(request, 'Not enough stock available.')
        else:
            total_price = product.price * quantity
            use_wallet = request.POST.get('use_wallet', 'off') == 'on'
            discount_code = request.POST.get('discount_code', '').strip()
            discount = 0
            if discount_code:
                try:
                    code = DiscountCode.objects.get(code=discount_code, used=False)
                    if code.expiration_date < datetime.date.today():
                        messages.error(request, 'Discount code expired.')
                    else:
                        discount = total_price * (code.discount_percentage / 100)
                        code.used = True
                        code.save()
                except DiscountCode.DoesNotExist:
                    messages.error(request, 'Invalid discount code.')
            if use_wallet and customer.wallet_balance >= total_price:
                customer.wallet_balance -= total_price - discount
                customer.save()
                total_price = 0
            else:
                total_price -= discount
            order = Order.objects.create(customer=customer, product=product, quantity=quantity, total_price=total_price)
            product.stock -= quantity
            product.save()
            customer.wallet_balance -= total_price
            customer.save()
            messages.success(request, 'Order placed successfully.')
            return redirect('order_history')
    return render(request, 'main/new_order.html', {'products': products, 'wallet_balance': customer.wallet_balance})

@login_required
def order_history(request):
    if request.user.role != User.CUSTOMER:
        return redirect('admin_panel')
    customer = Customer.objects.get(user=request.user)
    orders = Order.objects.filter(customer=customer)
    return render(request, 'main/order_history.html', {'orders': orders})

@login_required
def change_password(request):
    if request.method == 'POST':
        form = UserPasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Password changed successfully.')
            return redirect('customer_panel')
    else:
        form = UserPasswordChangeForm(user=request.user)
    return render(request, 'main/change_password.html', {'form': form})


def is_admin(user):
    return user.is_authenticated and user.role == User.ADMIN

@user_passes_test(is_admin)
def admin_panel(request):
    return render(request, 'main/admin_panel.html')

@user_passes_test(is_admin)
def add_product(request):
    if request.method == 'POST':
        code = request.POST['code']
        name = request.POST['name']
        price = request.POST['price']
        stock = request.POST['stock']
        if Product.objects.filter(code=code).exists():
            messages.error(request, 'Product with this code already exists.')
        else:
            Product.objects.create(code=code, name=name, price=price, stock=stock)
            messages.success(request, 'Product added successfully.')
    return render(request, 'main/add_product.html')

@user_passes_test(is_admin)
def update_stock(request):
    if request.method == 'POST':
        code = request.POST['product_id']
        stock = request.POST['stock']
        try:
            product = Product.objects.get(id=code)
            product.stock = stock
            product.save()
            messages.success(request, 'Stock updated successfully.')
        except Product.DoesNotExist:
            messages.error(request, 'Product not found.')

    products = Product.objects.all()
    
    return render(request, 'main/update_stock.html', {'products': products})

@user_passes_test(is_admin)
def update_price(request):
    if request.method == 'POST':
        code = request.POST['product_id']
        price = request.POST['price']
        try:
            product = Product.objects.get(id=code)
            product.price = price
            product.save()
            messages.success(request, 'Price updated successfully.')
        except Product.DoesNotExist:
            messages.error(request, 'Product not found.')

    products = Product.objects.all()

    return render(request, 'main/update_price.html', {'products': products})
