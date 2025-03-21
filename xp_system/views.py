from django.shortcuts import render, redirect
from .forms import XPEntryForm


def add_xp_entry(request):
    if request.method == 'POST':
        form = XPEntryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = XPEntryForm()
    return render(request, 'add_xp_entry.html', {'form': form})
