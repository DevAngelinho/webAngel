from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import handler404, handler500

urlpatterns = [
    path('', views.home, name='home'),
    path('index/', views.index, name='index'),
    path('interfaz/', views.interfaz, name='interfaz'), 
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)

# Configuración de vistas personalizadas para errores 404 y 500
handler404 = 'nucleoangel.views.error_404_view'
handler500 = 'nucleoangel.views.error_500_view'
