import cv2
path="im.jpg"
img= cv2.imread(path,0)
cv2.imshow("im",img)
cv2.waitKey(0)