from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from core.settings import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("main.urls"))
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns+= static(MEDIA_URL, document_root = MEDIA_ROOT)