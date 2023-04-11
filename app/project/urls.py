from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from django.urls import path, include
from django.contrib import admin


# urlpatterns = [
#     url(r'api/v1/', include(('users.urls', 'users'), namespace='users')),
#     url(r'api/v1/', include(('hotels.urls', 'hotels'), namespace='hotels')),
# ]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include(('users.urls', 'users'), namespace='users')),
    path('hotels/', include(('hotels.urls', 'hotels'), namespace='hotels')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)