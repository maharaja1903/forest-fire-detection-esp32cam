import cv2
from ultralytics import YOLO
from twilio.rest import Client
import time

# =========================
# TWILIO CONFIG
# =========================
account_sid = "YOUR_ACCOUNT_SID"
auth_token = "YOUR_AUTH_TOKEN"


TO_NUMBER = "+919790343705"
FROM_NUMBER = "+15097400028"

client = Client(ACCOUNT_SID, AUTH_TOKEN)

# =========================
# LOAD MODEL
# =========================
model = YOLO("best.engine")

# =========================
# VIDEO SOURCE
# =========================
cap = cv2.VideoCapture(0)

# For Mobile IP Camera:
# cap = cv2.VideoCapture(
#     "http://10.251.170.250/stream",
#     cv2.CAP_FFMPEG
# )

cap.set(cv2.CAP_PROP_BUFFERSIZE, 1)

# =========================
# ALERT CONTROL
# =========================
last_alert_time = 0
ALERT_INTERVAL = 30   # seconds

# =========================
# MAIN LOOP
# =========================
while True:

    ret, frame = cap.read()

    if not ret:
        print("Camera Error")
        break

    # YOLO Detection
    results = model(frame, imgsz=640)

    # Draw Detection Boxes
    frame = results[0].plot()

    # Fire Detection Check
    if len(results[0].boxes) > 0:

        current_time = time.time()

        # Prevent Spam Alerts
        if current_time - last_alert_time > ALERT_INTERVAL:

            print("🔥 FIRE DETECTED")

            # SMS ALERT
            client.messages.create(
                body="🔥 FIRE DETECTED! CHECK IMMEDIATELY",
                to=TO_NUMBER,
                from_=FROM_NUMBER
            )

            # CALL ALERT
            client.calls.create(
                twiml="""
                <Response>
                    <Say>
                        Fire detected. Please check immediately.
                    </Say>
                </Response>
                """,
                to=TO_NUMBER,
                from_=FROM_NUMBER
            )

            print("✅ Alert Sent")

            last_alert_time = current_time

    # Display Window
    cv2.imshow("Fire Detection", frame)

    # Press Q to Exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# =========================
# RELEASE
# =========================
cap.release()
cv2.destroyAllWindows()