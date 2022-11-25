from django.db import models

# Create your models here.


class TrackerType(models.Model):
    title = models.CharField(max_length=60, verbose_name="Tip")

    def __str__(self):
        return self.title


class TrackerStatus(models.Model):
    title = models.CharField(max_length=60, verbose_name="Status")

    def __str__(self):
        return self.title


class Tracker(models.Model):
    summary = models.CharField(max_length=140, null=False, blank=False, verbose_name='Kratkoe opisanie')
    description = models.TextField(max_length=3000, null=True, blank=True, verbose_name='Polnoe opisanie')
    status = models.ManyToManyField('webapp.TrackerStatus', related_name='tasks_status', verbose_name='Status', blank=True)
    type = models.ManyToManyField('webapp.TrackerType', related_name='tasks', blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Vremya sozdaniya')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Vremya izmeneniya')

    def __str__(self):
        return f'{self.pk}. {self.summary}'

