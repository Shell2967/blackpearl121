"""
URL configuration for blackpearl project.

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
from django.contrib import admin
from django.urls import path
from django.contrib import admin
from django.urls import path
from test_site import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index_page),

    path('', views.contacts_page),
    path('contacts/', views.contacts_page),

    path('', views.menu_page),
    path('menu/', views.menu_page),

    path('', views.navigate_page),
    path('navigate/', views.navigate_page),

    path('', views.photo_page),
    path('photo/', views.photo_page),

    path('', views.reviews_page),
    path('reviews/', views.reviews_page),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)