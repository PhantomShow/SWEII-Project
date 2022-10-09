from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'api'

urlpatterns = [
    path('', views.HomePage.as_view(), name='home_page'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login_page'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout_page'),
    path('signup/', views.SignUp.as_view(), name='signup_page'),
    path('user/<int:pk>/', views.UserDetail.as_view(), name='user_detail')
]