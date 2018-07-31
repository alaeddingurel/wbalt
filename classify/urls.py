"""annoAPI URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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

from . import views
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('', views.index),
    path('<int:text_id>', views.detail),
    path('register/', views.UserFormView.as_view(), name='register'),
    path('filtered/', views.filtered, name='filtered'),
    path('agreed/', views.agreed, name='agreed'),
    path('nonagreed/', views.nonagreed, name='nonagreed'),
    path('tagged/', views.tagged, name='tagged'),
    path('<int:text_id>/changeprotest/', views.protest, name='changeprotest'),
    path('<int:text_id>/changenonprotest/', views.nonprotest, name='changenonprotest')

]
