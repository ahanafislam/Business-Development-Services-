from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('signup/',views.signup,name='signup'),
    path('companyDetails/',views.companyDetails,name='companyDetails'),
    path('logout/',views.logout,name='logout'),
]
