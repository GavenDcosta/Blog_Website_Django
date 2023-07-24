from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('postblog', views.postblog, name='postblog'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('post/<str:post>', views.post, name='post'), 
]
