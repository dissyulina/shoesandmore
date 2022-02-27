from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_articles, name='all_articles'),
    path('<blog_id>', views.article_detail, name='article_detail'),
]
