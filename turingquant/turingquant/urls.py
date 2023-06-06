from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('risco_retorno.urls')),
    path("admin/", admin.site.urls),
]
