from django.contrib import admin
from django.urls import path
from post import views


urlpatterns = [

path('create/', views.post_create, name = 'create'),
path('list/', views.post_list, name = 'list'),
path('detail/<int:post_id>/', views.post_detail, name = 'detail'),
path('update/<int:post_id>/', views.post_update, name = 'update'),
path('delete/<int:post_id>/', views.post_delete, name = 'delete'),
path('user_signup/', views.user_signup, name = "usersignup"),
path('user_logout/', views.user_logout, name = "userlogout"),
path('user_login/', views.user_login, name = "userlogin"),
path('likes/<int:post_id>/', views.likes, name = 'likes'),
]