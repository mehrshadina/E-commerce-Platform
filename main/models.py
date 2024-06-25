from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    ADMIN = 1
    CUSTOMER = 2
    ROLE_CHOICES = (
        (ADMIN, 'Admin'),
        (CUSTOMER, 'Customer'),
    )
    role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, null=True, blank=True)

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_set',  # Update the related_name
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        related_query_name='user',
    )
    
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_set',  # Update the related_name
        blank=True,
        help_text='Specific permissions for this user.',
        related_query_name='user',
    )

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    wallet_balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

class Product(models.Model):
    code = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()

class DiscountCode(models.Model):
    code = models.CharField(max_length=100, unique=True)
    discount_percentage = models.DecimalField(max_digits=5, decimal_places=2)
    expiration_date = models.DateField()
    used = models.BooleanField(default=False)

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    date_ordered = models.DateTimeField(auto_now_add=True)
