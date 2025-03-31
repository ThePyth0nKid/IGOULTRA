from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    # 🔐 Admin
    path('admin/', admin.site.urls),

    # 🔥 Auth (JWT)
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # 👤 User (Custom User Routes)
    path('api/users/', include('users.urls')),

    # 📊 XP System
    path('api/xp/', include('xp_system.urls')),

    # 🌐 Allauth (OAuth, Discord etc.)
    path('accounts/', include('allauth.urls')),
]
