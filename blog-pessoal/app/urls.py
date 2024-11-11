from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.home, name='home'),
    path('novo_post/', views.novo_post, name='novo_post'),
]

