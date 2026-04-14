from PIL import Image, ImageDraw
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
template_path = os.path.join(BASE_DIR, "logs", "templates", "blank-paper-log.png")


def generate_log_image(day_data):
    try:
        print(f"[INFO] Generating log for Day {day_data['day']}")

        # 🔥 Create media folder
        media_dir = os.path.join(BASE_DIR, "media")
        os.makedirs(media_dir, exist_ok=True)

        # 🔥 Unique file per day
        file_name = f"log_day_{day_data['day']}.png"
        output_path = os.path.join(media_dir, file_name)

        # 🔹 Load template
        img = Image.open(template_path)
        draw = ImageDraw.Draw(img)

        # 🔹 Y-axis positions
        y_positions = {
            "off": 300,
            "sleeper": 250,
            "drive": 200,
            "on": 150
        }

        # 🔹 Scale for 24 hrs
        total_width = img.size[0] - 100
        x_scale = total_width / 24

        current_hour = 0

        for event in day_data["events"]:
            event_type = event["type"]
            hours = round(event["hours"], 2)

            start_x = 50 + (current_hour * x_scale)
            end_x = 50 + ((current_hour + hours) * x_scale)

            # 🔹 Map event type
            if event_type == "drive":
                y = y_positions["drive"]
            elif event_type == "break":
                y = y_positions["on"]
            elif event_type == "rest":
                y = y_positions["sleeper"]
            elif event_type == "cycle_reset":
                y = y_positions["off"]
            elif event_type in ["pickup", "dropoff", "fuel"]:
                y = y_positions["on"]
            else:
                y = y_positions["off"]

            draw.line((start_x, y, end_x, y), fill="black", width=3)

            current_hour += hours

        # 🔹 Save image
        img.save(output_path)

        print(f"[INFO] Log saved: {output_path}")

        # 🔥 IMPORTANT: return URL path (not file path)
        return f"/media/{file_name}"

    except Exception as e:
        print("[ERROR] Log generation failed:", e)
        return None
