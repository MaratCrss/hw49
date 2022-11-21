from django.contrib import admin
from webapp.models import Tracker, TrackerType, TrackerStatus
# Register your models here.

class TrackerAdmin(admin.ModelAdmin):
    list_display = ['id', 'summary', 'description', 'created_at', 'updated_at']
    list_filter = ['created_at']
    exclude = []

class TrackerTypeAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']
    list_filter = ['title']
    exclude = []

class TrackerStatusAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']
    list_filter = ['title']
    exclude = []

admin.site.register(Tracker, TrackerAdmin)
admin.site.register(TrackerStatus)
admin.site.register(TrackerType)