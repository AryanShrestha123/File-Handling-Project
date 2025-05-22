from graphics import *

def triangle(x1,y1,x2,y2,x3,y3):
    win=GraphWin("Triangle",500,500)
    line1=Line(Point(x1,y1),Point(x2,y2))
    line1.draw(win)

    line2=Line(Point(x2,y2),Point(x3,y3))
    line2.draw(win)

    line3=Line(Point(x1,y1),Point(x3,y3))
    line3.draw(win)

    win.getMouse()
    win.close()

def rect(x1,y1,x2,y2):
    win=GraphWin("Rectangle",500,500)
    line1=Line(Point(x1,y1),Point(x1,y2))
    line1.draw(win)
    line2=Line(Point(x1,y1),Point(x2,y1))
    line2.draw(win)
    line3=Line(Point(x2,y2),Point(x1,y2))
    line3.draw(win)
    line4=Line(Point(x2,y2),Point(x2,y1))
    line4.draw(win)

    win.getMouse()
    win.close()

#For Triangle
# x1=float(input("Enter the x-coordinate of 1st point: "))
# y1=float(input("Enter the y-coordinate of 1st point: "))
# x2=float(input("Enter the x-coordinate of 2nd point: "))
# y2=float(input("Enter the y-coordinate of 2nd point: "))
# x3=float(input("Enter the x-coordinate of 3rd point: "))
# y3=float(input("Enter the y-coordinate of 3rd point: "))

# if x1>500 or y1>500 or x2>500 or y2>500 or x3>500 or y3>500:
#     print("Please enter values below 500")
# elif x1/y1==x2/y2==x3/y3:
#     print("Triangle can't be formed. Enter differnet values.")
# elif x1==x2==x3 or y1==y2==y3:
#     print("Triangle can't be formed. Enter differnet values.")
# elif (x1==x2 and y1==y2) or (x2==x3 and y2==y3) or (x1==x3 and y1==y3):
#     print("Triangle can't be formed. Enter differnet values.")
# else:
#     triangle(x1,y1,x2,y2,x3,y3)


#For Rectangle 
x1=float(input("Enter the x-coordinate of 1st point: "))
y1=float(input("Enter the y-coordinate of 1st point: "))
x2=float(input("Enter the x-coordinate of 2nd point: "))
y2=float(input("Enter the y-coordinate of 2nd point: "))

if x1==x2 or y1==y2:
    print("Rectangle can't be formed.")
else:
    rect(x1,y1,x2,y2)