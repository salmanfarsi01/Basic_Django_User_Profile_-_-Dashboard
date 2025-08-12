"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
# core/urls.py

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic.base import RedirectView # <--- IMPORT THIS

urlpatterns = [
    # This is the new line you are adding.
    # It makes the root URL redirect to the login page.
    path('', RedirectView.as_view(url='login/', permanent=False), name='index'),

    # Your existing URLs
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('', include('django.contrib.auth.urls')), # This already provides the /login/ URL
]

# This part remains the same
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)