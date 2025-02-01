from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout
from .utils import haversine
from .models import Disaster

@csrf_exempt
def update_location(request):
    if request.method == 'POST':
        # Get latitude and longitude from the request
        latitude = float(request.POST.get('latitude'))
        longitude = float(request.POST.get('longitude'))

        # Fetch disasters within a certain radius (e.g., 50km)
        # Note: This is a simple implementation. For production, use a geospatial library like GeoDjango.
        disasters = Disaster.objects.filter(
            latitude__range=(latitude - 0.5, latitude + 0.5),
            longitude__range=(longitude - 0.5, longitude + 0.5)
        )

        # Prepare disaster data to send back to the frontend
        disaster_data = [
            {
                'name': d.name,
                'location': d.location,
                'severity': d.severity,
                'latitude': d.latitude,
                'longitude': d.longitude,
            }
            for d in disasters
        ]

        return JsonResponse({'disasters': disaster_data})
    return JsonResponse({'error': 'Invalid request method'}, status=400)


@login_required
def dashboard(request):
    return render(request, 'dashboard.html')


@login_required
def set_location(request):
    try:
        if request.method == 'POST':
            # Save the user's location in the session
            request.session['latitude'] = float(request.POST.get('latitude'))
            request.session['longitude'] = float(request.POST.get('longitude'))
            return redirect('dashboard')  # Redirect to the dashboard
    except ValueError:
        pass
    return render(request, 'set_location.html')

@login_required
def dashboard(request):
    # Get the user's location from the session
    latitude = request.session.get('latitude')
    longitude = request.session.get('longitude')

    if latitude is None or longitude is None:
        return redirect('set_location')  # Redirect to set location if not set

    # Pass the location to the template (optional)
    context = {
        'latitude': latitude,
        'longitude': longitude,
    }
    return render(request, 'dashboard.html', context)



@csrf_exempt
def check_new_disasters(request):
    if request.method == 'POST':
        # Get the user's location from the request
        latitude = float(request.POST.get('latitude'))
        longitude = float(request.POST.get('longitude'))

        # Fetch all disasters and filter by distance
        disasters = Disaster.objects.all()
        new_disasters = []
        for disaster in disasters:
            distance = haversine(latitude, longitude, disaster.latitude, disaster.longitude)
            if distance <= 50:  # 50 km radius
                new_disasters.append({
                    'name': disaster.name,
                    'location': disaster.location,
                    'severity': disaster.severity,
                })

        return JsonResponse({'disasters': new_disasters})
    return JsonResponse({'error': 'Invalid request method'}, status=400)

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.save()
            return redirect('login')  # Redirect to the dashboard
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')

def redirect_to_login(request):
    return redirect("login")
