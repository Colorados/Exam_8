"""main URL Configuration

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
from django.urls import path
from reviewer.views import IndexView, ProductView, ProductEditView, \
    ProductRemoveView, ProductCreateView, ReviewListView, ReviewEditView, ReviewDetailView, ReviewDeleteView, ReviewCreateView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='index'),
    path('product/<int:pk>/', ProductView.as_view(), name='product_view'),
    path('product/<int:pk>/edit/', ProductEditView.as_view(), name='product_edit'),
    path('product/<int:pk>/remove/', ProductRemoveView.as_view(), name='product_remove'),
    path('product/add/', ProductCreateView.as_view(), name='product_add'),
    path('reviews/', ReviewListView.as_view(), name='review_list_view'),
    path('reviews/<int:pk>', ReviewDetailView.as_view(), name='review_detail'),
    path('reviews/<int:pk>/edit', ReviewEditView.as_view(), name='review_edit'),
    path('review/create/', ReviewCreateView.as_view(), name='review_create'),
    path('review/<int:pk>/delete/', ReviewDeleteView.as_view(), name='review_delete')
]
