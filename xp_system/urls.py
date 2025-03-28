from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import XPEntryViewSet, UserProfileViewSet
from . import views  # classic views

# Router for REST API endpoints
router = DefaultRouter()
router.register(r'xp', XPEntryViewSet)
router.register(r'profiles', UserProfileViewSet)

urlpatterns = [
    # DRF API endpoints (e.g. /api/xp/, /api/profiles/)
    path('', include(router.urls)),

    # Classic Django views (for template rendering, optional)
    path('add/', views.xp_form_view, name='add_xp_entry'),
    path('xp-form/', views.xp_form_view, name='xp_form'),
    path('profile/', views.profile_view, name='profile'),
    path('leaderboard/', views.leaderboard_view, name='leaderboard'),
]
