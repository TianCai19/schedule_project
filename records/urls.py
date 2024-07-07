# records/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add_activity, name='add_activity'),
    path('update/<int:pk>/', views.update_activity, name='update_activity'),
    path('delete/<int:pk>/', views.delete_activity, name='delete_activity'),
]