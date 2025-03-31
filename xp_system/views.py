from django.shortcuts import render
from .forms import XPForm
from .models import XPEntry, UserProfile
from django.contrib.auth.decorators import login_required
from django.db.models import Sum
# === REST API ViewSets ===
from rest_framework import viewsets
from .serializers import XPEntrySerializer, UserProfileSerializer


# XP form submission view
def xp_form_view(request):
    if request.method == 'POST':
        form = XPForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = XPForm()
    return render(request, 'xp_system/xp_form.html', {'form': form})

# User profile view with XP and level calculation
@login_required
def profile_view(request):
    user = request.user
    entries = XPEntry.objects.filter(user=user).order_by('-timestamp')
    total_xp = sum(entry.amount for entry in entries)  # total XP from all entries
    level = total_xp // 1000  # simple level system: 1 level per 1000 XP

    context = {
        'user': user,
        'total_xp': total_xp,
        'level': level,
        'entries': entries[:5],  # show latest 5 entries
    }
    return render(request, 'xp_system/profile.html', context)

# Leaderboard view showing top 10 users by total XP
@login_required
def leaderboard_view(request):
    leaderboard = (
        XPEntry.objects
        .values('user__username')
        .annotate(total_xp=Sum('amount'))  # total XP per user
        .order_by('-total_xp')[:10]
    )
    return render(request, 'xp_system/leaderboard.html', {'leaderboard': leaderboard})


# API endpoint for XPEntry model
class XPEntryViewSet(viewsets.ModelViewSet):
    queryset = XPEntry.objects.all().order_by('-timestamp')
    serializer_class = XPEntrySerializer


# API endpoint for UserProfile model
class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
