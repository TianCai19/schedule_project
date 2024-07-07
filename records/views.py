# records/views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import Activity
from .forms import ActivityForm

def index(request):
    activities = Activity.objects.all().order_by('-start_time')
    return render(request, 'records/index.html', {'activities': activities})

def add_activity(request):
    if request.method == 'POST':
        form = ActivityForm(request.POST)
        if form.is_valid():
            activity = form.save(commit=False)
            activity.end_time = timezone.now()
            activity.save()
            return redirect('index')
    else:
        form = ActivityForm()
    return render(request, 'records/add_activity.html', {'form': form})

def update_activity(request, pk):
    activity = get_object_or_404(Activity, pk=pk)
    if request.method == 'POST':
        form = ActivityForm(request.POST, instance=activity)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ActivityForm(instance=activity)
    return render(request, 'records/update_activity.html', {'form': form, 'activity': activity})

def delete_activity(request, pk):
    activity = get_object_or_404(Activity, pk=pk)
    if request.method == 'POST':
        activity.delete()
        return redirect('index')
    return render(request, 'records/delete_activity.html', {'activity': activity})