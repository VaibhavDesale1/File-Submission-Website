from django.contrib import admin
from django.urls import path
from meapp.views import home, create, delete
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", home, name="home"),
    path("create/", create, name="create"),
    path("delete/<int:id>", delete, name="delete"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
