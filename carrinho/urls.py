from . import views
from django.urls import path

app_name = 'carrinho'

urlpatterns = [
    path('', views.carrinho, name='carrinho'),
]