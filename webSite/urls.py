"""
URL configuration for webSite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from webApp.views import create_tag, delete_tag, home, data_ordering, update_data_tags

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home, name="home"),
    path("create_tag/", create_tag),
    path("delete_tag/", delete_tag),
    path("data_ordering/", data_ordering),
    path("update_data_tags/", update_data_tags),
]
