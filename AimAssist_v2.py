import cv2 
import numpy as np
import mss
import pyautogui
import time

def scrnshot(monitor):
    
    with mss.mss() as sct:
        frame = np.array(sct.grab(monitor))
        
    return frame


def find_bar(frame):
    
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower = np.array([0,80,100])
    upper = np.array([0,255,255])
         
    mask = cv2.inRange(hsv, lower, upper)
        
    (cnts, _) = cv2.findContours(mask, cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
    cnts = sorted(cnts, key = cv2.contourArea, reverse = True)[:1]
    
    return cnts


def process(cnts,frame):
    
    for c in cnts:
        
        x,y,w,h = cv2.boundingRect(c)
        
        if h<9:
            w = int(h*8)
            cen = int((x + x+h)/2)

            draw_rect(x,y,w,h,cen,frame)
            mouse(x,y,cen,h)
            
        else:
            pass


def draw_rect(x,y,w,h,cen,frame):

    cen2 = int(cen+(w/2))
    
    cv2.rectangle(frame, (x,y), (x+w,y+h), (255,255,0), 2)
    cv2.rectangle(frame, ( cen2+20 , y+(h*2) ), ( cen+5 , y+40 ), (0,255,0), 2)

            
def mouse(x,y,cen,h):
    
    global width, height
    
    mx = (pyautogui.position().x) + x - (width/2)
    my = (pyautogui.position().y) - (height/2) +y + h*2 

    pyautogui.moveTo(mx, my,0)

def cleanup(frame):
    
    cv2.imshow('the damn window',frame)
        
    k = cv2.waitKey(1) & 0xFF
    if k == ord('q'):
        cv2.destroyAllWindows()
        quit()

    
def main():
    global width, height
    
    width = 450
    height = 450
    
    monitor = {"top" : 400, "left" : 950, "width" : width, "height" : height}

    frame = scrnshot(monitor)
    
    cnts = find_bar(frame)

    if len(cnts) > 0:
        process(cnts,frame)
        
    else:
        pass
    
    cleanup(frame)


if(__name__ == '__main__'):
    pyautogui.PAUSE = 0.05
    while True:
        fps = 0
        last_time = time.time()
        while time.time() - last_time < 1:
            main()
            fps += 1
        print(fps," : Whole Program")
