from graphics import *

#Task D
def histogram(d1,d2):
    window=GraphWin("Histogram",900,450)
    keys=list(d1.keys())
    values1=list(d1.values())
    values2=list(d2.values())
    bar_numbers=len(keys)
    bar_width=800/bar_numbers
    single_bar=bar_width/4
    max_v1=max(values1)
    max_v2=max(values2)
    max_v=max(max_v1,max_v2)
    scale=300/max_v
    for i in range(bar_numbers):
        group_centre=50+i*bar_width+single_bar*2
        x11=group_centre-single_bar
        y11=400
        x21=x11+single_bar
        y21=y11-values1[i]*scale
        rect1=Rectangle(Point(x11,y11),Point(x21,y21))
        rect1.setFill("cyan")
        rect1.draw(window)
        
        x12=x21
        y12=400
        x22=x12+single_bar
        y22=y12-values2[i]*scale
        rect2=Rectangle(Point(x12,y12),Point(x22,y22))
        rect2.setFill("orange")
        rect2.draw(window)

        text1=Text(Point(group_centre-single_bar/2,y21-3),values1[i])
        text1.setSize(6)
        text1.draw(window)
        text2=Text(Point(group_centre+single_bar/2,y22-3),values2[i])
        text2.setSize(6)
        text2.draw(window)

        text=Text(Point(group_centre,410),f"{keys[i]}")
        text.draw(window)

    aLine=Line(Point(50,400),Point(850,400))
    aLine.setWidth(3)
    aLine.draw(window)
    a_text=Text(Point(450,430),"Hours")
    a_text.draw(window)

    header=Text(Point(200,20),"Histogram of vehicle frequency per hour")
    header.setStyle("bold")
    header.setSize(15)
    header.draw(window)
    box1=Rectangle(Point(60,50),Point(70,60))
    box1.setFill("cyan")
    box1.draw(window)
    junction1=Text(Point(140,55),"Elm Avenue/Rabbit Road")
    junction1.setSize(8)
    junction1.draw(window)

    box2=Rectangle(Point(60,70),Point(70,80))
    box2.setFill("orange")
    box2.draw(window)
    junction2=Text(Point(145,75),"Hanley Highway/Westway")
    junction2.setSize(8)
    junction2.draw(window)
    window.getMouse()
    window.close()

def input_check(input,l,u):
    if input.isdigit():
        if l<=int(input) and int(input)<=u:
            return "Valid"
        else:
            print(f"Values must be between {l} and {u}.")
            return "Invalid"
    else:
        print("Enter integers")
        return "Invalid"

#Task A
def user_input():
    check="Invalid"
    while check=="Invalid":
        day=input("Please enter the day in the format dd: ")
        if len(day)<2:
            day="0"+day
        check=input_check(day,1,31)
    
    check="Invalid"
    while check=="Invalid":
        month=input("Enter the month in the format mm: ")
        if len(month)<2:
            month="0"+month
        check=input_check(month,1,12)

    check="Invalid"
    while check=="Invalid":
        year=input("Please enter the year in the format yy: ")
        check=input_check(year,2000,2024)

    date=day+month+year
    return date

#Task E
def repeat():
    while True:
        repeat=input("Do you want to select another data file for a different date? Enter 'Y' or 'N': ")
        if repeat.lower()=="y" or repeat.lower()=="n":
            return repeat
        else:
            print("Please enter 'Y' or 'N'.")

#Task B
def file_reading(date,content):
    content.pop(0)
    print(f"\nThe data file selected is {f"traffic_data{date}.csv"}")
    print(f"The total number of vehicles recorded is {len(content)}")
    electric_hybrid=list()
    two_wheel=0
    bicycle_count=0
    j1={}
    j2={}
    rain={}

    leaving_n=0
    overspeed=0
    vehicle_count1=0
    vehicle_count2=0
    scooter=0
    truck_count=0
    same_dir=0

    for data in content:
        data=data.split(",")
        if data[-2]=="Truck":
            truck_count+=1
        if data[-2]=="Bicycle" or data[-2]=="Motorcycle" or data[-2]=="Scooter":
            two_wheel+=1
        data[-1]=data[-1].strip("\n")
        electric_hybrid.append(data[-1])
        if data[-2]=="Bicycle":
            bicycle_count+=1
        if data[-6]==data[-7]:
            same_dir+=1
        if data[0] == "Elm Avenue/Rabbit Road" and data[4] == "N" and data[-2] == "Buss":
            leaving_n+=1
        if int(data[-3])>int(data[-4]):
            overspeed+=1
        if data[0] == "Elm Avenue/Rabbit Road":
            vehicle_count1+=1
            time=data[2].split(":")
            if data[-2]=="Scooter":
                scooter+=1
            if time[0] not in j1.keys():
                j1[time[0]]=1
            else:
                j1[time[0]]+=1
            
        else:
            vehicle_count2+=1
            time=data[2].split(":")
            if time[0] not in j2.keys():
                j2[time[0]]=1
            else:
                j2[time[0]]+=1
        if data[-5]=="Heavy Rain" or data[-5]=="Light Rain":
            rain_time=data[2].split(":")
            rain[rain_time[0]]=1

    percent_truck=round((truck_count/len(content))*100)
    e_vehicle=electric_hybrid.count("True")
    bicycle_phr=round(bicycle_count/24)
    percent_scoter=round(scooter/vehicle_count1*100)
    peakhour_count=max(j2.values())
    for k in j2:
        if j2[k]==peakhour_count:
            peak_hour=k

    print(f"\nThe total number of trucks is {truck_count}")
    print(f"The total number of electric vehicles is {e_vehicle}")
    print(f"The total number of two-wheeled vehicles is {two_wheel}")
    print(f"The total number of bus leaving Elm Avenue/Rabbit Road heading north is {leaving_n}")
    print(f"The percentage of total vehicles recorded that are truck for this date is {percent_truck}%")
    print(f"The average number of bikes per hour is {bicycle_phr}")
    print(f"Number of vehicles without turning left or right is {same_dir}")
    print(f"The total number of vehicles over the speed limit is {overspeed}")
    print(f"\nThe total number of vehicles through Elm Avenue/Rabbit Road is {vehicle_count1}")
    print(f"The total number of vehicles through Hanley Highway/Westway is {vehicle_count2}")
    print(f"The % of scooters through Elm Avenue/Rabbit Road is {percent_scoter}%.")
    print(f"\nThe peak number of vehicles in an hour on Hanley Highway/Westway is {peakhour_count}")
    print(f"The most vehicles through Hanley Highway/Westway was between {peak_hour}:00 and {int(peak_hour)+1}:00")
    print(f"The number of rain hours is {len(rain)}")

    #Task C
    with open("result.txt","a") as file:
        file.write(f"""*************************
The data file selected is {f"traffic_data{date}.csv"}
The total number of trucks is {truck_count}
\nThe total number of electric vehicles is {e_vehicle}
The total number of two-wheeled vehicles is {two_wheel}
The total number of bus leaving Elm Avenue/Rabbit Road heading north is {leaving_n}
The percentage of total vehicles recorded that are truck for this date is {percent_truck}%
The average number of bikes per hour is {bicycle_phr}
Number of vehicles without turning left or right is {same_dir}
The total number of vehicles over the speed limit is {overspeed}
\nThe total number of vehicles through Elm Avenue/Rabbit Road is {vehicle_count1}
The total number of vehicles through Hanley Highway/Westway is {vehicle_count2}
The % of scooters through Elm Avenue/Rabbit Road is {percent_scoter}%.
Number of vehicles without turning left or right is {same_dir}
\nThe peak number of vehicles in an hour on Hanley Highway/Westway is {peakhour_count}
The most vehicles through Hanley Highway/Westway was between {peak_hour}:00 and {int(peak_hour)+1}:00
The number of rain hours is {len(rain)}\n
""")

    histogram(j1,j2)

def main_function():
    while True:
        date=user_input()
        try:
            with open(f"traffic_data{date}.csv","r") as file:
                content=file.readlines()
                file_reading(date,content)
        except:
            print("File of the given date not found.")
        #Task E
        r=repeat()
        if r.upper()=="N":
            print("End.")
            break
        
main_function()