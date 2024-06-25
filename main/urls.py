from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .forms import UserLoginForm

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('customer_panel/', views.customer_panel, name='customer_panel'),
    path('new_order/', views.new_order, name='new_order'),
    path('order_history/', views.order_history, name='order_history'),
    path('change_password/', views.change_password, name='change_password'),
    path('admin_panel/', views.admin_panel, name='admin_panel'),
    path('add_product/', views.add_product, name='add_product'),
    path('update_stock/', views.update_stock, name='update_stock'),
    path('update_price/', views.update_price, name='update_price'),
]
