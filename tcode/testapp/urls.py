from django.urls import path
from . import views

urlpatterns  = [
    path('',views.join, name='join'),
    path('',views.join_result, name='join_result'),
    path('',views.translate, name='translate'),
    path('',views.translate_result, name='translate_result')
    path('',views.selecttest, name='selecttest'),
    path('',views.selecttest_result, name='selecttest_result'),
    path('',views.main, name='main'),
    path('',views.radiotest, name='radiotest'),
    path('',views.login, name='login'),
    path('',views.login_success, name='login_success'),
    path('',views.logout, name='logout'),
]

