##Following are the two methods which can be used to access the webcam connected to your syatem.

import cv2
# cam = cv2.VideoCapture(0)
# while cam.isOpened():
#     ret , frame = cam.read()
#     # ret , frame2 = cam.read()
#     #diff =
#     if cv2.waitKey(10) == ord('q'):
#         break
#     cv2.imshow("camera" , frame)

#secondway

cap = cv2.VideoCapture(0)
# cap.set()

while True:
    frame , img = cap.read()
    if cv2.waitKey(10) & 0xFF ==ord('q'):
        break
    cv2.imshow("camera" , img )
