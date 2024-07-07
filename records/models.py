# records/models.py

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

    def duration_minutes(self):
        if self.end_time:
            duration = self.end_time - self.start_time
        else:
            duration = timezone.now() - self.start_time
        return duration.total_seconds() / 60  # duration in minutes

    def scaled_duration(self, scale=2, min_height=20):
        scaled_height = self.duration_minutes() / scale
        return max(scaled_height, min_height)

    def __str__(self):
        return self.name