import cv2
# image is rgb
img = cv2.imread('shapes1.jpg')
# convert rgb image into grayscale image
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY);
# selecting the font to be displaced on the element in the image
font = cv2.FONT_HERSHEY_COMPLEX_SMALL 
# selecting the threshold which will show binary version of image
""" Value of pixels is explained below 
0 means black pixel
255 means white pixel
245: Values below 245 means black
255: Value above 245 means white
# one can tweak these values for better threshold image
"""
_, threshold = cv2.threshold(img, 245, 255, cv2.IMREAD_GRAYSCALE)
# drawing contour on each shape in the image
contours,_ = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
# loop contour
for cnt in contours:
	approx = cv2.approxPolyDP(cnt, 0.038*cv2.arcLength(cnt, True), True)
	# drawing the contour on each shape
	cv2.drawContours(img, [approx], 0, (0), 5)
	# calculating the x and y coordinate of shape
	# this is used to fidn the location on image to write text
	x_coordinate = approx.ravel()[0]
	y_coordinate = approx.ravel()[1]
	# defining length for various shapes in the image
	if len(approx) == 3:
		cv2.putText(img, "Traingle", (x_coordinate, y_coordinate), font, 1, (0))
	elif len(approx) == 8:
		cv2.putText(img, "Octagen", (x_coordinate, y_coordinate), font, 1, (0))
	elif len(approx) == 5:
		cv2.putText(img, "Pentagen", (x_coordinate, y_coordinate), font, 1, (0))	
	elif len(approx) == 10:
		cv2.putText(img, "Star", (x_coordinate, y_coordinate), font, 1, (0))	
	elif len(approx) == 4:
		(x, y, w, h) = cv2.boundingRect(approx)
		# if width and heigh are same it is square else rectangle
		if  ((float(w)/h)==1):
			cv2.putText(img, "Square", (x_coordinate, y_coordinate), font, 1, (0))
		else:
			cv2.putText(img, "Rectangle", (x_coordinate, y_coordinate), font, 1, (0))	

# showing the original image
cv2.imshow("Original Image", img)
# showing the binary image based on threshold
cv2.imshow("Binary Image", threshold)
# wait for 4 seconds
k = cv2.waitKey(4000) & 0xFF
cv2.destroyAllWindows()
