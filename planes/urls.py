from django.urls import path
from . import views

urlpatterns = [
    path('', views.plan_list, name='plan_list'),
    path('plan/<int:pk>/', views.plan_venta, name='plan_venta'),
    path('plan/<int:pk>/',views.plan_contrato, name='plan_contrato'),
]