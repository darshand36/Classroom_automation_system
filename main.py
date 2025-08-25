import cv2
import numpy as np
import time
import math
import random
import serial

# Initialize serial communication with Arduino on COM4
arduino = serial.Serial('COM4', 9600, timeout=1)  # Adjust 'COM4' to match your port

# videoSource = 0
cap = cv2.VideoCapture(1)

net = cv2.dnn.readNet(r"yolov3.weights", r"yolov3.cfg")

people = []
personId = 0
colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]
enteredPeople = 0
exitedPeople = 0
doorThresh = 50
doorCoord = (670, 400)
appendThresh = 80

class Person:
    def __init__(self, personId, location):
        self.id = personId
        self.curLocation = location
        self.trajectory = []
        self.state = []
        self.flag = 0
        if personId < len(colors):
            self.color = colors[personId]
        else:
            self.color = colors[personId % len(colors)]

    def addPointToTrajectory(self, location):
        self.trajectory.append(location)

def plotTrajectories(frame):
    global people, doorCoord
    for person in people:
        prev_point = None
        traj = person.trajectory[-5:]
        for i in traj:
            x, y = i[0], i[1]
            frame = cv2.circle(frame, (x, y), 3, person.color, cv2.FILLED)
            if prev_point is not None:
                frame = cv2.line(frame, prev_point, (x, y), person.color, 1)
            prev_point = (x, y)
    return frame

def calcDist(a, b):
    return math.sqrt(((b[0] - a[0]) ** 2) + ((b[1] - a[1]) ** 2))

def sendSignalToArduino(signal):
    print(f"Sending signal to Arduino: {signal}")  # Debugging line
    arduino.write(signal.encode())

def trackerHandle(curCoords, frame):
    global people, enteredPeople, exitedPeople, doorCoord, appendThresh

    # Check if there are any people in the frame
    if len(people) > 0:
        if len(curCoords) > 0:
            for person in people:
                dists = [calcDist(curCoord, person.curLocation) for curCoord in curCoords]

                if len(dists) > 0:  # Check if dists is not empty
                    minIndex = dists.index(min(dists))

                    if calcDist(person.curLocation, curCoords[minIndex]) < appendThresh:
                        person.trajectory.append(curCoords[minIndex])
                        person.curLocation = curCoords[minIndex]

                    curCoords.pop(minIndex)
        else:
            # If no coordinates, clear the people list and turn off light
            people.clear()
            sendSignalToArduino('L')  # Send signal to turn off light if no one is detected

    else:
        # If no people are currently tracked, add new persons from current coordinates
        for coord in curCoords:
            people.append(Person(len(people), coord))

    # Check if the people list is empty and send appropriate signal
    if len(people) == 0:
        print("No people detected. Sending signal to turn off light.")
        sendSignalToArduino('L')  # Send 'L' to turn off light
    else:
        sendSignalToArduino('H')  # Send 'H' to keep light on

    frame = plotTrajectories(frame)
    return frame

font = cv2.FONT_HERSHEY_PLAIN

with open("coco.names", "r") as f:
    classes = f.read().strip().split('\n')

cv2.namedWindow("Person Tracking", cv2.WINDOW_NORMAL)

while True:
    ret, frame = cap.read()
    frame = cv2.resize(frame, (800, 600))
    frame = cv2.circle(frame, doorCoord, 5, (255, 0, 0))

    blob = cv2.dnn.blobFromImage(frame, 0.00392, (416, 416), swapRB=True, crop=False)
    net.setInput(blob)
    outs = net.forward(net.getUnconnectedOutLayersNames())

    class_ids = []
    confidences = []
    boxes = []

    for out in outs:
        for detection in out:
            scores = detection[5:]
            class_id = np.argmax(scores)
            confidence = scores[class_id]

            if confidence > 0.5 and classes[class_id] == 'person':
                center_x, center_y, w, h = (detection[0:4] * np.array([frame.shape[1], frame.shape[0], frame.shape[1], frame.shape[0]])).astype(int)
                x, y = int(center_x - w / 2), int(center_y - h / 2)
                class_ids.append(class_id)
                confidences.append(float(confidence))
                boxes.append([x, y, w, h])

    indices = cv2.dnn.NMSBoxes(boxes, confidences, score_threshold=0.5, nms_threshold=0.4)
    curCoords = [[box[0] + box[2] // 2, box[1] + box[3] // 2] for i in indices for box in [boxes[i]]]

    for i in indices:
        box = boxes[i]
        x, y, w, h = box
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.putText(frame, 'Person', (x, y - 10), font, 1, (0, 255, 0), 1)

    frame = trackerHandle(curCoords, frame)

    cv2.putText(frame, f"People Count: {len(people)}", (550, 30), font, 1.5, (0, 0, 255), 2)
    cv2.imshow("Person Tracking", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
