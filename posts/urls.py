from django.contrib import admin
from django.urls import path, include
from .views import posts_listing, create_post, post_detail, update_post, delete_post

urlpatterns = [
    path('', posts_listing, name='posts_listing'),
    path('<int:pid>/', post_detail, name='post_detail'),
    path('create/', create_post, name='create_post'),
    path('<int:pid>/update/', update_post, name='update_post'),
    path('<int:pid>/delete/', delete_post, name='delete_post'),

]
