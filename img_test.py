import cv2

im = cv2.imread("test_img.jpg", cv2.IMREAD_GRAYSCALE)
im = cv2.resize(im, (40,40))
print(im)
cv2.imshow("new", im)
cv2.waitKey(0) 
  
#closing all open windows 
cv2.destroyAllWindows() 