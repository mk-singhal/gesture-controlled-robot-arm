import cvzone
import cv2

cap = cv2.VideoCapture(0)
detector = cvzone.HandDetector(maxHands=1, detectionCon=0.75)
ser = cvzone.SerialObject("COM4", 9600, 1)

while True:
    success, img = cap.read()
    img = detector.findHands(img)
    lmList, bbox = detector.findPosition(img)
    if lmList:
        fingers = detector.fingersUp()
        print(fingers)
        ser.sendData(fingers)
        for i in range(300):
            cv2.imshow("image", img)
    cv2.imshow("image", img)
    if (cv2.waitKey(1) & 0xFF == ord('q') ):
        ser.sendData([1, 1, 1, 1, 1])
        cap.release()
        cv2.destroyAllWindows()
        break
