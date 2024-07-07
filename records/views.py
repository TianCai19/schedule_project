# records/views.py
from django.shortcuts import render, redirect
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