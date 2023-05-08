"""vabus_backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from gestion_authentification.views import *
# from gestion_authentification import views
from django.contrib import admin
from django.urls import path, include
from vabus_backend.settings import DEBUG,MEDIA_ROOT, MEDIA_URL
from django.conf.urls.static import static 
# from django.conf.urls import url
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('api/gestionUser/', include('gestion_user.urls')),
    path('api/gestionAuthentification/', include('gestion_authentification.urls')),
    path('api/gestionAgences/', include('gestion_admin.urls')),
    path('api/gestionreservation/', include('gestion_reservation.urls')),
    # path('api', include('gestion_admin.urls')),
    path('admin/', admin.site.urls),
    # url(r'^', include('gestion_admin.urls')),
    
    path('api-auth/', include('rest_framework.urls')),
    # path('api-auth/registration/', include('rest_auth.registration.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'), 
    path('auth/', include('djoser.urls')),
    path('password_reset/', PasswordResetAPIView.as_view()),
    path('password_reset_confirm/<uidb64>/<token>/', PasswordResetConfirmAPIView.as_view()),   
]


if DEBUG:
    urlpatterns += static(MEDIA_URL, document_root = MEDIA_ROOT)
