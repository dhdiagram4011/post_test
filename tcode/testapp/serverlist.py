from django.urls import path
from . import views

urlpatterns = [
    path('',views.serverlist, name='serverlist')

]