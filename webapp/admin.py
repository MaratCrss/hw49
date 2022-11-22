from django.contrib import admin
from webapp.models import Tracker, TrackerType, TrackerStatus
# Register your models here.

# class TrackerAdmin(admin.ModelAdmin):
#     list_display = ['id', 'summary', 'description', 'created_at', 'updated_at']
#     list_filter = ['created_at']
#     exclude = []
#
# class TrackerTypeAdmin(admin.ModelAdmin):
#     list_display = ['id', 'title']
#     list_filter = ['title']
#     exclude = []
#
# # class TrackerStatusAdmin(admin.ModelAdmin):
# #     list_display = ['id', 'title']
# #     list_filter = ['title']
# #     exclude = []
#
# class TrackerAdmin(admin.ModelAdmin):
#     list_display = ['id', 'summary', 'description', 'type', 'status']
#
#     def type(self, object):
#         for type in object.type.all():
#             return type
#     list_display_links = ['summary']
#     list_filter = ['description']
#     search_fields = ['summary', 'description']
#     exclude = []
#     readonly_fields = ['created_at', 'updated_at']

admin.site.register(Tracker)
admin.site.register(TrackerStatus)
admin.site.register(TrackerType)