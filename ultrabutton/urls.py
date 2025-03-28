from django.urls import path, include
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('api/', include('xp_system.urls')),

    # Allauth URL patterns for login, logout, signup
    path('accounts/', include('allauth.urls')),

    # Your app urls
    path('xp_system/', include('xp_system.urls')),
]