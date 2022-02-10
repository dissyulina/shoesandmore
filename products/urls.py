from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_products, name='products'),
    path('load-more/', views.load_more, name='load_more'),
    path('<int:product_id>/', views.product_detail, name='product_detail'),
    path('add/', views.add_product, name='add_product'),
    path('edit/<int:product_id>/', views.edit_product, name='edit_product'),
]