## Models Overview

The application uses two main models: `User` and `Disaster`. These models handle user management and disaster event tracking respectively.

## User Model

The `User` model extends Django's built-in `User` model.

```python
from django.contrib.auth.models import User
from django.db import models

class User(User):
    def __str__(self):
        return self.user.username
```

### Fields

Inherits all fields from Django's authentication User model:

- `username`
- `password`
- `email`
- `first_name`
- `last_name`
- And other default User model fields

### Methods

- `__str__()`: Returns the username as a string representation of the User object

## Disaster Model

The `Disaster` model tracks information about disaster events including their location and severity.

```python
class Disaster(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    latitude = models.FloatField()
    longitude = models.FloatField()
    severity = models.CharField(max_length=50)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} at {self.location} ({self.timestamp})"
```

### Fields

| Field       | Type           | Description                                                    |
| ----------- | -------------- | -------------------------------------------------------------- |
| `name`      | CharField(100) | Name of the disaster (e.g., "Earthquake", "Flood")             |
| `location`  | CharField(100) | Description of the location (e.g., "New York City")            |
| `latitude`  | FloatField     | Geographic latitude coordinate                                 |
| `longitude` | FloatField     | Geographic longitude coordinate                                |
| `severity`  | CharField(50)  | Severity level of the disaster (e.g., "Low", "Medium", "High") |
| `timestamp` | DateTimeField  | Automatically set when a disaster is created                   |

### Methods

- `__str__()`: Returns a formatted string containing the disaster name, location, and timestamp

### Usage Example

```python
# Creating a new disaster entry
disaster = Disaster.objects.create(
    name="Earthquake",
    location="San Francisco",
    latitude=37.7749,
    longitude=-122.4194,
    severity="High"
)

# Querying disasters
recent_disasters = Disaster.objects.filter(severity="High").order_by('-timestamp')
nearby_disasters = Disaster.objects.filter(
    latitude__range=(37.7, 37.8),
    longitude__range=(-122.5, -122.3)
)
```
