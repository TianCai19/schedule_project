当然，下面是一个详细的 README 文档，介绍该项目以及一些基本的 Django 知识和命令。

---

# Schedule Recording and Visualization System

## Overview

This is a Django-based system for recording and visualizing your schedule. Users can record activities at any time, and the system will calculate the time spent on each activity by subtracting the end time of the previous record. Different colors represent different types of activities for better visualization. Each small square in the visualization grid represents 30 minutes.

## Features

- Record activities with start and end times.
- Calculate the duration of each activity.
- Visualize activities with different colors.
- Categories include:
  - Important Study (重要学习)
  - Important Work (重要工作)
  - Exercise (锻炼)
  - Daily Life (日常生活)
  - Rest (休息)
  - Entertainment (娱乐)

## Project Structure

```
schedule_project/
    manage.py
    schedule_project/
        __init__.py
        settings.py
        urls.py
        wsgi.py
    records/
        __init__.py
        admin.py
        apps.py
        forms.py
        models.py
        tests.py
        urls.py
        views.py
        templates/
            records/
                index.html
                add_activity.html
    db.sqlite3
```

## Prerequisites

- Python 3.6 or higher
- Django 3.0 or higher

## Installation

1. **Clone the repository**:

   ```bash
   git clone <repository_url>
   cd schedule_project
   ```

2. **Create a virtual environment and activate it**:

   ```bash
   python3 -m venv env
   source env/bin/activate  # On Windows use `env\Scripts\activate`
   ```

3. **Install dependencies**:

   ```bash
   pip install django
   ```

4. **Apply migrations**:

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Run the development server**:

   ```bash
   python manage.py runserver
   ```

6. **Open your browser and navigate to** `http://127.0.0.1:8000/`.

## Usage

### Adding an Activity

1. Navigate to `http://127.0.0.1:8000/add/`.
2. Fill out the form with the activity details:
   - Name
   - Start Time
   - Activity Type
3. Click the "Add Activity" button.
4. The activity will be recorded, and the end time will be set to the current time.

### Viewing the Schedule

1. Navigate to `http://127.0.0.1:8000/`.
2. The schedule will display all recorded activities with their respective colors.

## Django Basics

### Key Concepts

- **Project**: A Django project is a collection of settings for an instance of Django, including database configuration, Django-specific options, and application-specific settings.
- **App**: A Django app is a web application that does something — e.g., a blog system, a database of public records, or a simple poll app.

### Key Files

- `manage.py`: A command-line utility that lets you interact with this Django project in various ways.
- `settings.py`: Contains all the settings/configuration for your Django project.
- `urls.py`: Contains URL declarations for your Django project.
- `models.py`: Contains the data models of your application.
- `views.py`: Contains the functions/classes that handle the requests and return responses.
- `forms.py`: Contains the forms for your application.

### Common Commands

- **Start a new project**:
  ```bash
  django-admin startproject projectname
  ```
- **Start a new app**:
  ```bash
  python manage.py startapp appname
  ```
- **Create migrations**:
  ```bash
  python manage.py makemigrations
  ```
- **Apply migrations**:
  ```bash
  python manage.py migrate
  ```
- **Run the development server**:
  ```bash
  python manage.py runserver
  ```

### Templates

Templates in Django are used to generate HTML dynamically. The templates for this project are located in `records/templates/records/`.

### Models

Models define the structure of the database. Here's the model used in this project:

```python
from django.db import models
from django.utils import timezone

class Activity(models.Model):
    ACTIVITY_TYPE_CHOICES = [
        ('study', '重要学习'),
        ('work', '重要工作'),
        ('exercise', '锻炼'),
        ('life', '日常生活'),
        ('rest', '休息'),
        ('entertainment', '娱乐'),
    ]

    COLOR_CHOICES = {
        'study': '#FF6347',        # Tomato
        'work': '#4682B4',         # SteelBlue
        'exercise': '#32CD32',     # LimeGreen
        'life': '#FFD700',         # Gold
        'rest': '#8A2BE2',         # BlueViolet
        'entertainment': '#FF69B4' # HotPink
    }

    name = models.CharField(max_length=100)
    start_time = models.DateTimeField(default=timezone.now)
    end_time = models.DateTimeField(null=True, blank=True)
    activity_type = models.CharField(max_length=20, choices=ACTIVITY_TYPE_CHOICES, default='rest')
    color = models.CharField(max_length=7, default='#FFFFFF')  # Hex color code

    def save(self, *args, **kwargs):
        self.color = self.COLOR_CHOICES.get(self.activity_type, '#FFFFFF')
        super().save(*args, **kwargs)

    def duration(self):
        if self.end_time:
            return self.end_time - self.start_time
        return timezone.now() - self.start_time

    def __str__(self):
        return self.name
```

### Views

Views handle the logic of the application. Here's an example view for adding an activity:

```python
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
```

## Contributing

Contributions are welcome! Please create an issue or submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License.

---

希望这个 README 文档能帮助您更好地了解和使用这个项目。如果您有任何问题或需要进一步的帮助，请随时告诉我。