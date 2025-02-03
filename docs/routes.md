# Django URL Configuration

## Overview

The URL configuration includes routes for administration, authentication, alerts functionality, and a default redirect to login.

## Routes

### Admin Interface

```python
path('admin/', admin.site.urls)
```

Provides access to Django's built-in administration interface at `/admin/`. This route is restricted to users with admin privileges.

### Authentication Routes

```python
path('accounts/', include('django.contrib.auth.urls'))
```

Includes Django's default authentication views under the `/accounts/` prefix. This provides the following endpoints:

- `/accounts/login/` - Login page
- `/accounts/logout/` - Logout functionality
- `/accounts/password_change/` - Password change form
- `/accounts/password_reset/` - Password reset workflow

### Alert System

```python
path('alerts/', include('alerts.urls'))
```

Includes all URLs defined in the alerts application under the `/alerts/` prefix. The specific endpoints will depend on the routes defined in `alerts.urls`.

### Root URL

```python
path('', auth_views.redirect_to_login)
```

The root URL (`/`) redirects unauthenticated users to the login page. This ensures that users must authenticate before accessing the application.

## Dependencies

- `django.contrib.admin` - For admin interface
- `django.contrib.auth` - For authentication views
- `alerts` - Custom application for alert functionality
