import cv2
print(cv2.__version__)
import urllib
import time
cascade_src = 'cars.xml'
car_cascade = cv2.CascadeClassifier(cascade_src)
while True:
    resource = urllib.urlopen("http://tpark-cam.cs.aalto.fi/picture.jpg")
    output = open("picture.jpg","wb")
    output.write(resource.read())
    output.close()
    img = cv2.imread("picture.jpg")
    if (type(img) == type(None)):
        break
    
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    cars = car_cascade.detectMultiScale(gray, 1.1, 1)
    for (x,y,w,h) in cars:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)      
    
    cv2.imshow('video', img)
    
    if cv2.waitKey(33) == 27:
        break
    time.sleep(0.2)
cv2.destroyAllWindows()
