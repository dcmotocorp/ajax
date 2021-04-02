"""myproject URL Configuration

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
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('customer/', views.customer, name='customer'),
    path('add-customer/', views.add_customer, name='add-customer'),
    path('product/', views.product, name='product'),
    path('add-product/',views.add_product,name="add-product"),
    path('get-price/',views.get_price,name="get-price"),
    path('get-total/',views.get_total,name="get-total"),
    path('add-order/',views.add_order,name="add-order"),
    path("order/",views.order,name="order"),
    path("del-order/<int:pk>",views.del_order,name="del-order"),
    path("update-order/<int:uk>", views.update_order, name="update-order"),
    path("update-data/", views.update_data, name="update-data"),

    path("search-value/", views.search_value, name="search-value"),
]

