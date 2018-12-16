import cv2
import numpy as np

cap = cv2.VideoCapture(0)
#fourcc = cv2.VideoWriter_fourcc(*'XVID')    #opencv 3.x
fourcc = cv2.cv.CV_FOURCC(*'XVID')          #opencv 2.4.x
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640,480))
while (1):
    _, frame = cap.read()
    out.write(frame)
    cv2.imshow('renk takibi', frame)
    if cv2.waitKey(25) & 0xFF ==27:
         break
cap.release()
out.release()
cv2.destroyAllWindows()
