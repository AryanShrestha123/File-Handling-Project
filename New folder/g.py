from graphics import *
from graphics import *

# def graphics(dict1, dict2, window_width=1000, window_height=500):
#     # Create a window
#     win = GraphWin("Histogram Comparison", window_width, window_height)

#     # Extract keys and values
#     keys = list(dict1.keys())
#     values1 = list(dict1.values())
#     values2 = list(dict2.values())

#     # Number of keys
#     num_keys = len(keys)

#     # Calculate bar width and scaling factor
#     bar_group_width = window_width / num_keys
#     bar_width = bar_group_width / 3  # Space for each bar, leaving room between groups
#     max_value = max(max(values1), max(values2))
#     scale_factor = window_height / max_value

#     # Plot the bars
#     for i, key in enumerate(keys):
#         x_center = i * bar_group_width + bar_group_width / 2

#         # First dictionary bar
#         x1_1 = x_center - bar_width
#         x2_1 = x_center
#         y1_1 = window_height
#         y2_1 = window_height - values1[i] * scale_factor
#         rect1 = Rectangle(Point(x1_1, y1_1), Point(x2_1, y2_1))
#         rect1.setFill("blue")
#         rect1.draw(win)

#         # Second dictionary bar
#         x1_2 = x_center
#         x2_2 = x_center + bar_width
#         y1_2 = window_height
#         y2_2 = window_height - values2[i] * scale_factor
#         rect2 = Rectangle(Point(x1_2, y1_2), Point(x2_2, y2_2))
#         rect2.setFill("green")
#         rect2.draw(win)

#         # Add key labels
#         label = Text(Point(x_center, window_height - 10), str(key))
#         label.draw(win)

#     # Wait for user click to close
#     win.getMouse()
#     win.close()



def graphics(d1,d2):
    win=GraphWin("Program",1000,500)
    win.setBackground("white")

    hours=list(d1.keys())
    j1_values=list(d1.values())
    j2_values=list(d2.values())
    max_hieght=500-100-50
    max_value=max(max(j1_values),max(j2_values))
    scale_factor=max_hieght/max_value

    aLine=Line(Point(70,450),Point(930,450))
    aLine.draw(win)
    line_width=1000-70-70
    bar_group_width=line_width/len(hours)
    bar_width=bar_group_width/3
    for i in range(len(hours)):
        x_center = 70+i*bar_group_width+bar_group_width/2
        #First dictionary bar
        x1_1 = x_center-bar_width
        y1_1 = 450
        x2_1 = x_center
        y2_1 = 450 - j1_values[i] * scale_factor
        r1=Rectangle(Point(x1_1,y1_1),Point(x2_1,y2_1))
        r1.setFill("lightblue")
        r1.draw(win)
        v1_text=Text(Point(x_center-(bar_width/2),y2_1-5),j1_values[i])
        v1_text.setSize(7)
        v1_text.setFill("blue")
        v1_text.draw(win)

        #Second dictionary bar
        x1_2 = x_center
        y1_2=450
        x2_2=x_center+bar_width
        y2_2=450-j2_values[i]*scale_factor
        r2=Rectangle(Point(x1_2,y1_2),Point(x2_2,y2_2))
        r2.setFill("lightgreen")
        r2.draw(win)
        v2_text=Text(Point(x_center+(bar_width/2),y2_2-5),j2_values[i])
        v2_text.setSize(7)
        v2_text.setFill("green")
        v2_text.draw(win)

        # v1_text=Text(Point(x_center-(bar_width/2),y2_1+5))
        h_text1=Text(Point(x_center,460),hours[i])
        h_text1.setSize(8)
        h_text1.draw(win)

    header=Text(Point(250,15),"Histogram of vehicle frequency per hour (21/06/2024)")
    header.setStyle("bold")
    header.draw(win)

    c1_box=Rectangle(Point(50,30),Point(60,40))
    c1_box.setFill("lightblue")
    c1_box.draw(win)
    j1_name=Text(Point(135,35),"Elm Avenue/ Rabbit Road")
    j1_name.setSize(9)
    j1_name.draw(win)

    c2_box=Rectangle(Point(50,45),Point(60,55))
    c2_box.setFill("lightgreen")
    c2_box.draw(win)
    j2_name=Text(Point(135,50),"Hanley Highway/ Westway")
    j2_name.setSize(9)
    j2_name.draw(win)

    h_text2=Text(Point(500,480),"Hours 00:00 to 24:00")
    h_text2.setSize(10)
    h_text2.draw(win)


    win.getMouse()
    win.close()


d1={'00': 11, '01': 9, '02': 15, '03': 19, '04': 9, '05': 15, '06': 17, '07': 27, '08': 74, '09': 59, '10': 26, '11': 25, '12': 27, '13': 33, '14': 25, '15': 11, '16': 17, '17': 52, '18': 74, '19': 34, '20': 26, '21': 21, '22': 11, '23': 14}
d2={'00': 14, '01': 18, '02': 18, '03': 17, '04': 9, '05': 19, '06': 22, '07': 28, '08': 59, '09': 52, '10': 31, '11': 21, '12': 30, '13': 31, '14': 26, '15': 11, '16': 21, '17': 57, '18': 71, '19': 36, '20': 28, '21': 18, '22': 18, '23': 28}

graphics(d1,d2)