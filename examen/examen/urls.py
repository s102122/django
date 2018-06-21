from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url('admin', admin.site.urls),
    url('datechecker', include('datechecker.urls')),
]