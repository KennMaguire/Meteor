#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3

import time
from graphics import *
from PIL import Image as Im
import struct

with open("images/BigEarth.gif", "rb") as fhandle:         #https://stackoverflow.com/questions/8032642/how-to-obtain-image-size-using-standard-python-class-without-using-external-lib
    head = fhandle.read(24)
    print(head)
    width,height = struct.unpack("<HH", head[6:10])  #get width and height using struct, width = 1024, height = 512


print(width)
print(height)

win = GraphWin('Map',width, height)

pt = Point(100,50)



myImage = Image(Point((width/2),(height/2)), "images/BigEarth.gif")
ratioLong = width/360
ratioLat = height/180

myImage.draw(win)           #draw the image in the window

for i in range(0, 360, 10):
    longLine = Line(Point((i*ratioLong),0), Point((i*ratioLong),height))
    longLine.setOutline("#3890e2")
    longLine.setWidth(.01)
    longLine.draw(win)


for i in range(0, 180, 10):
    latLine = Line(Point(0,(i*ratioLat)), Point(width, (i*ratioLat)))
    latLine.setOutline("#3890e2")
    latLine.setWidth(1)
    latLine.draw(win)

cir = Circle(Point(500,100),5)
cir.setFill("blue")
cir.draw(win)

win.getMouse()
win.close()
