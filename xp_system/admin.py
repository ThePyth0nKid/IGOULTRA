from django.contrib import admin
from .models import XPEntry
from django.contrib.auth import get_user_model

User = get_user_model()

@admin.register(XPEntry)
class XPEntryAdmin(admin.ModelAdmin):
    list_display = ('user', 'activity', 'xp_points', 'timestamp')
    search_fields = ('user__username', 'activity')

