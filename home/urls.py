from django.urls import path
from .views import HomeView
from . import views

app_name = 'home'

urlpatterns = [
    path('', views.CategoryView.as_view(), name='category'),
    path('home/', views.HomeView.as_view(), name='home'),
    path('category/',views.CategoryView.as_view(), name='category'),
] 
