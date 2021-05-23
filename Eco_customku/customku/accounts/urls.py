from django.conf.urls import url
from . import views
from django.urls import path

app_name = 'accounts'

urlpatterns = [
    path('signup', views.signup, name='signup'),
    path('login', views.login, name='login'),
]
