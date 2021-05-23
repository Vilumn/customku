from django.conf.urls import url, include
from django.contrib import admin
from django.urls import path
from custom import views as views_custom

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),

    path('', views_custom.home, name='home'),
]
