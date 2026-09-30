from django.urls import path
from . import views

urlpatterns = [
    path('', views.productos, name='productos'),
    path('productos/', views.productos),
    path('editar/<int:id>/', views.editar, name='editar'),
    path('eliminar/<int:id>/', views.eliminar, name='eliminar'),
]