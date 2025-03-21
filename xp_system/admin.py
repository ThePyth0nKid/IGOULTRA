from django.contrib import admin
from .models import XPEntry


@admin.register(XPEntry)
class XPEntryAdmin(admin.ModelAdmin):
    list_display = ('user', 'activity', 'xp_points', 'timestamp')
    search_fields = ('user__username', 'activity')
