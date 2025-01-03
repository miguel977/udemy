from django.contrib import admin
from django.urls import path
from .views import homepage, about

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homepage),
    path('about', about),
]
