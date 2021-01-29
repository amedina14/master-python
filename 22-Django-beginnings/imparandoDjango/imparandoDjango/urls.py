"""imparandoDjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

# Importare la mia app con le viste(controller)
# import myapp.views # Maniera consigliata quando ci sono tante app
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.inizio, name='inizio'),
    path('inizio/', views.inizio, name='inizio'),
    path('ciao-mondo/', views.ciao_mondo, name='ciao_mondo'),
    path('pagina-prova/', views.pagina, name='pagina'),
    path('pagina-prova/<int:reindirizzare>', views.pagina, name='pagina'),
    path('contatto-pag/', views.contatto, name='contatto'),
    path('contatto-pag/<str:nome>', views.contatto, name='contatto'),
    path('contatto-pag/<str:nome>/', views.contatto, name='contatto'),
    path('contatto-pag//<str:cognome>/', views.contatto, name='contatto'),
    path('contatto-pag/<str:nome>/<str:cognome>', views.contatto, name='contatto'),
    path('create-article/', views.create_article, name='create_article'),
]
