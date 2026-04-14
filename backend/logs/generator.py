from PIL import Image, ImageDraw
import os
import base64
from io import BytesIO

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
template_path = os.path.join(BASE_DIR, "logs", "templates", "blank-paper-log.png")


def generate_log_image(day_data):
    try:
        print(f"[INFO] Generating log for Day {day_data['day']}")

        # 🔹 Load template
        img = Image.open(template_path)
        draw = ImageDraw.Draw(img)

        y_positions = {
            "off": 300,
            "sleeper": 250,
            "drive": 200,
            "on": 150
        }

        total_width = img.size[0] - 100
        x_scale = total_width / 24

        current_hour = 0

        for event in day_data["events"]:
            event_type = event["type"]
            hours = round(event["hours"], 2)

            start_x = 50 + (current_hour * x_scale)
            end_x = 50 + ((current_hour + hours) * x_scale)

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

        # 🔥 Convert to base64
        buffer = BytesIO()
        img.save(buffer, format="PNG")
        img_str = base64.b64encode(buffer.getvalue()).decode()

        return f"data:image/png;base64,{img_str}"

    except Exception as e:
        print("[ERROR] Log generation failed:", e)
        return None
