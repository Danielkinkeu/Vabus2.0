from django.urls import path
from gestion_authentification.views import *
from gestion_authentification import views

urlpatterns = [
    path('login',views.LoginView.as_view(), name='login'),   
    path('register',views.RegistrationView.as_view(), name='register'),      
    path('password_reset/', PasswordResetAPIView.as_view()),
    path('password_reset_confirm/<uidb64>/<token>/', PasswordResetConfirmAPIView.as_view()),    
]