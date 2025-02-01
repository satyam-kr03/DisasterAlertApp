from django.contrib.auth.models import User
from django.db import models

class User(User):
    def __str__(self):
        return self.user.username

class Disaster(models.Model):
    # Disaster name (e.g., "Earthquake", "Flood")
    name = models.CharField(max_length=100)

    # Location description (e.g., "New York City")
    location = models.CharField(max_length=100)

    # Latitude and longitude for geolocation
    latitude = models.FloatField()
    longitude = models.FloatField()

    # Severity level (e.g., "Low", "Medium", "High")
    severity = models.CharField(max_length=50)

    # Timestamp for when the disaster was registered
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} at {self.location} ({self.timestamp})"
    
    