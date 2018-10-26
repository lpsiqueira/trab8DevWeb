from django.urls import path
from . import views

app_name = 'appsite'

urlpatterns = [
    path('', views.teste, name='teste'),
    path('index/', views.index, name='index'),
    path('signin/', views.signIn, name='signin'),
    #path('signup/', views.signUp, name='signup'),
]