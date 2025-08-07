"""
URL configuration for DifferentTypesOfViews project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from app1.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('StringByFbv/',StringByFbv,name='StringByFbv'),
    path('StringByCbv/',StringByCbv.as_view(),name='StringByCbv'),

    
    path('HtmlByFbv/',HtmlByFbv,name='HtmlByFbv'),
    path('HtmlByCbv/',HtmlByCbv.as_view(),name='HtmlByCbv'),

    
    path('insertbyfbv/',insertbyfbv,name='insertbyfbv'),
    path('InsertByCbv/',InsertByCbv.as_view(),name='InsertByCbv'),

     
    path('HtmlbyTV/',HtmlbyTV.as_view(),name='HtmlbyTV'),
    path('RenderHtmlByTV/',TemplateView.as_view(template_name='RenderHtmlByTV.html'),name='RenderHtmlByTV'),
    path('SendDataByTV/',SendDataByTV.as_view(),name='SendDataByTV'),
]
