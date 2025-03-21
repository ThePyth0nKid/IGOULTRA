from django.shortcuts import render
from .forms import XPForm
from .models import XPEntry
from django.contrib.auth.decorators import login_required
from django.db.models import Sum

# XP form submission view
def xp_form_view(request):
    if request.method == 'POST':
        form = XPForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = XPForm()
    return render(request, 'xp_system/xp_form.html', {'form': form})

# User profile view
@login_required
def profile_view(request):
    user = request.user
    entries = XPEntry.objects.filter(user=user).order_by('-timestamp')
    total_xp = sum(entry.xp_points for entry in entries)
    level = total_xp // 1000  # Level = total XP divided by 1000

    context = {
        'user': user,
        'total_xp': total_xp,
        'level': level,
        'entries': entries[:5],  # Show latest 5 entries
    }
    return render(request, 'xp_system/profile.html', context)

# Leaderboard view
@login_required
def leaderboard_view(request):
    leaderboard = (
        XPEntry.objects
        .values('user__username')
        .annotate(total_xp=Sum('xp_points'))
        .order_by('-total_xp')[:10]
    )

    return render(request, 'xp_system/leaderboard.html', {'leaderboard': leaderboard})