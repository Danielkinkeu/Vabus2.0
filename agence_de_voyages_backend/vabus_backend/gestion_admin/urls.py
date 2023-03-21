from django.urls import path, include, re_path


from gestion_user.views import home, login, register
from .views import *
from gestion_admin import views

# import routers from the REST framework
# it is necessary for routing
from rest_framework import routers
# create a router object
router = routers.DefaultRouter()
 
# register the router
router.register(r'adminAgence',views.adminView, 'task')



urlpatterns = [
    path('', home, name="home"),
    path('login/', login, name="login"),
    path('register/', register, name="register"),
    path('index/', views.index, name="index"),
    path('upload/', views.upload, name='upload-agence'),
    path('upload/<int:gestionagence_id>', views.update),
    path('delete/<int:gestionagence_id>', views.delete),
    path('update/<int:gestionagence_id>', views.update), 
    path('index/delete/<int:gestionagence_id>', views.delete),
    path('index/update/<int:gestionagence_id>', views.update), 
    path('api/', include(router.urls)),
    
    re_path(r'^api/students/', views.students_list),
    re_path(r'^api/students/([0-9])', views.students_detail),
    

    # path(r'api/admin', views.adminView),
    # path(r'api/tutorials', views.tutorial_list),
    # path(r'api/tutorials/(?P<pk>[0-9]+)', views.tutorial_detail),
    # path(r'api/tutorials/published', views.tutorial_list_published)

]
