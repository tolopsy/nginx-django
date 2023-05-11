from django.views.generic import TemplateView
from django.views import debug
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ping/', TemplateView.as_view(template_name="ping.html")),
    path('secure/', TemplateView.as_view(template_name="secure.html")),
    path('', debug.default_urlconf),
]
