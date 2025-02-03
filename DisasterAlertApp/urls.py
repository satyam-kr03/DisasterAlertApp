from django.contrib import admin
from django.urls import path, include
from alerts import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('alerts/', include('alerts.urls')),
    path('', views.redirect_to_login),
]