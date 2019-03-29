import pyautogui
import os
import os.path
import cv2
import time
import numpy
import mss

def screenshot():

    with mss.mss() as sct:
        monitor = {"top": 400, "left": 950, "width": 450, "height": 450}
        #monitor = {"top": 0, "left": 0, "width": 1600, "height": 1200}
        x = 225
        h = 225 
        y = 225
        previous_x = 225
        while True:
            img2 = numpy.array(sct.grab(monitor))
            img = cv2.cvtColor(img2, cv2.COLOR_BGRA2GRAY)
            ret,img = cv2.threshold(img,240,255,cv2.THRESH_BINARY)
            img = cv2.blur(img,(4,4))
            (cnts, _) = cv2.findContours(img, cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
            cnts = sorted(cnts, key = cv2.contourArea, reverse = True)[:1]
            for c in cnts:
                x,y,w,h = cv2.boundingRect(c)
                cv2.rectangle(img2, (x,y), (x+w,y+h), (255,255,0), 2)
            cv2.imshow("frame", img2)
            average_x = (x + x+h)/2
            if x == previous_x:
                pass
            elif w/h < 1.3:
                pass
            elif w*h <= 100:
                pass
            else:
                pyautogui.moveTo(pyautogui.position().x+average_x-225+30, (pyautogui.position().y)+y-225+50)
            x = previous_x

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

def main():
    screenshot()


main()








#450,450
#225,225


    #params = cv2.SimpleBlobDetector_Params()
    
    #params.filterByArea = True
    #params.minArea = 20
    #params.maxArea = 400

    
    #detector = cv2.SimpleBlobDetector_create(params)


            #kp = detector.detect(img)
            #for marker in kp:
            #try:
                #marker = kp[0]
                #img = cv2.drawMarker(img, tuple(int(i) for i in marker.pt), color=(0, 0, 255))
                #pyautogui.moveTo((pyautogui.position().x+marker.pt[0]-225-40), (pyautogui.position().y+marker.pt[1]-225+90))
                #cv2.imshow('frame',img)
            #except:
                #pyautogui.moveTo(pyautogui.position().x, (pyautogui.position().y))
                #cv2.imshow('frame',img)
            #time.sleep(0.5)
