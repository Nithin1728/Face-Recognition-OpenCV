import cv2

#randrange is for selecting the color of the rectangle randomly from BGR 
from random import randrange


#load some pretrained data on face frontals from opencv(haar cascade algorithm)
trained_face_data = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

#chose an image to detect faces in
#the below line of code is for testing with an image so ive commented it after it worked 

#imread reads the image

#img = cv2.imread('crap.jpg')


#detecting using webcam

webcam = cv2.VideoCapture(0 , cv2.CAP_DSHOW)


#iterate forever for frames
while True:
	successful_frame_read , frame = webcam.read()



#convert the image to grayscale 
	gray_img = cv2.cvtColor(frame , cv2.COLOR_BGR2GRAY)


	#detect faces
	face_coordinates = trained_face_data.detectMultiScale(gray_img)



#draw a rectangle around the faces
#258 is the top left coordinate and 85 is bottom right (x , y)
#224 is the width and height  and we need to add the x and y coordinates to get desired rectangle for the face
	for (x , y , w , h) in face_coordinates:
		cv2.rectangle(frame , (x ,y) , (x+w ,y+h) , (0 , 255 , 0) , 2)




	cv2.imshow('Lenovo EasyCamera' , frame)
	key = cv2.waitKey(1)


	#Stop the cam if Q is pressed  
	if key == 81 or key == 113:
		break


webcam.release()




#this line is just to print the statement to check the code worked fine
print("Code completed")


