from django.urls import path
from . import views

urlpatterns = [
    path('xp-form/', views.xp_form_view, name='xp_form'),
]
