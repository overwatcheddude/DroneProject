from utlis import *
import cv2
import time
import sys
import pynput
import keyboard

w,h = 360,240
#PID      Kp    Ki   Kd
pidYaw = [0.5,  0.5, 0]
pidFB  = [0.01, 0.5, 0]
pidUD  = [0.5,  0.5, 0]

pError = 0
startCounter = 0 # to takeoff 0 , for no flying
save = False
timer = time.time()

#-------------------------
myDrone = IntializeTello()
eq
while True:
    

    img = telloGetFrame(myDrone,w ,h)
    img, info = findFace(img)
    cv2.imshow("image",img)
    


    #if cv2.waitKey(1) & 0xFF == ord("s"):
        #save = True

    if (save == True and info[0][0] != 0 ):
        saveImage(info, img)
        save = False

    #if cv2.waitKey(1) & 0xFF == ord("q"):
        #myDrone.land()
    
    if keyboard.is_pressed('e'):
        print("forward")
        myDrone.takeoff()

    if keyboard.is_pressed('q'):
        print("land drone")
        myDrone.land()


cv2.destroyAllWindows()
myDrone.streamoff()