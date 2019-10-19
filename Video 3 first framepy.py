import cv2,time

video = cv2.VideoCapture(0)
check,frame = video.read()
print(check)

time.sleep(2)

cv2.imshow('The first image',frame)
cv2.waitKey(0)
cv2.destroyAllWindows
video.release()