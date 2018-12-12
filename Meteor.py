#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3

import time
from graphics import *
from PIL import Image as Im
import struct
import csv
import math



#https://stackoverflow.com/questions/10759117/converting-jpg-images-to-png was used to convert my image, but the code is no longer needed for my program

with open("images/BigEarth.gif", "rb") as fhandle:         #https://stackoverflow.com/questions/8032642/how-to-obtain-image-size-using-standard-python-class-without-using-external-lib
    head = fhandle.read(24)
    print(head)
    width,height = struct.unpack("<HH", head[6:10])  #get width and height using struct, width = 1024, height = 512


print(width)
print(height)

win = GraphWin('Map',width, height)

pt = Point(100,50)

locMass = []
with open('data/meteorite-landings.csv', 'r') as metFile:
    next(metFile)
    metReader = csv.reader(metFile, skipinitialspace = True, delimiter=',', quotechar = '"')
    for row in metReader:
        #geolocation @ 9, mass @ 4
        #https://bytes.com/topic/python/answers/45526-convert-string-tuple
        if row[4] != "" and row[4] != "0" and row[9] != "" and row[9] != "(0.000000, 0.000000)":
            mass = float(row[4])
            fall = row[5]
            geo = row[9]
            geo = tuple(map(float, geo[1:-1].split(",")))

            locMass.append((geo, mass, fall))  #new list, geolocation @ 1, mass @ 2

myImage = Image(Point((width/2),(height/2)), "images/BigEarth.gif")         #https://stackoverflow.com/questions/19249859/importing-custom-images-into-graphics-py
ratioLong = width/360
ratioLat = height/180
print(ratioLong)
print(ratioLat)
myImage.draw(win)           #draw the image in the window


#plot longitude lines
for i in range(0, 360, 10):
    if i != 0:
        longLine = Line(Point((i*ratioLong),0), Point((i*ratioLong),height))
        longLine.setOutline("#3890e2")
        longLine.setWidth(1)
        if i == 180:
            longLine.setWidth(3)        #prime meridian is bold
        longLine.draw(win)

#plot latitude lines
for i in range(0, 180, 10):
    if i != 0:
        latLine = Line(Point(0,(i*ratioLat)), Point(width, (i*ratioLat)))
        latLine.setOutline("#3890e2")
        latLine.setWidth(1)
        if i == 90:
            latLine.setWidth(3) #equator is bold
        latLine.draw(win)
#total = 0
#plot points on the map
print("Plotting data")
for i in locMass:                                           #adding 180 to long, and 90 to lat since measurements in my space are from 0 to 360 and 0 to 180
    lat = height - (((i[0][0] + 90) * (ratioLat)))      #have to subtract from height since pixel 0,0 is in the top left, and coordinates work for bottom left position
    long = ((i[0][1] + 180) * (ratioLong))
    #print((long,lat))
    size = math.log(i[1],8)                     #using log8 for appropriate scaling
    #print(size)
    if(size < 2):
        size = 2
    cir = Circle(Point(long, lat), size)        #Point holds coordinates, size is the size of the circle
    if i[2] == "Fell":
        cir.setOutline("#6c7287")
        cir.setFill("red")
    elif i[2] == "Found":
        cir.setOutline("#6c7287")
        cir.setFill("#45cb06")
    else:
        cir.setOutline("white")
        cir.setFill("#1cba5b")
    #total += 1
    #print(total)
    cir.draw(win)

print("Finished Plotting")

win.getMouse()
win.close()
