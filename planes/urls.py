from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.urls import re_path
from django.conf.urls.static import static
from rest_framework import routers
from .views import PlanViewSet

routers = routers.DefaultRouter()
routers.register('DetallePlanes', PlanViewSet)

urlpatterns = [
    #path('', views.plan_list, name='plan_list'),
    path('plan/<int:pk>/', views.plan_venta, name='plan_venta'),
    path('plan/<int:pk>/',views.plan_contrato, name='plan_contrato'),
    
    
    
    re_path( r'^$', views.index2, name="index2"), # funcion re_path remplaza url
    re_path( r'^planes/plan_list.html/$', views.plan_list, name="plan_list"),
    re_path( r'^contacto.html/$', views.contacto, name="contacto"),
    re_path( r'^Mapa.html/$', views.Mapa, name="Mapa"),
    re_path( r'^nosotros.html/$', views.nosotros, name="nosotros"),
    re_path( r'^login.html/$', views.login, name="login"),
    re_path( r'^registrar.html/$', views.registrar, name="registrar"), 

    path('reset_password/', auth_views.PasswordResetView.as_view(template_name="planes/templates/password_reset.html"), name="reset_password"), 
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name="planes/password_reset_done.html"), name="password_reset_done"),
    path('reset/<uidb64><token>/', auth_views.PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    path('reset_password_complete/', auth_views.PasswordResetView.as_view(),name="password_reset_complete"),
    path('api/', include(routers.urls)),
]