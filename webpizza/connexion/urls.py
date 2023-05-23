
from django.urls import path, include
from django.contrib.auth import views as auth_views
from connexion import views

urlpatterns = [
    path('logout', auth_views.LogoutView.as_view(template_name='connexion/logout.html'), name='logout'),
    path(
        'login', auth_views.LoginView.as_view(template_name='connexion/login.html'), name='login'),
]