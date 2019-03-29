import cv2 
import numpy as np
import mss
import pyautogui
  

with mss.mss() as sct:
    monitor = {"top": 400, "left": 950, "width": 450, "height": 450}
    while True:
        frame = np.array(sct.grab(monitor))
        
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        
        lower = np.array([0,80,100])
        upper = np.array([0,255,255])
         
        mask = cv2.inRange(hsv, lower, upper)
        (cnts, _) = cv2.findContours(mask, cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
        cnts = sorted(cnts, key = cv2.contourArea, reverse = True)[:1]
        for c in cnts:
            x,y,w,h = cv2.boundingRect(c)
            w= h*8
            cen = int((x + x+h)/2)
            cen2 = int(cen+(w/2))
            cv2.rectangle(frame, (x,y), (x+w,y+h), (255,255,0), 2)
            cv2.rectangle(frame, (cen2+20,y+int(h*2/1.001)), (cen+5,y+40), (0,255,0), 2)
            #pyautogui.moveTo(pyautogui.position().x+cen-225+30, (pyautogui.position().y)+y-225+int(260/h))
            pyautogui.moveTo(pyautogui.position().x+cen-225+30, (pyautogui.position().y)+y-225+50)
            #print(str(h)+" "+str(w))
        cv2.imshow('the damn window',frame)
        
        k = cv2.waitKey(1) & 0xFF
        if k == ord('q'):
            cv2.destroyAllWindows()
            quit()
            break


          