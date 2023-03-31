from django.urls import path, include, re_path


from gestion_user.views import *
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
    path('api/', include(router.urls)),
    re_path(r'^api/students/', views.students_list),
    re_path(r'^api/students/([0-9])', views.students_detail),

    path('agenceList',views.ListAgenceView.as_view(), name='agence'),
    path('add_agence/',views.CreateAgenceView.as_view(), name='create_agence'),
    path('<pk>/update_agence/',views.UpdateAgenceView.as_view(), name='agence_update'),
    path('<pk>/delete_agence/',views.DeleteAgenceView.as_view(), name='agence_delete'),

]
