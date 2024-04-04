from django.urls import path
from . import views

urlpatterns = [
    path('auth/login',views.login_user),
    path('auth/register',views.register),
    path("auth/register-utilisateur",views.registerUtilisateur),
    path('auth/verification-email', views.send_verification_email),
    path('auth/verify-email', views.verify_email),
    path("auth/reset-password-email", views.send_reset_password_email),
    path("auth/reset-password", views.reset_password),
    path('auth/logout',views.logout_user,name='logout'),
    path("", views.default),
]