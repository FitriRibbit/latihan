"""myapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import include, path

from page.views import homepage_view, contact_view, about_view, baseview, navbar_view
#from product.views import (product_detail_view, product_create_view, render_initial_data, dynamic_lookup_view)
#from product.views import dynamic_lookup_view,product_delete_view, product_list_view, product_create_view, product_update_view

urlpatterns = [
    path('course/', include('course.urls')),
    path('blog/', include('blog.urls')),
    path('product/', include('product.urls')),
    path('', homepage_view, name='home'),
    path('contact/', contact_view),
    path('about/<int:id>/', about_view, name='product-detail'),
    #path('base/', baseview),
    #path('navbar/', navbar_view),
    #path('create/', product_create_view, name='product-list'),
    #path('product/', product_detail_view),
    path('admin/', admin.site.urls),
 #   path('product/<int:id>/' , dynamic_lookup_view, name='product-detail'),
    #path('product/<int:id>/update/', product_update_view, name='product-update'),
    #path('product/<int:id>/delete/', product_delete_view, name='product-delete'),
    #path('product/', product_list_view, name='product-list'),
]

