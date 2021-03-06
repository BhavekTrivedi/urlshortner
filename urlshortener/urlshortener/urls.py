"""urlshortener URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
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
from shortener.views import  URLRedirectView, test_view, HomeView #  Redirect_FB_View,

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^about123$', test_view),
    url(r'^$',HomeView.as_view()),
    url(r'^(?P<shortcode>[\w-]+)/$', URLRedirectView.as_view(), name='scode'),
    #  url(r'^(?P<shortcode>[\w-]+){6,15}/$', Redirect_FB_View),
    #  url(r'^(?P<shortcode>[\w-]+)/$', Redirect_FB_View),
]
