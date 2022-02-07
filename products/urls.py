from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_products, name='products'),
    path('load-more/', views.load_more, name='load_more'),
    path('<product_id>', views.product_detail, name='product_detail'),
]