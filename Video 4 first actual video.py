import cv2

video = cv2.VideoCapture(0)
a = 1


while True:
    a = a+1
    check, frame = video.read()
    cv2.imshow('Capturing video lol.......',frame)
    key = cv2.waitKey(1)
    
    if key == ord('q'):
        break


video.release()
cv2.destroyAllWindows