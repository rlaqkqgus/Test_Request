from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic import RedirectView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("iot/", include('iot.urls')),
    path("",RedirectView.as_view(url="/iot/sec_file/", permanent=True)),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

