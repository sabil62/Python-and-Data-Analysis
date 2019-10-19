'''SEE the webcam flashes light'''
import cv2,time

video = cv2.VideoCapture(0)
check,frame = video.read()

print(check)
print(frame)
time.sleep(3)#the webcam glows for 3sec
video.release()
