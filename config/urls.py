# config/urls.py
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path("", TemplateView.as_view(template_name="pages/home.html"), name="home"),
    path("about/", TemplateView.as_view(template_name="pages/about.html"), name="about"),
    path(settings.ADMIN_URL, admin.site.urls),
    path("users/", include("gab_turism.users.urls", namespace="users")),
    path("accounts/", include("allauth.urls")),
    # Your custom URLs go here
    path("api/", include("config.api_router")),
    path('api/', include('loyalty.urls')),
    # DRF auth token
    path("api/auth-token/", obtain_auth_token),
    path("api/schema/", SpectacularAPIView.as_view(), name="api-schema"),
    path("api/docs/", SpectacularSwaggerView.as_view(url_name="api-schema"), name="api-docs"),
]

if settings.DEBUG:
    from django.views import defaults as default_views
    import debug_toolbar

    urlpatterns += [
        path("400/", default_views.bad_request, kwargs={"exception": Exception("Bad Request!")}),
        path("403/", default_views.permission_denied, kwargs={"exception": Exception("Permission Denied!")}),
        path("404/", default_views.page_not_found, kwargs={"exception": Exception("Page not Found!")}),
        path("500/", default_views.server_error),
        path("__debug__/", include(debug_toolbar.urls)),
    ]
