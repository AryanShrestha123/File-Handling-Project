#Q1
# name=input("Enter your name:")
# print(f"Hello, {name.title()}! Welcome to python")

#Q2
# num1=float(input("Enter first number: "))
# num2=float(input("Enter second number: "))
# print(f"The addition of {num1} and {num2} is {num1+num2}")

#Q3
# num1=int(input("Enter a number: "))
# if num1>0:
#     print("The number is positive")
# elif num1<0:
#     print("The number is negative")
# else:
#     print("The number is 0")

#Q4
# num1=int(input("Enter a number: "))
# if num1==0:
#     print("The number is 0")
# elif num1%2==0:
#     print("The number is even")
# else:
#     print("The number is odd")

#Q5
# n1=int(input("Enter a number: "))
# n2=int(input("Enter another number: "))
# if n1>n2:
#     print(f"{n1} is greater than {n2}")
# elif n1<n2:
#     print(f"{n2} is greater than {n1}")
# else:
#     print(f"{n1} and {n2} are equal")

#Q6
# n=int(input("Enter a number:"))
# sum = n*(n+1)/2
# print(f"The sum of first {n} natural number is {sum}")

#Q7
# c=float(input("Enter temperature in celcius: "))
# f=c* 9/5 +32
# print(f"Temperature in farhenheit is {f}")

#Q8
# year=int(input("Enter a year: "))
# if year%4==0:
#     if year%100==0 and year%400!=0:
#         print(f"{year} is not a leap year")
#     else:
#         print(f"{year} is a leap year")
# else:
#     print(f"{year} is not a leap year")

#Q9
# p=float(input("Enter principle: "))
# r=float(input("Enter rate: "))
# t=float(input("Enter time in years: "))
# si=p*r*t/100
# print(f"Simple interest= {si}")

#Q10
# r=float(input("Enter radius: "))
# pi=3.14159
# circumference=2*pi*r
# area=pi*r**2
# print(f"circumference= {circumference} and area={area}")

#Q11
# n=int(input("Enter a number: "))
# count=0
# if n>1:
#     for i in range(2,n):
#         if n%i==0:
#             count+=1
#             break
# else:
#     print("enter a number greater than 1.")
# if count==0:
#     print("Prime")
# else:
#         print("Not prime")
    

#Q12
# def factorial(n):
#     if n==0 or n==1:
#         return 1
#     else:
#         return n*factorial(n-1)
# x=int(input("Enter a number: "))
# print(f"{x}!= {factorial(x)}")
  
#Q13
# string=input("Enter a string: ")
# reversed_string=string[::-1]
# print(reversed_string)

#Q14
# word=input("Enter a word: ")
# vowels="aeiou"
# count=0
# for vowel in vowels:
#     count+=word.lower().count(vowel)
# print(f"Number of vowels= {count}")


#Q15
# def multiplication_table(n):
#     for i in range(1,11):
#         print(f"{n} * {i} = {n*i}")

# n=int(input("Enter a number: "))
# multiplication_table(n)


#Q16
# def sum_of_digits(num):
#     sum=0
#     while num!=0:
#         sum += num%10
#         num=num//10
#     return sum
# x=int(input("Enter positive number: "))
# print(f"{sum_of_digits(x)}")


#Q17 
# a=input("Enter a string: ")
# if a.lower()==a[::-1].lower():
#     print("Pallindrome")
# else:
#     print("Not a Pallindrome")


#Q18
# n=int(input("Enter a number"))
# fibo_list=[0,1]
# if n<=0:
#     print("nil")
# elif n==1:
#     print(fibo_list[0])
# else:
#     while len(fibo_list)<n:
#         fibo_list.append(fibo_list[-1]+fibo_list[-2])
#     print(fibo_list)


#Q19
# list1=list(map(int,input("Enter integers seperated by spaces: ").split()))
# print(f"large= {max(list1)}")
# print(f"small= {min(list1)}")


#Q20
# def word_freq(sent):
#     words = sent.split(" ")
#     freq = {}
#     for word in words:
#         if word in freq:
#             freq[word] += 1
#         else:
#             freq[word] = 1
#     return freq
# x=input("Enter a sentence: ")
# print(word_freq(x))


#Q21
# def square(list1):
#     new_list=list()
#     for i in list1:
#         i=i**2
#         new_list.append(i)
#     return new_list

# n=int(input("Enter the elements you want: "))
# list1=[]
# while len(list1)<n:
#     try:
#         a=int(input("Enter the element: "))
#         list1.append(a)
#     except:
#         print("Invalid input. Enter an integer.")
# result=square(list1)
# print(f"\nInput: {list1}")
# print(f"Output: {result}")


#Q22
# def remove_duplicates(list1):
#     new_list=[]
#     for item in list1:
#         if item not in new_list:
#             new_list.append(item)
#     return new_list

# x=True
# while x:
#     try:
#         list1=list(map(int,input("Enter integers seperated by spaces: ").split()))
#         x=False
#     except:
#         print("Invalid input. Enter integers only.")
# print(f"\nInput: {list1}")
# print(f"Output: {remove_duplicates(list1)}")


#Q23
# def merge_sort(list1,list2):
#     new_list=list1+list2
#     new_list.sort()
#     return new_list
# list1=list(map(int,input("Enter integers of list 1 seperated by spaces:").split()))
# list2=list(map(int,input("Enter integers of list 2 seperated by spaces:").split()))
# output=merge_sort(list1,list2)
# print("\n",output)

#Q24
# def specific_word_count(sent,n):
#     words = sent.split()
#     list=[]
#     for word in words:
#         if len(word)==n:
#             list.append(word)
#     return list
# sent=input("Enter a sentence: ")
# n=int(input("Enter the length of word: "))
# output=specific_word_count(sent,n)
# print(output)

#Q25
# sent=input("Enter a sentence: ")
# symbols=[",",".","!"]
# words=sent.split()
# output=[]
# for word in words:
#     for symbol in symbols:
#         word=word.replace(symbol,"")
#     output.append(word)
# print(f"Words: {output}")

#Q26
# sent=input("Enter a sentence: ")
# words=sent.split()
# for word in words:
#     print(word.title(),end=" ")

#Q27
# numbers=input("Enter numbers seperated by spaces: ")
# input_list=numbers.split()
# num_list=list(map(int,input_list))
# num_list.remove(max(num_list))
# second_largest=max(num_list)
# print(second_largest)

#Q28
# string=input("Enter a sentence: ")
# sub_string=input("Enter a sub-string: ")
# status="not found"
# for i in range(len(string)):
#     if string[i:i+len(sub_string)]==sub_string:
#         print(f"Sub-string found at index {i}")
#         status="found"
# if status=="not found":
#     print("Substring not found")

#Q29
# sentence = input("Enter a sentence: ")
# target_word = input("Enter the target word to replace: ")
# replacement_word = input("Enter the replacement word: ")
# modified_sentence = sentence.replace(target_word, replacement_word)
# print("Modified sentence:", modified_sentence)

#Q30
# list1 = input("Enter the elements of the first list separated by spaces: ").split()
# list2 = input("Enter the elements of the second list separated by spaces: ").split()
# if len(list1) != len(list2):
#     print("Error: Both lists must be of equal length.")
# else:
#     combined_list = []
#     for i in range(len(list1)):
#         combined_list.append(list1[i])
#         combined_list.append(list2[i])
#     print("Combined list:", combined_list)

#Q31
# numbers = input("Enter numbers separated by spaces: ").split()
# frequency_dict = {}
# for num in numbers:
#     if num in frequency_dict:
#         frequency_dict[num] += 1
#     else:
#         frequency_dict[num] = 1
# print("Frequency of each number:", frequency_dict)

#Q32
# sentence = input("Enter a sentence: ")
# letter_count = {}
# for char in sentence.lower():
#     if char.isalpha():  
#         if char in letter_count:
#             letter_count[char] += 1
#         else:
#             letter_count[char] = 1
# print(letter_count)

#Q33
# numbers = input("Enter integers separated by spaces: ").split()
# sum=0
# for num in numbers:
#     if int(num)%2==0:
#         sum+=int(num)
# print(f"The sum of even numbers of list is {sum}")


#Q34
# n=int(input("Enter the number of lists you want inside a list: "))
# main_list=[]
# flatten_list=[]
# while n>0:
#     n-=1
#     items=input("Enter the elements of list separated by spaces: ").split()
#     main_list.append(items)
# for list in main_list:
#     for item in list:
#         flatten_list.append(item)
# print(f"Input: {main_list}")
# print(f"Flatten list: {flatten_list}")

#Q35
# print("For first 2x2 matrix")
# m1_r1=list(map(int,input("Enter the first 2 elements separated by a space:").split()))
# m1_r2=list(map(int,input("Enter the 3rd and 4th element separated by a space:").split()))
# print()
# print("For second 2x2 matrix")
# m2_r1=list(map(int,input("Enter the first 2 elements separated by a space:").split()))
# m2_r2=list(map(int,input("Enter the 3rd and 4th element separated by a space:").split()))

# m_r1=f"{m1_r1[0]+m2_r1[0]}, {m1_r1[1]+m2_r1[1]}"
# m_r2=f"{m1_r2[0]+m2_r2[0]}, {m1_r2[1]+m2_r2[1]}"
# print(f"Sum of the two matrices is: \n{m_r1}\n{m_r2}")


#Q36
# list1= input("Enter integers separated by spaces: ").split()
# list2= input("Enter integers separated by spaces: ").split()
# intersection=[]
# for item in list1:
#     if item in list2:
#         intersection.append(item)
# print(intersection)

#Q37
# str1=input("Enter a string: ")
# str2=input("Enter another string: ")
# if sorted(str1.lower())==sorted(str2.lower()):
#     print("They are anagram.")
# else:
#     print("They are not anagram.")


#Q38
# r1=list(map(int,input("Enter the first 2 elements separated by a space:").split()))
# r2=list(map(int,input("Enter the 3rd and 4th element separated by a space:").split()))
# if len(r1)!=2 and len(r2)!=2:
#     print("Please enter a 2x2 matrix.")
# else:
#     print(f"Matrix:\n{r1}\n{r2}")
#     t_r1=f"{r1[0], r2[0]}"
#     t_r2=f"{r1[1], r2[1]}"
#     print(f"\nTransposed matrix:\n{t_r1}\n{t_r2}")

#Q39
d={"hello":5,"world":5,"welcome":7,"to":2,"python":6,"programming":11}
print(f"Initial dictationary: {d}")
sorted_d={}
values=[]
for value in d.values():
    values.append(value)
while len(d)>0:
    max_value=max(values)
    for k,v in d.items():
        if v==max_value:
            sorted_d[k]=max_value
            values.remove(max_value)
            break
    d.pop(k)
print(f"Sorted dictationary: {sorted_d}")



#Q40
# numbers = list(map(int, input("Enter integers separated by spaces: ").split()))
# target = int(input("Enter the target number: "))
# found = False
# for num in numbers:
#     complement = target - num
#     if complement in numbers:
#         print(f"Numbers found: {complement} and {num}")
#         found = True
#         break
# if found==False:
#     print("No two numbers add up to the target.")

#Q41
# letter_dict={0:"a",1:"b",2:"c",3:"d",4:"e",5:"f",6:"g",7:"h",8:"i",9:"j",10:"k",11:"l",12:"m",13:"n",14:"o",15:"p",16:"q",17:"r",18:"s",19:"t",20:"u",21:"v",22:"w",23:"x",24:"y",25:"x"}
# def cipher(message,shift_number):
#     encoded_message=""
#     for char in message:
#         if char==" ":
#             encoded_message+=" "
#         else:
#             for key,value in letter_dict.items():
#                 if char==value:
#                     encoded_message+=letter_dict[(key+shift_number)%26]
#     return encoded_message
# message=input("Enter the message you want to enocde: ").lower()
# shift_number=int(input("Enter the number by which you want to shift it : "))
# encoded_message=cipher(message, shift_number)
# print(f"Encoded message: {encoded_message}")

#Q42
# sent=input("Enter a sentence: ")
# words=sent.split()
# longest_word=""
# for word in words:
#     if len(word)>len(longest_word):
#         longest_word=word
# print(f"The longest word is {longest_word}.")


#Q43
# punctuations=[".",",","!","?"]
# word_count=dict()
# sent=input("Enter a sentence: ")
# for punctuation in punctuations:
#     sent=sent.replace(punctuation,"").lower()
# words=sent.split()
# for word in words:
#     if word in word_count:
#         word_count[word]+=1
#     else:
#         word_count[word]=1
# print(word_count)


#Q44
# numbers=input("Enter numbers seperated by spaces: ").split()
# new_list=[]
# dulpicates=[]
# for number in numbers:
#     if number in new_list:
#         dulpicates.append(number)
#     else:
#         new_list.append(number)
# print(f"Origianl list: {numbers}")
# print(f"List of duplicates: {dulpicates}")


#Q45
# for i in range(1,51):
#     if i%3==0 and i%5==0:
#         print("FizzBuzz")
#     elif i%3==0:
#         print("Fizz")
#     elif i%5==0:
#         print("Buzz")
#     else:
#         print(i)


#Q46
# str1=input("Enter first string: ").lower()
# str2=input("Enter second string: ").lower()
# print("Letters\t|Frequency in str1\t| Frequency in str2")
# letters=[]
# # str2_dict={}
# def letter_count(string):
#     for letter in string:
#         if letter in letters:
#             continue
#         else:
#             print(f"{letter}\t|\t{str1.count(letter)}\t\t|\t{str2.count(letter)}")
#             letters.append(letter)
# letter_count(str1)
# letter_count(str2)


#Q47
# n=int(input("Enter the number of rows you want in pyramid: "))
# for i in range(1,n+1):
#     print(" "*(n-i),end="")
#     print("*"*(i*2-1))

#Q48
# print("""Password should contain atleast 8 characters, both upper and lower case letters, 
# atleast a digit, and a special character (like @, , or $)""")
# def password_validator(password):
#     if len(password)>=8 and password.lower()!=password and password.upper()!=password:
#         digit="not found"
#         for char in password:
#             if char.isdigit():
#                 digit="found"
#                 break
#         if digit=="not found":
#             return "Invalid. Atleast 1 digit is required."
#         else:
#             if password.isalnum():
#                 return "Invalid. Atleast 1 special character (like @,!,#...) is required."
#             else:
#                 return "valid"
#     else:
#         return "Invalid. Password should contain atleast 8 characters including both upper and lower case letters."

# x=input("Enter a password to create: ")
# y=password_validator(x)
# if y=="valid":
#     print("Password is valid")
# else:
#     print(y)


#Q49
# def factorial(n):
#     result=1
#     while n>1:
#         result*=n
#         n-=1
#     return result
# n=int(input("Enter a number: "))
# result=factorial(n)
# print(f"{n}! = {result}")


#Q50
# l1=input("Enter integers of list 1 separated by spaces: ").split()
# l2=input("Enter integers of list 2 separated by spaces: ").split()
# unique_l1=[]
# unique_l2=[]
# for item in l1:
#     if item not in l2:
#         unique_l1.append(item)
# for item in l2:
#     if item not in l1:
#         unique_l2.append(item)
# if len(unique_l1)>0:
#     print(f"The unique elements in list 1 are {unique_l1}")
# else:
#     print("No unique element in list 1")
# if len(unique_l2)>0:
#     print(f"The unique elements in list 2 are {unique_l2}")
# else:
#     print("No unique element in list 1")