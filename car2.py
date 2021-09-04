import cv2
import sys

imagePath = sys.argv[1]


faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_car.xml')

#print(f"face: {faceCascade}")


image = cv2.imread(imagePath)
#print(f"img: {image}")    

#if image == None: 
#    raise Exception("could not load image !")


gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#gray = cv2.equalizeHist(gray)
#print(f"gray: {gray}")



faces= faceCascade.detectMultiScale( image) 

print("I found {0} cars!".format(len(faces)))

for(x,y,w,h) in faces:
	cv2.rectangle(image, (x,y), (x+w, y+h), (33,255,0), 2)
	
cv2.imshow("Faces Found", image)
cv2.waitKey(0)
