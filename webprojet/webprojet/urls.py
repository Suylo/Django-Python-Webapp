"""
URL configuration for webprojet project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from appliprojet import views
from django.urls import path, include
from django.conf.urls.static import static
from webprojet import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('jeux/', views.jeux),
    path('jeux/<int:id_jeux>', views.jeux_details),
    path('categories/', views.categories),
    path('categories/<int:id_categorie>/jeux', views.categories_jeux),
    path('', views.all),
    path('', include('connexion.urls')),
    path('panier/', views.panier, name='panier'),
    path('ajouter-au-panier/<int:jeux_id>/', views.ajouter_au_panier, name='ajouter_au_panier'),
    path('supprimer-du-panier/<int:ligne_panier_id>/', views.supprimer_du_panier, name='supprimer_du_panier'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
