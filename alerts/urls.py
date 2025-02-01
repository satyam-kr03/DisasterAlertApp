from django.urls import path
from . import views

urlpatterns = [
    path('update-location/', views.update_location, name='update_location'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('set-location/', views.set_location, name='set_location'),
    path('check-new-disasters/', views.check_new_disasters, name='check_new_disasters'),
    path('signup/', views.signup, name='signup'),  
    path('logout/', views.logout_view, name='logout')
]