from django.contrib import admin
from django.urls import include, path
from django.conf import settings
import debug_toolbar

admin.site.site_header = "Storefront Admin"
admin.site.index_title = "Admin"

urlpatterns = [
    path("admin/", admin.site.urls),
    path("store/", include("store.urls")),
    path("worktracker/", include("worktracker.urls")),
]

if settings.DEBUG:
    urlpatterns += [
        path("__debug__/", include(debug_toolbar.urls)),
    ]
