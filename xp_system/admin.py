from django.contrib import admin
from .models import XPEntry, UserProfile
from django.contrib.auth import get_user_model

User = get_user_model()

@admin.register(XPEntry)
class XPEntryAdmin(admin.ModelAdmin):
    list_display = ('user', 'category', 'amount', 'timestamp')  # updated field names
    search_fields = ('user__username', 'category')  # updated from 'activity'

# Register UserProfile model for admin view
@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'xp', 'level', 'rank')
    search_fields = ('user__username', 'rank')
