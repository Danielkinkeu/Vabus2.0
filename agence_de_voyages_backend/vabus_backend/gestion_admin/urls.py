from django.urls import path, include, re_path

from vabus_backend.settings import DEBUG,STATIC_ROOT,MEDIA_ROOT, MEDIA_URL, STATIC_URL
from django.conf.urls.static import static 
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
# router.register(r'agence',views.agenceView, 'task')



urlpatterns = [
    path('', include(router.urls)),
    re_path(r'^api/students/', views.students_list),
    re_path(r'^api/students/([0-9])', views.students_detail),

    path('agenceList',views.ListAgenceView.as_view(), name='agence'),
    # path('agence',views.agenceView.as_view(), name='agenceTEST'),
    path('add_agence/',views.CreateAgenceView.as_view(), name='create_agence'),
    path('<pk>/update_agence/',views.UpdateAgenceView.as_view(), name='agence_update'),
    path('<pk>/delete_agence/',views.DeleteAgenceView.as_view(), name='agence_delete'),
]
# + static(MEDIA_URL, document_root = MEDIA_ROOT)

if DEBUG:
    urlpatterns += static(MEDIA_URL, document_root = MEDIA_ROOT)




