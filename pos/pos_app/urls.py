# pos_app/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.pos, name='pos'),
    path('process_order/', views.process_order, name='process_order'),
]
