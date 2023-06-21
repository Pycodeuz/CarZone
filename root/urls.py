from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from root import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pages.urls')),
    path('accounts/', include('accounts.urls')),
    path('cars/', include('cars.urls')),
    path('contacts/', include('contacts.urls')),
    path('socialaccounts', include('allauth.urls'))
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + \
               static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#

# + static(settings.MEDIA_URL,
#          document_root=settings.MEDIA_ROOT)
