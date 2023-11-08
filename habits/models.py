from django.db import models
from config import settings
import django as django

from constants import NULLABLE


class Habit(models.Model):

    class HabitFrequency(models.TextChoices):
        Daily = 'DAILY'
        monday = 'MONDAY'
        tuesday = 'TUESDAY'
        wednesday = 'WEDNESDAY'
        thursday = 'THURSDAY'
        friday = 'FRIDAY'
        saturday = 'SATURDAY'
        sunday = 'SUNDAY'

    owner = models.ForeignKey(settings.AUTH_USER_MODEL,
                              on_delete=models.CASCADE, **NULLABLE, verbose_name="owner of habit")
    place = models.CharField(max_length=100, **NULLABLE,
                             verbose_name="place for habit")
    time = models.TimeField(default=django.utils.timezone.now,
                            verbose_name="start time for habit")
    action = models.CharField(max_length=100, **NULLABLE,
                              verbose_name="habit action")
    is_pleasant = models.BooleanField(default=False,
                                      verbose_name="flag for pleasant habit")
    link_pleasant = models.ForeignKey("self", on_delete=models.CASCADE,
                                      **NULLABLE)
    frequency = models.CharField(choices=HabitFrequency.choices,
                                 default=HabitFrequency.Daily, max_length=50)
    award = models.CharField(max_length=100, **NULLABLE,
                             verbose_name="award for habit")
    duration = models.IntegerField(**NULLABLE,
                                   verbose_name="habit duration")
    is_public = models.BooleanField(default=True)

    def __str__(self):
        return f"ACTION: {self.action} PLACE: {self.place}"

    class Meta:
        verbose_name = "habit"
        verbose_name_plural = 'habits'
        ordering = ['-id']
