from django.conf.urls import url
from django.urls import path, re_path
from . import views
from .views import HomeView, ArticleDetailView, AddPostView, UpdatePostView, DeletePostView
from members.views import UserRegisterView, UserEditView


from .views import *


urlpatterns = [

    path('', views.index, name='index'),
    path('resources/', views.resources, name='resources'),
    path('trending/', views.trending, name='trending'),
    # path('',HomeView.as_view(),name='home')
    #re_path('article/(?P<pk>\d+)$', ArticleDetailView.as_view(),name='article-detail'),
    path('add_post/', AddPostView.as_view(), name='add_post'),
    path('register/', UserRegisterView.as_view(), name='register'),
    path('edit_profile/', UserEditView.as_view(), name='edit_profile')
    #re_path('article/edit/(?P<pk>\d+)$', UpdatePostView.as_view(),name='update_post'),
    #re_path('article/delete/(?P<pk>\d+)$', DeletePostView.as_view(),name='delete_post'),



]
