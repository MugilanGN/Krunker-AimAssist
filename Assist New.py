import cv2 
import numpy as np
import mss
import pyautogui
#from DirectKeys import PressKey, ReleaseKey, C, left_click
import time
#from threading import Thread

with mss.mss() as sct:
    
    width = 450
    height = 450
    
    monitor = {"top": 400, "left": 950, "width": width, "height": height}
    
    while True:
        
        frame = np.array(sct.grab(monitor))
        
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        
        lower = np.array([0,80,100])
        upper = np.array([0,255,255])
         
        mask = cv2.inRange(hsv, lower, upper)
        
        (cnts, _) = cv2.findContours(mask, cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
        cnts = sorted(cnts, key = cv2.contourArea, reverse = True)[:1]
        
        if len(cnts) > 0:
            for c in cnts:
                
                x,y,w,h = cv2.boundingRect(c)
                if h<9:
                
                    w= int(h*8.5)
                    
                    cen = int((x + x+h)/2)
                    cen2 = int(cen+(w/2))
                    
                    cv2.rectangle(frame, (x,y), (x+w,y+h), (255,255,0), 2)
                    cv2.rectangle(frame, ( cen2+20 , y+(h*2) ), ( cen+5 , y+40 ), (0,255,0), 2)
                    
                    mx = (pyautogui.position().x) + cen - (width/2) + 20
                    my = (pyautogui.position().y) + y+(h*2) - (height/2) + 15

                    pyautogui.moveTo(mx, my)
                    
                    #Thread(target = PressKey, args=([C])).start()
                    #time.sleep(0.03)
                    #Thread(target = left_click).start()
                    
                    #PressKey(C)
                    #left_click()

                    
                else:
                    #ReleaseKey(C)
                    pass
        else:
            #ReleaseKey(C)
            pass
        cv2.imshow('the damn window',frame)
        
        k = cv2.waitKey(1) & 0xFF
        if k == ord('q'):
            cv2.destroyAllWindows()
            quit()
            break


#check height>8 or something
#look for white uptop

























          
#pyautogui.moveTo(pyautogui.position().x+cen-225+30, (pyautogui.position().y)+y-225+int(260/h))
        
            #my = (pyautogui.position().y) + (( ( y+int(h*2) ) + ( y+int(h*2) + y+40 ) ) / 2) -225 - 50
            #mx = (pyautogui.position().x) + ((cen2+20 + cen+5) / 2) - 225 + 20
