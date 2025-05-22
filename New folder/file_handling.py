# name=input("Enter name: ")
# grade= int(input("Enter grade: "))
# with open("grades.txt","a") as file:
#     file.write(f"\n{name}, {grade}")
# with open("grades.txt","r") as file:
#     content=file.readlines()
# print(content)

#Q1
# with open("grades.txt","r") as file:
#     contents=file.readlines()
# with open("low_grades.txt","w") as file:
#     file.write("")
# total=0
# highest=0
# for content in contents:
#     content=content.split(",")
#     content[1]=content[1].strip("\n")
#     total+=int(content[1])
#     if int(content[1])>highest:
#         highest=int(content[1])
#         highest_scorer=content[0]
#     if int(content[1])<80:
#         with open("low_grades.txt","a") as file:
#             file.write(f"{content[0]}\n")
# avg=total/len(contents)
# print(f"Average score: {avg}")
# print(f"Student with highest score: {highest_scorer}")


#Q2
# with open("logs.txt","r") as file:
#     contents=file.readlines()
# log_summary=dict()
# for content in contents:
#     content=content.split("] ")
#     content[1]=content[1].strip("\n")
#     if content[1] in log_summary:
#         log_summary[content[1]]+=1
#     else:
#         log_summary[content[1]]=1
# print(log_summary)
# with open("log_summary.txt","w") as file:
#     file.write("")
# with open("log_summary.txt","a") as file:
#     for key in log_summary:
#         file.write(f"{key}: {log_summary[key]}\n")


#Q3
# punctuations=[".",",","!","?"]
# word_count=dict()
# with open("article.txt","r") as file:
#     content=file.read()
# for punctuation in punctuations:
#     content=content.replace(punctuation,"").lower()
# words=content.split()
# for word in words:
#     if word in word_count:
#         word_count[word]+=1
#     else:
#         word_count[word]=1
# with open("top_words.txt","w") as file:
#     file.write("")
# print("The top 5 words are:")
# def highest_freq():
#     highest=0
#     for key,value in word_count.items():
#         if value>highest:
#             highest=value
#             highest_word=key
#     print(highest_word)
#     with open("top_words.txt","a") as file:
#         file.write(f"{highest_word}: {highest}\n")
#     return highest_word
# n=0
# while n<5:
#     highest_word=highest_freq()
#     word_count.pop(highest_word)
#     n+=1


#Q4
# x=int(input("Enter \"1\" to add new contact, \"2\" to search, and \"3\" to delete: "))
# if x==1:
#     name=input("Enter name to add: ")
#     phone=input("Enter phone number: ")
#     email=input("Enter e-mail: ")
#     with open("contacts.txt","a") as file:
#         file.write(f"{name.title()}, {phone}, {email}\n")
#     print("Contact added.")
# elif x==2:
#     name=input("Enter name to search: ")
#     with open("contacts.txt","r") as file:
#         content=file.readlines()
#     contact="Not found"
#     for line in content:
#         line_list=line.split(", ")
#         if line_list[0].lower()==name.lower():
#             print("Contact found")
#             print(f"Name: {line_list[0]}\nPhone: {line_list[1]}\nEmail: {line_list[2]}")
#             contact="Found"
#     if contact=="Not found":
#             print("Contact not found")
# elif x==3:
#     name=input("Enter name to delete: ")
#     with open("contacts.txt","r") as file:
#         content=file.readlines()
#     contact="Not found"
#     for line in content:
#         line_list=line.split(", ")
#         if line_list[0].lower()==name.lower():
#             content.remove(line)
#             with open("contacts.txt","w") as file:
#                 file.writelines(content)
#             print("Contact deleted")
#             contact="Found"
#     if contact=="Not found":
#         print("Contact not found")
# else:
#     print("Invalid. Please enter 1, 2 or 3")

#Q5
# with open("data.csv","r") as file:
#     content=file.readlines()
# content.pop(0)
# highest_stock=0
# with open("summary.csv","w") as file:
#         file.write(f"Product, Category, Total\n")
# for line in content:
#     line_list=line.split(",")
#     line_list[-1]=line_list[-1].strip("\n")
#     total_stock_value=int(line_list[-2])*int(line_list[-1])
#     with open("summary.csv","a") as file:
#         file.write(f"{line_list[0]}, {line_list[1]}, {total_stock_value}\n")
#     if total_stock_value>highest_stock:
#         highest_stock=total_stock_value
#         highest_stock_catagory=line_list[1]
# print(f"The category with highest total stock value is {highest_stock_catagory}")