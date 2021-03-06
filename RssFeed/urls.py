from django.conf.urls import url
from django.urls import path, re_path
from . import views
from .views import HomeView ,  ArticleDetailView, AddPostView, UpdatePostView, DeletePostView , TelegramADV ,TwitterADV , DiscordADV , YoutubeADV
from members.views import UserRegisterView, UserEditView


from .views import *


urlpatterns = [

    path('', views.index, name='index'),
    #path('trending/', HomeView.as_view(), name='trending'),
    path('resources/', views.resources, name='resources'),
    path('trending/', views.trending, name='trending'),
    
    #path('trending/',HomeView.as_view(),name='home'),
    path ('article/(?P<pk>\d+)$',ArticleDetailView.as_view(), name='article-detail'),
    #path('<int:article_id>/$',ArticleDetailView.as_view(), name='article-detail'),
    re_path('article/(?P<pk>\d+)$', TelegramADV.as_view(),name='telegram-detail'),
    re_path('article/(?P<pk>\d+)$', TwitterADV.as_view(),name='twitter-detail'),
    re_path('article/(?P<pk>\d+)$', DiscordADV.as_view(),name='discord-detail'),
    re_path('article/(?P<pk>\d+)$', YoutubeADV.as_view(),name='youtube-detail'),
    #path('trending/', AddPostView.as_view(), name='add_post'),
    #path('add_post/', AddPostView.as_view(), name='add_post'),
    #path('register/', views.registeration, name='registeration'),
    path('register/', UserRegisterView.as_view(), name='register'),
    path('login/', views.login, name='index'),
    #path('logout/', HomeView.as_view(), name='index'),
    path('logout/', views.index, name='index'),
    
    path('show/', views.telegramShow, name='telegramShow'),
    path('edit_profile/', UserEditView.as_view(), name='edit_profile')
    #re_path('article/edit/(?P<pk>\d+)$', UpdatePostView.as_view(),name='update_post'),
    #re_path('article/delete/(?P<pk>\d+)$', DeletePostView.as_view(),name='delete_post'),



]
