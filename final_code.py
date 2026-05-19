import cv2
import time
import threading
from ultralytics import YOLO
from twilio.rest import Client

# TWILIO CONFIG
account_sid = "YOUR_ACCOUNT_SID"
auth_token = "YOUR_AUTH_TOKEN"

client = Client(account_sid, auth_token)

TO_NUMBER = "+919790343705"
FROM_NUMBER = "+15097400028"

# LOAD MODEL
model = YOLO("best.engine", task="detect")


# VIDEO STREAM
STREAM_URL = "http://10.251.170.250:81/stream"
# http://10.251.170.250/
cap = cv2.VideoCapture(
    STREAM_URL,
    cv2.CAP_FFMPEG
)

# cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_BUFFERSIZE, 1)


# ALERT CONTROL
last_alert_time = 0
alert_interval = 60



# SEND ALERT FUNCTION
def send_alert():

    try:

        # SMS
        client.messages.create(
            body="🔥 FIRE DETECTED! CHECK IMMEDIATELY!",
            to=TO_NUMBER,
            from_=FROM_NUMBER
        )

        print("SMS SENT")

        # CALL
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

    except Exception as e:
        print("TWILIO ERROR:")
        print(e)


# MAIN LOOP

while True:

    ret, frame = cap.read()

    if not ret:
        print("Frame not received")
        break

    # YOLO
    results = model.predict(
        frame,
        imgsz=640,
        conf=0.5,
        verbose=False
    )

    annotated_frame = results[0].plot()

    # FIRE DETECTED
    if len(results[0].boxes) > 0:

        current_time = time.time()

        if current_time - last_alert_time > alert_interval:

            print("FIRE DETECTED")

            # RUN ALERT IN BACKGROUND
            threading.Thread(
                target=send_alert,
                daemon=True
            ).start()

            last_alert_time = current_time

    # SHOW
    cv2.imshow("YOLO FIRE DETECTION", annotated_frame)

    # EXIT
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()