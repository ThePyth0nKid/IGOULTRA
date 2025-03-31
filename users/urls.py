from django.urls import path
from .views import ProfileView, RegisterView

urlpatterns = [
    # User registration endpoint
    path('register/', RegisterView.as_view(), name='register'),

    # Authenticated user profile endpoint (GET & PUT)
    path('me/', ProfileView.as_view(), name='profile'),
]
