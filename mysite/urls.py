"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import include, path
from smallthings import views as blog_views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/',admin.site.urls),
    path('', include('smallthings.urls')),

    url(r'^post/(.*)$', blog_views.post),
   # url(r'^accounts/login/$', blog_views.login, name='login'),
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^accounts/login/$', auth_views.login, name='login'),
    
     url(r'^signup/$', blog_views.signup, name='signup'),
    
    #url(r'^accounts/logout/$', auth_views.logout, name='logout'),
    
    url(r'^accounts/logout/$', auth_views.logout, name='logout', kwargs={'next_page': '/'}),
    
    #url(r'^$', blog_views.index),
    #url(r'^admin/', admin.site.urls),
    #url(r'^home/', blog_views.home),
] 
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

