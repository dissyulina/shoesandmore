from django.urls import path
from . import views

urlpatterns = [
    path('<product_id>', views.product_reviews, name='product_reviews'),
]