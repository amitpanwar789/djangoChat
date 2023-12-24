from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('core.urls')),
    path('rooms/', include(('room.urls', 'room'), namespace='room')),
    path('admin/', admin.site.urls),
]
