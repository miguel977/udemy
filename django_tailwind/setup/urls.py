from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import home_view


urlpatterns = [
    path("", home_view, name="home"),
    path('admin/', admin.site.urls),
    
]     
urlpatterns += static(
    settings.STATIC_URL
)

