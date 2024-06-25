from django.contrib import admin
from .models import User, Customer, Product, DiscountCode, Order

admin.site.register(User)
admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(DiscountCode)
admin.site.register(Order)
