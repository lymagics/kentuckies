from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('room/', include('rooms.urls')),
    path('member/', include('members.urls')),
    path('', include('pages.urls')),
]
