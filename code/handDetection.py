import mediapipe as mp
import cv2
import numpy as np

mpHands = mp.solutions.hands
mpDraw = mp.solutions.drawing_utils

class HandDetector:
    def __init__(self, max_num_hands=2, min_detection_confidence=0.5, min_tracking_confidence=0.5):
        self.hands = mpHands.Hands(max_num_hands=max_num_hands, min_detection_confidence=min_detection_confidence,
                                   min_tracking_confidence=min_tracking_confidence)

    def findHandLandMarks(self, image, handNumber=0, draw=False):
        originalImage = image
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)  # mediapipe needs RGB
        results = self.hands.process(image)
        landMarkList = []

        if results.multi_hand_landmarks:  # returns None if hand is not found
            hand = results.multi_hand_landmarks[handNumber] #results.multi_hand_landmarks returns landMarks for all the hands

            for id, landMark in enumerate(hand.landmark):
                # landMark holds x,y,z ratios of single landmark
                imgH, imgW, imgC = originalImage.shape  # height, width, channel for image
                xPos, yPos = int(landMark.x * imgW), int(landMark.y * imgH)
                landMarkList.append([id, xPos, yPos])

            if draw:
                mpDraw.draw_landmarks(originalImage, hand, mpHands.HAND_CONNECTIONS)
        # print(landMarkList)
        return landMarkList

    def get_label(index, hand, results):
        # output = None
        for idx, classification in enumerate(results.multi_handedness):
            if classification.classification[0].index == index:
                
                # Process results
                label = classification.classification[0].label
                score = classification.classification[0].score
                text = '{} {}'.format(label, round(score, 2))
                
                # Extract Coordinates
                # coords = tuple(np.multiply(
                #      np.array((hand.landmark[mp_hands.HandLandmark.WRIST].x,
                #      hand.landmark[mp_hands.HandLandmark.WRIST].y)),
                #      [640,480]).astype(int))
                
                # output = text, coords
        # return output
        return text
# results = self.hands.process(image)
