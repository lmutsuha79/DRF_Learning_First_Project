from django.contrib import admin
from django.urls import path, include
from .views import CreateListPostsView, ManagePostView

urlpatterns = [

    path('', CreateListPostsView.as_view(), name='create_list_posts'),
    path('<int:id>/', ManagePostView.as_view(), name='manage_posts'),

]
