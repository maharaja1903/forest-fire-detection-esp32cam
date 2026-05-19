import cv2
import time
from ultralytics import YOLO
from twilio.rest import Client

# TWILIO CONFIG
account_sid = "YOUR_ACCOUNT_SID"
auth_token = "YOUR_AUTH_TOKEN"

client = Client(account_sid, auth_token)

TO_NUMBER = "+919790343705"
FROM_NUMBER = "+15097400028"

# LOAD YOLO MODEL
model = YOLO("best.engine", task="detect")

# VIDEO SOURCE
STREAM_URL = "http://10.251.170.250:81/stream"

cap = cv2.VideoCapture(
    STREAM_URL,
    cv2.CAP_FFMPEG
)

cap.set(cv2.CAP_PROP_BUFFERSIZE, 1)

# ALERT SETTINGS
last_alert_time = 0
alert_interval = 60  # seconds

# MAIN LOOP
while True:

    ret, frame = cap.read()

    # CHECK FRAME
    if not ret:
        print("Frame not received")
        break

    # YOLO DETECTION
    results = model.predict(
        frame,
        imgsz=640,
        conf=0.5
    )

    # DRAW DETECTION BOXES
    annotated_frame = results[0].plot()

    # CHECK FIRE DETECTION
    if len(results[0].boxes) > 0:

        current_time = time.time()

        # PREVENT SMS/CALL SPAM
        if current_time - last_alert_time > alert_interval:

            print("FIRE DETECTED")

            try:

                # SEND SMS
                client.messages.create(
                    body="🔥 FIRE DETECTED! CHECK IMMEDIATELY!",
                    to=TO_NUMBER,
                    from_=FROM_NUMBER
                )

                print("SMS SENT")

                # MAKE CALL
                client.calls.create(
                    twiml='''
                    <Response>
                        <Say>
                            Warning. Fire detected.
                            Please check immediately.
                        </Say>
                    </Response>
                    ''',
                    to=TO_NUMBER,
                    from_=FROM_NUMBER
                )

                print("CALL SENT")

                last_alert_time = current_time

            except Exception as e:
                print("TWILIO ERROR:")
                print(e)

    # SHOW OUTPUT
    cv2.imshow("YOLO FIRE DETECTION", annotated_frame)

    # PRESS Q TO EXIT
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


# RELEASE
cap.release()
cv2.destroyAllWindows()