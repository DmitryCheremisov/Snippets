"""Snippets URL Configuration

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
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin

from MainApp import views

urlpatterns = [
    path('', views.index_page, name="main_page"),
    path('admin/', admin.site.urls),
    path('snippet/add', views.add_snippet_page, name="snippet_add"),
    path('snippets/list', views.snippets_page, name="snippet_view"),
    path('snippets/filter', views.snippets_filter),
    path('snippet/<int:snippet_id>', views.snippet, name="snippet"),
    path('edit/<int:snippet_id>', views.edit, name="sn_edit"),
    path('snippet/delete/<int:sn_id>', views.sn_delete, name="sn_delete"),
    path('comment/add', views.comment_add, name="comment_add"),
    path('thanks/', views.thanks),
    path('search/', views.search),
    path('auth/', views.login),
    path('login/', views.login_page),
    path('logout/', views.logout),
    #path('snippet/add_form/', views.add_form),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

