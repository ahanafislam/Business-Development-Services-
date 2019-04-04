from django.urls import path
from . import views

urlpatterns = [
    path('',views.svProvider_home,name='svProvider_home'),
    path('<int:company_id>/',views.svDetails,name='svDetails'),
]
