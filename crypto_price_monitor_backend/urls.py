"""
URL configuration for crypto_price_monitor_backend project.

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
from crypto_monitor_backend import views
from authentication.views import UserCreateAPIView, sign_in

urlpatterns = [
    path('admin/', admin.site.urls),
    path('log-access/', views.log_access, name='log_access'),
    path('notify-price-change/', views.notify_price_change,
         name='notify_price_change'),
    path('api/users/sign-up', UserCreateAPIView.as_view(), name='user-create'),
    path('api/users/sign-in', sign_in, name='sign-in'),

]
