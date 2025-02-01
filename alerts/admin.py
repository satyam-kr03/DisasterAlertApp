from django.contrib import admin
from .models import Disaster
from .widgets import MapWidget
from django import forms

admin.site.site_header = "Disaster Alert App Admin"
admin.site.site_title = "Disaster Alert App Admin Portal"
admin.site.index_title = "Welcome to the Disaster Alert App Admin Portal"

class DisasterForm(forms.ModelForm):
    class Meta:
        model = Disaster
        fields = '__all__'
        widgets = {
            'latitude': MapWidget(),
            'longitude': MapWidget()
        }

@admin.register(Disaster)
class DisasterAdmin(admin.ModelAdmin):
    form = DisasterForm
    list_display = ('name', 'location', 'severity', 'timestamp')
    search_fields = ('name', 'location')
    list_filter = ('severity', 'timestamp')