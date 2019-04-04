from django.urls import path
from . import views
urlpatterns = [
    path('',views.user_home,name='user_home'),
    path('notification/',views.notification,name='notification'),
    path('<int:provider_id>/',views.nDetails,name='nDetails'),
    path('submited/',views.submited,name='submited'),
    path('<int:company_id>/',views.subDetail,name="subDetail"),
]
