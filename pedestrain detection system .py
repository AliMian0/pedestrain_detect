import cv2

hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

video_path = r"C:\Users\alimi\OneDrive\Desktop\d3.mp4"
video_capture = cv2.VideoCapture(video_path)

display_width = 640
display_height = 480

# Initialize counters
total_pedestrians = 0
crossed_pedestrians = 0

while video_capture.isOpened():
    ret, frame = video_capture.read()

    if not ret:
        break

    frame = cv2.resize(frame, (display_width, display_height))

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect pedestrians in the frame
    pedestrians, _ = hog.detectMultiScale(gray)

    for (x, y, w, h) in pedestrians:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # Check if pedestrian has crossed the road (you can customize the condition based on your video)
        if y + h >= display_height // 2:
            crossed_pedestrians += 1

        total_pedestrians += 1

    cv2.imshow('Pedestrian Detection', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video_capture.release()
cv2.destroyAllWindows()

print("Total pedestrians detected:", total_pedestrians)
print("Pedestrians crossed the road:", crossed_pedestrians)
