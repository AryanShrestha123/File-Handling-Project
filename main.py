"""
****************************************************************************
Additional info
 1. I declare that my work contins no examples of misconduct, such as
 plagiarism, or collusion.
 2. Any code taken from other sources is referenced within my code solution.
 3. Student ID: w2083987 
 4. Date: 11/29/2024
****************************************************************************
"""
from graphics import *

#Function to check if the given input is valid
def input_validity(user_input,l_range,u_range):
    if user_input.isdigit():
        if l_range<=int(user_input)<=u_range:
            return "Valid"
        else:
            print(f"Out of range - values must be in the range {l_range} and {u_range}.")
            return "Invalid"
    else:
        print("Integer required")
        return "Invalid"

#Function to get user input and validate it
def date_input():
    validity="Invalid"
    while validity!="Valid":
        dd=input("Please enter the day of the survey in the format dd: ")
        if len(dd)<2:
            dd="0"+dd
        validity=input_validity(dd,1,31)
    print()
    
    validity="Invalid"
    while validity!="Valid":
        mm=input("Please enter the day of the survey in the format MM: ")
        if len(mm)<2:
            mm="0"+mm
        validity=input_validity(mm,1,12)
    print()

    validity="Invalid"
    while validity!="Valid":
        yy=input("Please enter the day of the survey in the format YYYY: ")
        validity=input_validity(yy,2000,2024)
    print()
    user_date=dd+mm+yy
    return user_date

#Function to ask user if they want to select another date
def repeat_loop():
    while True:
        repeat=input("""\nDo you want to select another data file for a different date?
Enter 'Y' or 'N': """)
        if repeat.lower()=="y" or repeat.lower()=="n" or repeat.lower()=="yes" or repeat.lower()=="no":
            return repeat
        else:
            print("Please enter 'Y' or 'N'.\n")

#Function to show histogram
def histogram(j1_hour_dict,j2_hour_dict,formatted_date):
    win=GraphWin("Histogram",1000,500)    #Creates a window
    win.setBackground("white")

    hours=list(j1_hour_dict.keys())
    j1_values=list(j1_hour_dict.values())
    j2_values=list(j2_hour_dict.values())
    max_hieght=500-100-50    #Separating 100 units above and  50 units below the histogram
    max_value=max(max(j1_values),max(j2_values))  #Calculating highest value of both lists
    scale_factor=max_hieght/max_value    #Caluclating scale sector 

    bottom_line=Line(Point(70,450),Point(930,450))   #Creates a base line for the bars(leaving 70 units behind and after)
    bottom_line.draw(win)
    bottom_text=Text(Point(500,480),"Hours 00:00 to 24:00")
    bottom_text.setSize(10)
    bottom_text.draw(win)

    vertical_line=Line(Point(70,450),Point(70,100))  #Creates a vertical line(leaving 100 units above and 50 units after)
    vertical_line.draw(win)
    vertical_text=Text(Point(35,275),"Frequency\nof\nVehicles")
    vertical_text.setSize(10)
    vertical_text.draw(win)

    line_width=1000-70-70    #Width of base line (total width-space on left-space on right)
    bar_group_width=line_width/len(hours)    #Width of one bar group (including space required for another bar group)
    bar_width=bar_group_width/3        #Width of single bar (also of space)
    
    #Using for loop to plot the bars
    for i in range(len(hours)):
        x_center = 70+i*bar_group_width+bar_group_width/2       #Center of each bar_group
        #First dictionary bar
        x1_rect1=x_center-bar_width     
        y1_rect1=450
        x2_rect1=x_center
        y2_rect1=450-j1_values[i]*scale_factor
        bar1=Rectangle(Point(x1_rect1,y1_rect1),Point(x2_rect1,y2_rect1))
        bar1.setFill("lightblue")
        bar1.draw(win)
        bar1_text=Text(Point(x_center-(bar_width/2),y2_rect1-5),j1_values[i])  #Creates text just above the bar indicating the frequency of that bar
        bar1_text.setSize(7)
        bar1_text.setFill("blue")
        bar1_text.draw(win)

        #Second dictionary bar
        x1_rect2=x_center
        y1_rect2=450
        x2_rect2=x_center+bar_width
        y2_rect2=450-j2_values[i]*scale_factor
        bar2=Rectangle(Point(x1_rect2,y1_rect2),Point(x2_rect2,y2_rect2))
        bar2.setFill("lightgreen")
        bar2.draw(win)
        bar2_text=Text(Point(x_center+(bar_width/2),y2_rect2-5),j2_values[i])
        bar2_text.setSize(7)
        bar2_text.setFill("green")
        bar2_text.draw(win)

        hour_text=Text(Point(x_center,460),hours[i])   #Creates text(hour) below each bar group 
        hour_text.setSize(8)
        hour_text.draw(win)

    header=Text(Point(250,15),f"Histogram of vehicle frequency per hour ({formatted_date})")
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

    win.getMouse()
    win.close()

#Function to read the selected file and print required output
def read_file(file_name,content):
    content.pop(0)
    print("*"*20)
    print(f"The data file selected is {file_name}")
    print("*"*20)
    print(f"The total number of vehicles recorded for this date is {len(content)}\n")
    vehicle_type=list()
    e_vehicle_count=0
    no_turn_count=0
    j1_hour_dict=dict()
    j2_hour_dict=dict()
    peak_hours=[]
    rain_dict=dict()

    b_leaving_n=0
    overspeed_count=0
    j1_vehicle_count=0
    j2_vehicle_count=0
    j1_scooter_count=0
    
    for data in content:
        splitted_data=data.split(",")
        vehicle_type.append(splitted_data[-2])
        if splitted_data[-1].strip("\n")=="True":
            e_vehicle_count+=1
        
        if int(splitted_data[-3])>int(splitted_data[-4]):
            overspeed_count+=1
        
        if splitted_data[0] == "Elm Avenue/Rabbit Road":
            j1_vehicle_count+=1
            hour=splitted_data[2].split(":")[0]
            if hour in j1_hour_dict.keys():
                j1_hour_dict[hour]+=1
            else:
                j1_hour_dict[hour]=1
            if splitted_data[4] == "N" and splitted_data[-2] == "Buss":
                b_leaving_n+=1
            if splitted_data[-2]=="Scooter":
                j1_scooter_count+=1
        else:
            j2_vehicle_count+=1
            hour=splitted_data[2].split(":")[0]
            if hour in j2_hour_dict.keys():
                j2_hour_dict[hour]+=1
            else:
                j2_hour_dict[hour]=1
        
        if splitted_data[3]==splitted_data[4]:
            no_turn_count+=1
            
        if splitted_data[-5]=="Heavy Rain" or splitted_data[-5]=="Light Rain":
            rain_hour=splitted_data[2].split(":")[0]
            rain_dict[rain_hour]=1     #Appends 1 as value for each hour of rain in a dictionary so that the hour is not repeated.


    truck_count=vehicle_type.count("Truck")
    truck_percent=round((truck_count/len(vehicle_type))*100)
    two_wheeled_count=vehicle_type.count("Bicycle")+vehicle_type.count("Motorcycle")+vehicle_type.count("Scooter")
    bicycle_count=vehicle_type.count("Bicycle")
    bicycle_per_hr=round(bicycle_count/24)
    j1_scooter_percent=round(j1_scooter_count/j1_vehicle_count*100)
    peakhour_vehicle_count=max(j2_hour_dict.values())
    for key,value in j2_hour_dict.items():
        if value==peakhour_vehicle_count:
            peak_hours.append(key)

    print(f"The total number of trucks recorded for this data is {truck_count}")
    print(f"The total number of electric vehicles recorded for this data is {e_vehicle_count}")
    print(f"The total number of two-wheeled vehicles recorded for this data is {two_wheeled_count}")
    print(f"The total number of busses leaving Elm Avenue/Rabbit Road junction heading north is {b_leaving_n}")
    print(f"The total number of vehicles through both junctions not turning left or right is {no_turn_count}\n")
    print(f"The percentage of total vehicles recorded that are truck for this date is {truck_percent}%")
    print(f"The average number of bikes per hour for this date is {bicycle_per_hr}\n")
    print(f"The total number of vehicles recorded as over the speed limit for this date is {overspeed_count}\n")
    print(f"The total number of vehicles recorded through Elm Avenue/Rabbit Road junction is {j1_vehicle_count}")
    print(f"The total number of vehicles recorded through Hanley Highway/Westway junction is {j2_vehicle_count}\n")
    print(f"{j1_scooter_percent}% of vehicles recorded through Elm Avenue/Rabbit Road are scooters.\n")
    print(f"The highest number of vehicles in an hour on Hanley Highway/Westway is {peakhour_vehicle_count}")
    if len(peak_hours)<2:
        end_time=int(peak_hours[0])+1
        line_peakhour=f"The most vehicles through Hanley Highway/Westway was between {peak_hours[0]}:00 and {end_time}:00"
    else:
        line_peakhour=f"The most vehicles through Hanley Highway/Westway was between"
        for i in peak_hours:
            end_time=int(i)+1
            line_peakhour+=f" {i} and {end_time},"
        line_peakhour=line_peakhour.rstrip(",")
    print(line_peakhour)
    print(f"\nThe number of hours of rain for this date is {len(rain_dict)}")

    with open("results.txt","a") as result_file:     #Creating a new file and appending the required data
        result_file.write(f"""The data file selected is {file_name}
The total number of vehicles recorded for this date is {len(content)}
The total number of trucks recorded for this data is {truck_count}
The total number of electric vehicles recorded for this data is {e_vehicle_count}
The total number of two-wheeled vehicles recorded for this data is {two_wheeled_count}"
The total number of busses leaving Elm Avenue/Rabbit Road junction heading north is {b_leaving_n}
The total number of vehicles through both junctions not turning left or right is {no_turn_count}
The percentage of total vehicles recorded that are truck for this date is {truck_percent}%
The average number of bikes per hour for this date is {bicycle_per_hr}
The total number of vehicles recorded as over the speed limit for this date is {overspeed_count}
The total number of vehicles recorded through Elm Avenue/Rabbit Road junction is {j1_vehicle_count}
The total number of vehicles recorded through Hanley Highway/Westway junction is {j2_vehicle_count}
{j1_scooter_percent}% of vehicles recorded through Elm Avenue/Rabbit Road are scooters.
The highest number of vehicles in an hour on Hanley Highway/Westway is {peakhour_vehicle_count}
{line_peakhour}
The number of hours of rain for this date is {len(rain_dict)}
\n{"*"*60}\n
""")

    return j1_hour_dict,j2_hour_dict

    
def main():
    while True:
        user_date=date_input()
        formatted_date=f"{user_date[0:2]}/{user_date[2:4]}/{user_date[4:]}"
        file_name=f"traffic_data{user_date}.csv"
        try:
            with open(f"{file_name}","r") as file:
                content=file.readlines()
            j1_hour_dict,j2_hour_dict=read_file(file_name,content)
            histogram(j1_hour_dict,j2_hour_dict,formatted_date)
        except:
            print("""File of the given date not found.
The dates for which the files are available are 15/06/2024, 16/06/2024, and 21/06/2024.
Please enter these dates to get their data.""")

        repeat=repeat_loop()
        if repeat.lower()=="y" or repeat.lower()=="yes":
            print()
        else:
            print("End of Process.\n")
            break

main()