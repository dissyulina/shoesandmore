from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_favorites, name='view_favorites'),
    path('add_to_favorites/<item_id>/', views.add_to_favorites,
         name='add_to_favorites'),
    path('remove_from_favorites/<item_id>/', views.remove_from_favorites,
         name='remove_from_favorites'),
]
