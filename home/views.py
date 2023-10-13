from django.shortcuts import render
from django.views import View, generic
from django.views import View
from .models import Category, Product, Cart, CartItem, CustomUser, Order, OrderDetail

class HomeView(View):
    def get(self, request):
        return render(request, 'homepage/index.html')

class CategoryView(generic.DetailView):
    model = Category

    def get(self, request):
        menu = Category.objects.all()
        products = Product.objects.all().order_by('name')
        products_array = []
        for product in products:
                products_array.append({'product': product})
        return render(request, 'catalog/menu.html', {'menu': menu, 'products': products, 'products_array': products_array})
