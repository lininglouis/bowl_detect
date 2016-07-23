import cv2

def img_show(name,img):
    
    if len(img.shape) == 2:   # if gray image, convert to colorful image
        img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)

    cv2.imshow(name, img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
# read and show image    
img = cv2.imread('bowl2.jpg')
img_show('',img)

# convert to gray image
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 

# detect all circles
circle_list = cv2.HoughCircles(image = img_gray, method = cv2.cv.CV_HOUGH_GRADIENT,\
                               dp =1, minDist=20, minRadius = 10 )

# draw circles on the image
img_cp = img.copy()
for i in circle_list[0]:
    # draw the outer circle
    cv2.circle(img_cp,(i[0],i[1]),i[2],(0,0,255),2)
    # draw the center of the circle
    cv2.circle(img_cp,(i[0],i[1]),2,(0,255,0),3)
    
# show image with detected cirles    
img_show('',img_cp)
cv2.imwrite('deteced_circle.jpg',img_cp)

