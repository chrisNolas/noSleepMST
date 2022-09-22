import pyautogui as maus
import time

def muvMaus():
    global pivotPoint
    time.sleep(500)
    currentPoint = maus.position()
    if (pivotPoint == currentPoint):
        maus.moveRel(0,1, duration=1)
        maus.leftClick()
        pivotPoint = maus.position()
        muvMaus()
    else:
        pivotPoint = maus.position()
        muvMaus()


pivotPoint = maus.position()
muvMaus()