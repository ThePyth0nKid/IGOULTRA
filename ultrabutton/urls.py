from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('xp_system/', include('xp_system.urls')),  # Deine neue App-URL
]
