"""
URL configuration for BasicProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from hotelproject.views import details, read_details, create_hotels, update_details, delete_estate

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', details),
    path('moreInfo/<pk>/edit/', update_details),
    path('moreInfo/<pk>/', read_details),
path('moreInfo/<pk>/delete/', delete_estate),
    path('add-estate/', create_hotels),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)