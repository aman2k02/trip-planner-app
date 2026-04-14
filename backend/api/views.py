import requests
from rest_framework.decorators import api_view
from rest_framework.response import Response
from hos.engine import generate_trip_plan
from api.route_service import get_route_data
from logs.generator import generate_log_image


# 🔍 Location Search API
@api_view(['GET'])
def search_location(request):
    query = request.GET.get("q")

    if not query:
        return Response([])

    url = "https://api.openrouteservice.org/geocode/search"

    params = {
        "api_key": "YOUR_API_KEY",  
        "text": query,
        "size": 5
    }

    try:
        res = requests.get(url, params=params)
        data = res.json()

        results = []

        for item in data.get("features", []):
            results.append({
                "name": item["properties"]["label"]
            })

        return Response(results)

    except Exception as e:
        print("[ERROR] Search API failed:", e)
        return Response([])


# 🚛 Main Trip Planner API
@api_view(['POST'])
def plan_trip(request):
    try:
        data = request.data

        current = data.get("current_location")
        pickup = data.get("pickup_location")
        dropoff = data.get("dropoff_location")
        cycle_used = float(data.get("cycle_used", 0))

        # 🔴 Validation
        if not current or not pickup or not dropoff:
            return Response({
                "error": "All locations are required"
            }, status=400)

        print("[INFO] Starting trip planning...")

        # 🔹 Step 1: Get Route
        route = get_route_data(current, pickup, dropoff)

        distance = route.get("distance_km", 0)
        duration = route.get("duration_hr", 0)

        print("[INFO] Route received:", route)

        if distance == 0 or duration == 0:
            return Response({
                "error": "Failed to fetch route. Check locations."
            }, status=400)

        # 🔹 Step 2: Generate Trip Plan
        plan = generate_trip_plan(duration, distance, cycle_used)

        print("[INFO] Trip plan generated")

        # 🔹 Step 3: Generate Logs (BASE64)
        logs = []

        for day in plan:
            try:
                log_base64 = generate_log_image(day)  #  returns base64
                if log_base64:
                    logs.append(log_base64)
            except Exception as e:
                print("[ERROR] Log generation failed:", e)

        print("[INFO] Logs generated (base64)")

        # 🔹 Final Response (NO URL, DIRECT IMAGE)
        return Response({
            "route": route,
            "plan": plan,
            "logs": logs
        })

    except Exception as e:
        print("[ERROR] API failed:", e)

        return Response({
            "error": "Something went wrong"
        }, status=500)
