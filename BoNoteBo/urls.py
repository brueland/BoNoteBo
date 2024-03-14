from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", TemplateView.as_view(template_name="base.html")),
    path("admin/", admin.site.urls),
    path("profiles/", include("profiles.urls")),
    path("__reload__/", include("django_browser_reload.urls")),  # tailwind
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
