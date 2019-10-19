import cv2

img =  cv2.imread('wlop5.jpg')
    #print(img)  prints matrices of rgb colors
    
#to display image
#cv2.imshow('Image',img)
#cv2.waitKey(0)
#cv2.destroyAllWindows

#Resizing image
height = int(img.shape[1]/3)
width = int(img.shape[0]/3)    
resized_img = cv2.resize(img, (int(img.shape[1]/3), int(img.shape[0]/3)) )

#you will find new .jpg file in folder 
cv2.imwrite('wlop5_New.jpg',resized_img)