"""Eat24x7 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path, include
from customer.views import Index ,About,Order,signin,Pricing,signup,home,Menu,MenuSearch,OrderConfirmation,OrderPayConfirmation
from django.conf.urls.static import static
from django.conf import settings

from customer import views

urlpatterns = [
    path('mail/', views.mail),
    path('admin/', admin.site.urls),
    path('restaurant/',include('restaurant.urls')),
    path('pricing/',Pricing.as_view(),name='pricing'),
    path('menu/', Menu.as_view(), name='menu'),
    path('menu/search/', MenuSearch.as_view(), name='menu-search'),
    path('',Index.as_view(),name='index'),
    path('about/',About.as_view(),name='about'),
    path('order/',Order.as_view(),name='order'),
    path('order-confirmation/<int:pk>',OrderConfirmation.as_view(),name='order-confirmation'),
    path('payment-confirmation/', OrderPayConfirmation.as_view(),name='payment-confirmation'),
    path('signin/',signin,name='signin'),
    path('signup/',signup,name='signup'),
    path('home/',home,name='home')


]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
