from django.urls import path
from .views import add_xp_entry

urlpatterns = [
    path('add/', add_xp_entry, name='add_xp_entry'),
]
