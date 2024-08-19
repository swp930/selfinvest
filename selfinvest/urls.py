"""selfinvest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.conf import settings
from django.contrib import admin
from django.urls import path, re_path, include
from . import views
from client.views import serve_react_static, serve_react_index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.page.as_view(), name='index'),
    path('', include('api.urls')),
    path('reacts/', serve_react_index, {"document_root": settings.REACT_APP_BUILD_PATH}),
    #path('home', views.page.as_view(), name='index') # will be at /home
    re_path(r"^(?P<path>.*)$", serve_react_static, {"document_root": settings.REACT_APP_BUILD_PATH}),
]
