from PIL import Image, ImageDraw
import os


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
template_path = os.path.join(BASE_DIR, "logs", "templates", "blank-paper-log.png")


def generate_log_image(day_data, output_path="media/log.png"):
    try:
        print(f"[INFO] Generating log for Day {day_data['day']}")

        

        # 🔹 Load template (ensure correct path)
        img = Image.open(template_path)
        draw = ImageDraw.Draw(img)

        # 🔹 Y-axis positions (adjusted for log sheet)
        y_positions = {
            "off": 300,
            "sleeper": 250,
            "drive": 200,
            "on": 150
        }

        # 🔹 Scale: 24 hours width
        total_width = img.size[0] - 100  # margin adjust
        x_scale = total_width / 24  # pixels per hour

        current_hour = 0

        for event in day_data["events"]:
            event_type = event["type"]
            hours = event["hours"]

            start_x = 50 + (current_hour * x_scale)
            end_x = 50 + ((current_hour + hours) * x_scale)

            # 🔹 Map event type to correct row
            if event_type == "drive":
                y = y_positions["drive"]
            elif event_type == "break":
                y = y_positions["on"]
            elif event_type == "rest":
                y = y_positions["sleeper"]
            elif event_type == "cycle_reset":
                y = y_positions["off"]
            else:
                y = y_positions["off"]

            # 🔹 Draw horizontal line
            draw.line((start_x, y, end_x, y), fill="black", width=3)

            # 🔹 Move timeline forward
            current_hour += hours

        # 🔹 Ensure folder exists
        os.makedirs(os.path.dirname(output_path), exist_ok=True)

        # 🔹 Save image
        img.save(output_path)

        print(f"[INFO] Log saved: {output_path}")

        return output_path

    except Exception as e:
        print("[ERROR] Log generation failed:", e)
        return None