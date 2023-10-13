from django.db import models
from datetime import date
from django.urls import reverse
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

class CustomUser(AbstractUser):
    phone = models.CharField(max_length=15)

    def get_user_orders(self): #trả về các đơn hàng của người dùng cụ thể
        return self.order_set.all()

class Category(models.Model):
    name = models.CharField(max_length=50)
    parent = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, help_text=_("Parent category of this category (if any)."))

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='product_images/', null=True, blank=True, help_text=_("Product image"))
    description = models.CharField(max_length=255, help_text=_("Brief description of the product."))
    base_price = models.DecimalField(max_digits=12, decimal_places=3, help_text=_("The origin price of the product."))
    number_in_stock = models.IntegerField(default=0, help_text=_("Quantity of the product available in stock."))
    sold_number = models.IntegerField(default=0, help_text=_("Number of products sold."))
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def is_available(self):
        return self.number_in_stock > 0

    def get_stock_count(self):
        return self.number_in_stock

class Order(models.Model):
    order_date = models.DateField(default=date.today, help_text=_("Date of the order."))
    customer = models.CharField(max_length=255, null=True, help_text=_("Brief description of the product."))
    ORDER_STATUS = (
        (0, 'Pending'),
        (1, 'Ongoing'),
        (2, 'Cancelled'),
        (3, 'Rejected'),
        (4, 'Done'),
    )
    status = models.IntegerField(choices=ORDER_STATUS, default=0, help_text=_("Status of the order."))
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    cart = models.ForeignKey('Cart', on_delete=models.CASCADE)
    total_cost = models.DecimalField(max_digits=12, decimal_places=3, default=0, help_text=_("total cost of order."))

class OrderDetail(models.Model):
    price = models.DecimalField(max_digits=12, decimal_places=3, default=0, help_text=_("Price of product at order."))
    quantity = models.IntegerField(default=0, help_text=_("total quantity of products ordered."))
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    cost = models.DecimalField(max_digits=12, decimal_places=3, default=0, help_text=_("cost of each product."))

class Cart(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

class CartItem(models.Model):
    quantity = models.IntegerField(default=0, help_text=_("Quantity of each product in the cart."))
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
