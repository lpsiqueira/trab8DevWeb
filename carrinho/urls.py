from . import views
from django.urls import path

app_name = 'carrinho'

urlpatterns = [
    path('carrinho/', views.carrinho, name='carrinho'),
]