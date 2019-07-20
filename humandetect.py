# -*- coding: utf-8 -*-
import cv2
<<<<<<< HEAD
#import sys
=======
import sys
>>>>>>> cb2c3081e5e98c9a8844f1230711180789e302ee
#import paho.mqtt.client as mqtt

#client = mqtt.Client()
#client.connect("192.168.100.3", 1883)


x=0
y=0

cascPath = "haarcascade_fullbody.xml"
faceCascade = cv2.CascadeClassifier(cascPath)
font=cv2.FONT_HERSHEY_SIMPLEX
video_capture = cv2.VideoCapture(1)
#video_capture = cv2.VideoCapture("movie.avi")

while True:
    # CAPTURE FRAME-BY-FRAME
    ret, frame = video_capture.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(50, 50),)
    # DRAW A RECTANGLE AROUND THE FACES FOUND
    if len(faces) >= 1:
     print "Face detect"
     cv2.putText(img = frame, text = 'Body found:' + str(len(faces)), org=(50,50), fontFace=cv2.FONT_HERSHEY_DUPLEX, fontScale=1, color=(0, 0, 255))
     #system("echo  '%s %s' > data.txt" % (len(faces_rects), 1 ))
 #    client.publish("home/sala/porta/01/status/"," 1 ")
     for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 100), 1)

        #---To write the x,y on the middle of the rectangle.
        stringxy="+%s,%s"%(x,y) # To prepare the string with the xy values to be used with the cv2.putText function
        #In the case we want to put Xxvalue,Yyvalue we can use the following line removing #.
<<<<<<< HEAD
        #stringaxy="X%s,Y%s"%(x,y)
=======
        #fig
        stringaxy="X%s,Y%s"%(x,y) 
>>>>>>> a08c72c142c1f4a2b77d3f347287d4f6754fd961
        cv2.putText(frame,stringxy,(x+w/2,y+h/2),font, 1,(0,0,255),1)
        cv2.imwrite('people.jpg', frame)

    else:
<<<<<<< HEAD
        print "Not body "
  #      client.publish("home/sala/porta/01/status/"," 0 ")
        cv2.imwrite('body.jpg', frame)
=======
        print "Not face "
<<<<<<< HEAD
 #       client.publish("home/sala/porta/01/status/"," 0 ")
=======
  #      client.publish("home/sala/porta/01/status/"," 0 ")
>>>>>>> cb2c3081e5e98c9a8844f1230711180789e302ee
        cv2.imwrite('face.jpg', frame)
>>>>>>> a08c72c142c1f4a2b77d3f347287d4f6754fd961
    # DISPLAY THE RESULTING FRAME
    cv2.imshow('Video', frame)
    print x,y,
    print"\n"
    font=cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(faces,'x,y',(x,y),font, 2,(255,255,255),1)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything is done, release the capture
video_capture.release()
cv2.destroyAllWindows()