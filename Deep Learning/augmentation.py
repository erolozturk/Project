import cv2
import numpy as np

def augment_brightness(image):
	image1 = cv2.cvtColor(image,cv2.COLOR_BGR2HSV) 
	image1 = np.array(image1, dtype = np.float64)
	random_bright = 0.5+np.random.uniform()
	image1[:,:,2] = image1[:,:,2]*random_bright
	image1[:,:,2][image1[:,:,2]>255]  = 255
	image1 = np.array(image1, dtype = np.uint8)
	image1 = cv2.cvtColor(image1,cv2.COLOR_HSV2RGB)
	return image1

image=cv2.imread("2.jpg")

for i in range(10):
	yeni=augment_brightness(image)
	cv2.imshow("frame", yeni)
	cv2.waitKey(0)
cv2.destroyAllWindows()


