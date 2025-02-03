## Authentication Endpoints

### Signup

**URL:** `/signup/`  
**Method:** `POST`  
**Description:** Register new user account  
**Form Data:**

- `username`: String
- `password1`: String
- `password2`: String (confirmation)

**Returns:** Redirects to login page

### Logout

**URL:** `/logout/`  
**Method:** `GET`  
**Description:** Logs out current user  
**Returns:** Redirects to login page

## Location Management

### Update Location

**URL:** `/update-location/`  
**Method:** `POST`  
**Description:** Updates user location and returns nearby disasters  
**Form Data:**

- `latitude`: Float
- `longitude`: Float

**Returns:** JSON

```json
{
    "disasters": [
        {
            "name": "string",
            "location": "string",
            "severity": "string",
            "latitude": float,
            "longitude": float,
            "timestamp": "datetime"
        }
    ]
}
```

### Set Location

**URL:** `/alerts/set-location/`  
**Method:** `POST`  
**Authentication:** Required  
**Form Data:**

- `latitude`: Float
- `longitude`: Float

**Returns:** Redirects to dashboard

### Check New Disasters

**URL:** `/check-new-disasters/`  
**Method:** `POST`  
**Description:** Checks for disasters within 50km radius  
**Form Data:**

- `latitude`: Float
- `longitude`: Float

**Returns:** JSON

```json
{
  "disasters": [
    {
      "name": "string",
      "location": "string",
      "severity": "string",
      "timestamp": "datetime"
    }
  ]
}
```

## Dashboard Views

### Dashboard

**URL:** `/dashboard/`  
**Method:** `GET`  
**Authentication:** Required  
**Description:** Main dashboard view showing user's location  
**Context Data:**

- `latitude`: Float
- `longitude`: Float

**Returns:** Renders dashboard.html template

### Redirect to Login

**URL:** `/`  
**Method:** `GET`  
**Description:** Redirects root URL to login page  
**Returns:** Redirects to login page
