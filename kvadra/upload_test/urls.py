"""site_smyt URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url
from . import views

app_name = 'upload_test'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^text_save_view/$', views.text_save_view, name='text_save_view'),
    url(r'^text_save/$', views.text_save, name='text_save'),
    url(r'^get_text_list/$', views.get_text_list, name='get_text_list'),

]
