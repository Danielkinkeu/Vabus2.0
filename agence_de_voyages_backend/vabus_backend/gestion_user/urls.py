from django import views
from django.urls import path,include
from vabus_backend.settings import DEBUG,STATIC_ROOT,MEDIA_ROOT, MEDIA_URL, STATIC_URL
from django.conf.urls.static import static  
from gestion_admin.views import update, delete
from .views import *
from . import views 

# import routers from the REST framework
# it is necessary for routing
from rest_framework import routers
# create a router object
router = routers.DefaultRouter()
 
# register the router
router.register(r'tasks',views.userView, 'task')


urlpatterns = [
    path('', home, name="home"),
    path('login/', login, name="login"),
    path('register/', register, name="register"),
    path('propos/',propos, name="propos"),
    # path('reservation/liste/',liste, name="liste"),    
    path('reservations/', reservations, name="reservations"),
    path('visiter/', visiter, name="visiter"),
    path('visiter/reservations', reservations, name="reservations"),
    path('upload/', views.upload, name='upload-agence'),
    path('index/upload/', views.upload, name='upload-agence'),
    path('upload/<int:gestionagence_id>', update),
    path('delete/<int:gestionagence_id>', delete),
    path('update/<int:gestionagence_id>', update), 
    path('api/', include(router.urls)),

]  

if DEBUG:
    urlpatterns += static(STATIC_URL, document_root = STATIC_ROOT)
    urlpatterns += static(MEDIA_URL, document_root = MEDIA_ROOT)
