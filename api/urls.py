from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from . import views

app_name = 'api'

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login_page'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout_page'),
    path('signup/', views.SignUp.as_view(), name='signup_page'),
    path('user/<int:pk>/', views.UserDetail.as_view(), name='user_detail_page'),
    path('user/<int:pk>/update', views.UpdateUser.as_view(), name='update_user_page'),
    path('user/<int:pk>/delete_post', views.DeletePost.as_view(), name='delete_post_page'),
    path('search/', views.search_results, name='search_results'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # Used to show images