
from django.urls import path
from . import views

app_name = 'attendance_records'


urlpatterns = [
    path('', views.login_view, name='login'),
    path('index/', views.index_view, name='index'),
    path('logout/', views.logout_view, name='logout'),
    
]                                                                  