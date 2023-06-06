
from django.urls import path, include
from django.contrib.auth import views as auth_views
from connexion import views

urlpatterns = [
    path('logout', auth_views.LogoutView.as_view(template_name='connexion/logout.html'), name='logout'),
    path('login', auth_views.LoginView.as_view(template_name='connexion/login.html'), name='login'),
    path('register/', views.register, name='register'),
    path('password_reset/',
         auth_views.PasswordResetView.as_view(
             template_name='connexion/password_reset.html',
             email_template_name='connexion/password_reset_email.html'),
         name='password_reset'),
    path('reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
             template_name='connexion/password_reset_confirm.html'),
         name='password_reset_confirm'),
    path('password_reset/done/',
         auth_views.PasswordResetDoneView.as_view(
             template_name='connexion/password_reset_done.html'),
         name='password_reset_done'),
    path('reset/done/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name='connexion/password_reset_complete.html'),
         name='password_reset_complete'),
]