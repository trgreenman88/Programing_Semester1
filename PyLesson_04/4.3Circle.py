print("This program will help you to find the area of a circle")
r = float(input("What is the radius of your circle in feet?"))
def setNums(r):
    global radius
    radius = r

def findArea(radius):
    return 2 * 3.14159265358979323 * radius

print("The area of a circle with a radius of" , r, "meters is" , "{:00.5f}".format(findArea(r)) , "square meters")
