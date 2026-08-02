from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('dashboard/', admin.site.urls),
    path('tinymce/', include('tinymce.urls')),
    path('', include('apps.core.urls')),
    path('products/', include('apps.products.urls')),
    path('services/', include('apps.services.urls')),
    path('registration/', include('apps.registration.urls')),
    path('contact/', include('apps.contact.urls')),
]





if settings.DEBUG:
    urlpatterns += [
        path("__reload__/", include("django_browser_reload.urls")),
    ]
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
