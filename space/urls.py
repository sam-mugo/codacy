from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('tuts/', views.tuts, name='tuts'), 
    path('tut-list/', views.TutorialListAPIView.as_view(), name='tut-list'),
    
]