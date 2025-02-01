from django.forms import Widget
from django.utils.safestring import mark_safe

class MapWidget(Widget):
    class Media:
        css = {
            'all': ('https://unpkg.com/leaflet@1.9.4/dist/leaflet.css',)
        }
        js = ('https://unpkg.com/leaflet@1.9.4/dist/leaflet.js',)

    def render(self, name, value, attrs=None, renderer=None):
        # Create read-only input field
        input_html = f'<input type="number" step="any" name="{name}" value="{value if value else ""}" id="id_{name}" readonly style="background-color: auto;" />'
        
        # Add map after longitude field
        if 'longitude' in name:
            map_html = """
            <div id="map" style="height: 400px; width: 100%; margin-top: 20px;"></div>
            <div style="margin-top: 10px; color: #666; font-size: 0.9em;">Click on the map to set the coordinates</div>
            <script>
                if (!window.mapInitialized) {
                    window.addEventListener('load', function() {
                        var latInput = document.getElementById('id_latitude');
                        var lngInput = document.getElementById('id_longitude');
                        
                        // Normalize coordinates function
                        function normalizeCoordinates(lat, lng) {
                            // Normalize latitude to [-90, 90]
                            lat = parseFloat(lat);
                            lng = parseFloat(lng);
                            
                            // Handle latitude
                            lat = ((lat + 90) % 180) - 90;
                            if (lat > 90) {
                                lat = 180 - lat;
                            } else if (lat < -90) {
                                lat = -180 - lat;
                            }
                            
                            // Handle longitude
                            lng = ((lng + 180) % 360) - 180;
                            
                            return {
                                lat: parseFloat(lat.toFixed(6)),
                                lng: parseFloat(lng.toFixed(6))
                            };
                        }
                        
                        var map = L.map('map', {
                            worldCopyJump: true,  // Handle date line wrapping
                            maxBounds: L.latLngBounds(L.latLng(-90, -180), L.latLng(90, 180))
                        });
                        
                        L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
                            attribution: '© OpenStreetMap contributors',
                            noWrap: false  // Allow the map to wrap around the date line
                        }).addTo(map);
                        
                        // Get and normalize initial coordinates
                        var coordinates = normalizeCoordinates(
                            latInput.value || 0,
                            lngInput.value || 0
                        );
                        
                        map.setView([coordinates.lat, coordinates.lng], 2);
                        
                        var marker = null;
                        if (coordinates.lat !== 0 || coordinates.lng !== 0) {
                            marker = L.marker([coordinates.lat, coordinates.lng]).addTo(map);
                        }
                        
                        map.on('click', function(e) {
                            // Normalize the clicked coordinates
                            var coords = normalizeCoordinates(e.latlng.lat, e.latlng.lng);
                            
                            latInput.value = coords.lat;
                            lngInput.value = coords.lng;
                            
                            if (marker) {
                                marker.setLatLng([coords.lat, coords.lng]);
                            } else {
                                marker = L.marker([coords.lat, coords.lng]).addTo(map);
                            }
                        });
                        
                        window.mapInitialized = true;
                    });
                }
            </script>
            """
            return mark_safe(input_html + map_html)
        
        return mark_safe(input_html)