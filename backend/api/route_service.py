import requests
import polyline  # 🔥 IMPORTANT: pip install polyline

# 🔑 API KEY
API_KEY = "eyJvcmciOiI1YjNjZTM1OTc4NTExMTAwMDFjZjYyNDgiLCJpZCI6ImU1ZDFlZWZiZDk2ZDQ1ZGY5YjNjMWZmNDYwMjQ5ODY0IiwiaCI6Im11cm11cjY0In0="


# 🔹 STEP 1: Location → Coordinates
def get_coordinates(place):
    url = "https://api.openrouteservice.org/geocode/search"

    params = {
        "api_key": API_KEY,
        "text": place
    }

    try:
        response = requests.get(url, params=params, timeout=10, verify=False)
        data = response.json()

        print(f"[DEBUG] Geocoding response for {place}:", data)

        features = data.get("features", [])
        if not features:
            raise Exception("No results found")

        coords = features[0]["geometry"]["coordinates"]
        return coords  # [lon, lat]

    except Exception as e:
        print(f"[ERROR] Location not found: {place}", e)
        raise Exception(f"Location not found: {place}")


# 🔹 STEP 2: Route calculation
def get_route_data(current, pickup, dropoff):
    try:
        print("[INFO] Getting coordinates...")

        # 🔹 Convert locations to coordinates
        current_coords = get_coordinates(current)
        pickup_coords = get_coordinates(pickup)
        dropoff_coords = get_coordinates(dropoff)

        coordinates = [
            current_coords,
            pickup_coords,
            dropoff_coords
        ]

        print("[DEBUG] Coordinates:", coordinates)

        url = "https://api.openrouteservice.org/v2/directions/driving-car"

        headers = {
            "Authorization": API_KEY,
            "Content-Type": "application/json"
        }

        body = {
            "coordinates": coordinates
        }

        response = requests.post(url, json=body, headers=headers, timeout=10, verify=False)
        data = response.json()

        print("[DEBUG] Route API response:", data)

        # 🔴 अगर route fail हो
        if "routes" not in data:
            print("[ERROR] Route API failed:", data)
            return {
                "distance_km": 0,
                "duration_hr": 0,
                "path": []
            }

        route = data["routes"][0]

        # 🔹 Summary
        summary = route["summary"]
        distance_km = summary["distance"] / 1000
        duration_hr = summary["duration"] / 3600

        # 🔥 🔥 IMPORTANT FIX (Polyline decode)
        encoded_geometry = route["geometry"]

        decoded = polyline.decode(encoded_geometry)

        # Convert to [lat, lon]
        path = [[lat, lon] for lat, lon in decoded]

        print("[INFO] Route calculated successfully")
        print("[INFO] Distance:", distance_km, "km")
        print("[INFO] Duration:", duration_hr, "hours")
        print("[INFO] Path points:", len(path))

        return {
            "distance_km": round(distance_km, 2),
            "duration_hr": round(duration_hr, 2),
            "path": path
        }

    except Exception as e:
        print("[ERROR] Route Error:", e)

        return {
            "distance_km": 0,
            "duration_hr": 0,
            "path": []
        }