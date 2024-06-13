import cv2
import os

#############################################
frameWidth = 640
frameHeight = 480
cascadePath = "haarcascades/haarcascade_russian_plate_number.xml"
videoPath = "video12.mp4"
minArea = 200
color = (255, 0, 255)
###############################################

# Check if the cascade file exists
if not os.path.isfile(cascadePath):
    print(f"Error: Cascade file '{cascadePath}' not found")
    exit()

nPlateCascade = cv2.CascadeClassifier(cascadePath)

# Check if the video file exists
if not os.path.isfile(videoPath):
    print(f"Error: Video file '{videoPath}' not found")
    exit()

cap = cv2.VideoCapture(videoPath)
if not cap.isOpened():
    print(f"Error: Could not open video file '{videoPath}'")
    exit()

cap.set(3, frameWidth)
cap.set(4, frameHeight)
cap.set(10, 150)
count = 0

while True:
    success, img = cap.read()
    if not success:
        print("Error: Could not read frame from video or end of video reached")
        break

    if img is None or img.size == 0:
        print("Error: Frame is empty")
        break
    
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    numberPlates = nPlateCascade.detectMultiScale(imgGray, 1.1, 10)
    for (x, y, w, h) in numberPlates:
        area = w * h
        if area > minArea:
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 255), 2)
            cv2.putText(img, "Number Plate", (x, y - 5),
                        cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, color, 2)
            imgRoi = img[y:y + h, x:x + w]
            cv2.imshow("ROI", imgRoi)

    cv2.imshow("Result", img)

    if cv2.waitKey(1) & 0xFF == ord('s'):
        if 'imgRoi' in locals():
            if not os.path.exists("Scanned"):
                os.makedirs("Scanned")
            cv2.imwrite(f"Scanned/NoPlate_{count}.jpg", imgRoi)
            cv2.rectangle(img, (0, 200), (640, 300), (0, 255, 0), cv2.FILLED)
            cv2.putText(img, "Scan Saved", (150, 265), cv2.FONT_HERSHEY_DUPLEX,
                        2, (0, 0, 255), 2)
            cv2.imshow("Result", img)
            cv2.waitKey(500)
            count += 1
        else:
            print("No ROI to save")

cap.release()
cv2.destroyAllWindows()
