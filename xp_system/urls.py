from django.urls import path
from . import views

urlpatterns = [
    path('xp-form/', views.xp_form_view, name='xp_form'),
    path('profile/', views.profile_view, name='profile'),
]
