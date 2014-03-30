from PIL import Image
land = Image.open("land.jpg")
width, height = land.size
land = land.load()
totalarea = 0
#249 238 114
print "Starting..."
for y in xrange(height):
    for x in xrange(width):
    	pixel = land[x,y]
    	if pixel[0] > 222 and pixel[0] < 262 and pixel[1] > 214 and pixel[1] < 254 and pixel[2] > 113 and pixel[2] < 153:
    		totalarea = totalarea+1
    	if pixel[0] > 228 and pixel[1] < 26 and pixel[2] < 24:
    		totalarea = totalarea+1
print totalarea * .1
print "DONE"
