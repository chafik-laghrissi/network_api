"""api URL Configuration

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
from django.urls import path, include
from rest_framework.schemas import get_schema_view
from rest_framework.documentation import include_docs_urls
from django.conf import settings
from django.conf.urls.static import static
API_TITLE = 'Network API'  # new
API_DESCRIPTION = 'A Web API for analysing traffics.'  # new
schema_view = get_schema_view(title=API_TITLE)

urlpatterns = [
    path('docs/', include_docs_urls(title=API_TITLE, description=API_DESCRIPTION)),
    path('admin/', admin.site.urls),
    path('api/', include('traffics.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('api/rest-auth/registration/', include('rest_auth.registration.urls')),
    path('schema/', schema_view)
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
