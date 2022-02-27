from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('Tuts/', views.code, name='code'),
    
]