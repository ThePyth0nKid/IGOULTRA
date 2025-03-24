from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.xp_form_view, name='add_xp_entry'),
    path('xp-form/', views.xp_form_view, name='xp_form'),
    path('profile/', views.profile_view, name='profile'),
    path('leaderboard/', views.leaderboard_view, name='leaderboard'),
]
