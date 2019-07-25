"""blogProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
import blog.views
import accounts.views
import portfolio.views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', blog.views.home, name='home'), # views를 import했음
    path('portfolios/', portfolio.views.portfolio, name='portfolio'),
    path('<int:blog_id>/', blog.views.detail, name='detail'),
    path('new/', blog.views.new, name='new'),
    path('create/', blog.views.create, name='create'),
    path('signup/', accounts.views.signup, name='signup'),
    path('login/', accounts.views.login, name='login'),
    path('logout/', accounts.views.logout, name='logout'),
    path('newblog/', blog.views.blogpost, name='newblog'),
    
    #path('blog/', include('blog.urls')),
    #path('portfolio/', include('portfolio.urls')),
    #path('accounts/', include('accounts.urls')),

    #import blog.views
    #path('', blog.views.home, name='home') # blog.views를 import했으면

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# 올린 이미지를 읽어오기 위한 코드


#urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
