import cv2
import handDetection as htm
import serial

def sendData(data):
    myString = "$"
    for d in data:
        myString += str(int(d)).zfill(1)
    serial.write(myString.encode())

# ser = serial.Serial("COM3", 9600)

wCam, hCam = 640, 480

cap = cv2.VideoCapture(0)
detector = htm.HandDetector(max_num_hands=2, min_detection_confidence=0.75)


tipIds = [4, 8, 12, 16, 20]    # [Thumb tip, Index tip, Middle finger tip, Ring finger tip, Pinky finger tip]

while True:
    success, img = cap.read()

    lmList = detector.findHandLandMarks(img, draw=True)
    if len(lmList) != 0:
        fingers = []
        
        # Right Thumb
        if lmList[4][1] > lmList[20][1]:
            if lmList[tipIds[0]][1] > lmList[tipIds[0] - 1][1]:      # In tihs case we check for lmList[Thumb][x-axis(1)]
                fingers.append(1)
            else:
                fingers.append(0)
        # Left Thumb
        else:
            if lmList[tipIds[0]][1] > lmList[tipIds[0] - 1][1]:      # In tihs case we check for lmList[Thumb][x-axis(1)]
                fingers.append(0)
            else:
                fingers.append(1)
                
        # 4 Fingers
        for id in range(1, 5):
            if lmList[tipIds[id]][2] < lmList[tipIds[id] - 2][2]:       # lmList[finger_tip_id][y-axis(2)]
                fingers.append(1)
            else:
                fingers.append(0)

        print(fingers)
        # sendData(fingers)
        for i in range(300):
            cv2.imshow("image", img)
            
    cv2.imshow("Image", img)
    if (cv2.waitKey(1) & 0xFF == ord('q') ):
        # for i in range(10):
        #     sendData([0, 0, 0, 0, 0])
        cap.release()
        cv2.destroyAllWindows()
        break