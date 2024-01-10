import cv2
import numpy as np
import os
 
img_path = 'images/withlogo/backlogo.png'
 
img = cv2.imread(img_path)
#font
font =cv2.FONT_HERSHEY_SIMPLEX
font2 =cv2.FONT_HERSHEY_COMPLEX_SMALL
#position
pos = (300,320)
#fontscale
fs= 1.5
#Color
col =(0,0,0)
#Line thickness
thick = 2

#put text
image = cv2.putText(img,'CERTIFICATE OF ACHIEVEMENT',pos,font2,fs,col,thick,cv2.LINE_AA)


image = cv2.putText(img,'THIS CERTIFICATE IS PROUDLY PRESENTED',(370,400),font,0.6,col,1,cv2.LINE_AA)
image = cv2.putText(img,'FOR HONORABLE ACHIEVEMENT TO',(400,420),font,0.6,col,1,cv2.LINE_AA)

print ("Name of the trainee")
Name = input()
image = cv2.putText(img,Name,(410,510),font,1,col,thick,cv2.LINE_AA)

print ("Issued date : ")
date = input()
image = cv2.putText(img,'AWARDED THIS DAY of '+date,(390,560),font,0.6,col,1,cv2.LINE_AA)

image = cv2.putText(img,'The Managing Director, co-CEO: ',(370,640),font,0.4,col,1,cv2.LINE_AA)
image = cv2.putText(img,'The Scientific Director, co-CEO: ',(370,700),font,0.4,col,1,cv2.LINE_AA)

image = cv2.putText(img,'Arun Sharma',(420,660),font,0.4,(0,0,200),1,cv2.LINE_AA)
image = cv2.putText(img,'Yabebal Fantaye',(420,720),font,0.4,(0,0,200),1,cv2.LINE_AA)

cv2.imwrite("images/model_certificate.png", img)
 
cv2.waitKey(0)
cv2.destroyAllWindows()
