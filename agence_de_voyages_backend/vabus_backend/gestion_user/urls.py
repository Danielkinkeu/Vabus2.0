from django import views
from django.urls import path,include
from vabus_backend.settings import DEBUG,STATIC_ROOT,MEDIA_ROOT, MEDIA_URL, STATIC_URL
from django.conf.urls.static import static  
from gestion_admin.views import *
from .views import *
from . import views 

# import routers from the REST framework
# it is necessary for routing
from rest_framework import routers
# create a router object
router = routers.DefaultRouter()
 
# register the router
router.register(r'user',views.userView, 'task')


urlpatterns = [
    path('', include(router.urls)),
    path('userList',views.ListUserView.as_view(), name='user'),
    path('add_user/',views.CreateUserView.as_view(), name='create_user'),
    path('<pk>/update_user/',views.UpdateUserView.as_view(), name='user_update'),
    path('<pk>/delete_user/',views.DeleteUserView.as_view(), name='user_delete'),  
     

]  

if DEBUG:
    urlpatterns += static(STATIC_URL, document_root = STATIC_ROOT)
    urlpatterns += static(MEDIA_URL, document_root = MEDIA_ROOT)

