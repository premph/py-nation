from django.urls import path
from django.conf.urls import url

from . import views
from . import news

urlpatterns = [
    path('', views.home, name='home'),
    path('index.html/', views.home, name='home'),
    path('category.html/', views.catg, name='home'),
    path('post.html/', views.postp, name='poast'),
    path('news/', views.newsp, name='poast'),
    path('news2/', views.newsp2, name='poast'),
    path('page.html/', views.pagep, name='posat'),
    path('addpost.html/', views.upload_form, name='poslllt'),
    path('signup.html/', views.SignUpForm, name='poslllt'),
    path('news.html/', views.search, name='poast'),
    path('data.html/', views.data, name='poast'),
    path('comm/', views.comp, name='poast'),
    path('analyse/', views.analyse, name='poast'),
    
    path('comm.html/', views.Upload_comm, name='poast'),
    #path('comm, views.add_comment_to_post, name='add_comment_to_post'),
    
    path('feed/', views.feed, name='feed'),
    path('people/', views.people, name='people'),
    path('post/', views.Upload_comm, name='post'),
    #url(r'^post/form_upload.html$',
        #'views.post_form_upload', name='post_form_upload'),
    #path('upload/',views.upload)
    
    
    
    #path('upload/', views.upload, name='post_foccccrm_upload'),
    #path('upload.html/', views.upload_form, name='post_foccccrm_upload'),
    
    
     path('global/',  views.upload_form, name='jjj'),
     
     #url(r'^post/(?P<pk>\d+)/comment/$', views.add_comment_to_post, name='add_comment_to_post'),
     
    #url(r'^post/form_upload.html$',
        #views.upload, name='post_form_upload'),
    
    
]