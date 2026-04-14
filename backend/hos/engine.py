MAX_DRIVE_HOURS = 11
BREAK_AFTER = 8
REST_HOURS = 10
CYCLE_LIMIT = 70  # 70 hrs / 8 days

PICKUP_TIME = 1      # 1 hour
DROPOFF_TIME = 1     # 1 hour
FUEL_DISTANCE = 1600  # km (~1000 miles)
FUEL_TIME = 0.5      # 30 min


def generate_trip_plan(total_hours, distance, cycle_used):
    days = []
    remaining_hours = total_hours
    remaining_distance = distance

    used_cycle = cycle_used
    day_count = 1

    avg_speed = distance / total_hours if total_hours > 0 else 50

    print("[INFO] Starting HOS simulation...")

    while remaining_hours > 0:

        # 🔥 Cycle reset check
        if used_cycle >= CYCLE_LIMIT:
            print("[INFO] Cycle limit reached → applying 34hr reset")

            days.append({
                "day": day_count,
                "events": [
                    {"type": "cycle_reset", "hours": 34}
                ],
                "total_drive_hours": 0,
                "total_distance": 0
            })

            used_cycle = 0
            day_count += 1
            continue

        day = {
            "day": day_count,
            "events": [],
            "total_drive_hours": 0,
            "total_distance": 0
        }

        # 🔥 Pickup only on Day 1
        if day_count == 1:
            day["events"].append({
                "type": "pickup",
                "hours": PICKUP_TIME
            })

        # 🔥 Available cycle hours
        available_cycle = CYCLE_LIMIT - used_cycle

        # 🔥 Driving hours
        drive_hours = min(MAX_DRIVE_HOURS, remaining_hours, available_cycle)

        if drive_hours <= 0:
            break

        drive_hours = round(drive_hours, 2)

        # 🔹 Break logic
        if drive_hours > BREAK_AFTER:
            day["events"].append({"type": "drive", "hours": BREAK_AFTER})
            day["events"].append({"type": "break", "hours": 0.5})

            remaining_drive = round(drive_hours - BREAK_AFTER, 2)

            day["events"].append({
                "type": "drive",
                "hours": remaining_drive
            })
        else:
            day["events"].append({
                "type": "drive",
                "hours": drive_hours
            })

        # 🔹 Distance calculation
        distance_today = min(drive_hours * avg_speed, remaining_distance)
        distance_today = round(distance_today, 2)

        # 🔥 Fuel stop logic
        if distance_today >= FUEL_DISTANCE:
            day["events"].append({
                "type": "fuel",
                "hours": FUEL_TIME
            })

        day["total_drive_hours"] = drive_hours
        day["total_distance"] = distance_today

        # 🔹 Last day check
        is_last_day = remaining_hours <= drive_hours

        # 🔥 Drop only on last day
        if is_last_day:
            day["events"].append({
                "type": "dropoff",
                "hours": DROPOFF_TIME
            })

        # 🔹 Rest (NOT on last day)
        if not is_last_day:
            day["events"].append({
                "type": "rest",
                "hours": REST_HOURS
            })

        # 🔹 Update counters
        remaining_hours -= drive_hours
        remaining_distance -= distance_today
        used_cycle += drive_hours

        print(f"[INFO] Day {day_count}: drove {drive_hours} hrs, {distance_today} km")

        days.append(day)
        day_count += 1

    print("[INFO] Trip simulation complete")

    return days