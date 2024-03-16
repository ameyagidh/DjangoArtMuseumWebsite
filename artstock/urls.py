from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static


admin.site.site_header = "ARTSTOCK Admin"
admin.site.site_title = "ArtStock Admin Portal"
admin.site.index_title = "Welcome to Artstock Portal"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('stock.urls')),
]

if settings.DEBUG:
    urlpatterns +=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns +=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)