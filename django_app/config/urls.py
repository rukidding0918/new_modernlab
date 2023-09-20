from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.views.generic import TemplateView

from accounts.views import UserSignupView


urlpatterns = [
    path("", TemplateView.as_view(template_name="index.html"), name="index"),
    path("accounts/", include("django.contrib.auth.urls")),
    path("accounts/signup/", UserSignupView.as_view(), name="signup"),
    path("tang/", include("tang.urls")),
    path("admin/", admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += [
        path("__debug__/", include("debug_toolbar.urls")),
    ]
