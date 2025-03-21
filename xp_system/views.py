from django.shortcuts import render
from .forms import XPForm


def xp_form_view(request):
    if request.method == 'POST':
        form = XPForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = XPForm()
    return render(request, 'xp_system/xp_form.html', {'form': form})
