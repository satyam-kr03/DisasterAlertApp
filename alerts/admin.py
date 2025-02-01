from django.contrib import admin
from .models import Disaster

admin.site.site_header = "Disaster Alert App Admin"
admin.site.site_title = "Disaster Alert App Admin Portal"
admin.site.index_title = "Welcome to the Disaster Alert App Admin Portal"

@admin.register(Disaster)
class DisasterAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'severity', 'timestamp')  # Fields to display in the admin list view
    search_fields = ('name', 'location')  # Enable search by name and location
    list_filter = ('severity', 'timestamp')  # Add filters for severity and timestamp