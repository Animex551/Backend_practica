
from django.contrib import admin
from django.urls import path, include
from core.urls import core_urlpatterns

urlpatterns = [
    path("",include(core_urlpatterns)),
    path("admin/", admin.site.urls),
    path("accounts/",include("django.contrib.auth.urls") ),
    path("accounts/",include("registration.urls") ),
    
]
