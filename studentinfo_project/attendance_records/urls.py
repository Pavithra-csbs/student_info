from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from .views import  login_view, index_view 

app_name = 'attendance_records'


urlpatterns = [
    path('', LoginView.as_view(template_name='login.html'), name='log_in'),
    path('home/', index_view, name='index'),
    path('logout/', LogoutView.as_view(next_page="attendance_records:log_in"), name='logout'),
]                                                                  