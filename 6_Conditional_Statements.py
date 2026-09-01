# ----------------------Conditional Statements---------------------------------

# Conditional Statements helps to control the flow of program


# if-else

# a=13;

# if a>10:
#     print("Number greater than 10");
# else:
#     print("Number smaller than 10");


# Nested if-else


# x = int(input("Enter the marks ="));


# if x > 90:
#     print("A grade");
# elif x>80 and x<90:
#     print("B grade");
# elif x>70 and x<80:
#     print("C grade");
# elif x>60 and x<70:
#     print("D grade");
# else:
#     print("Have to Improve")


# QUESTIONS

# Q1: Accept two numbers and print the greater b/w them ->

# n1 = int(input("Enter first number ="));
# n2 = int(input("Enter second number ="));

# if n1>n2:
#     print("First number is greater");
# elif n2>n1:
#     print("Second number is greater");
# else:
#     print("Numbers are equal");


# Q2 : Take input of gender as a character and print the greeting message accoridng to gender (Sir / Madam)

# gender =input("Enter gender (M/F)= ");

# if (gender=="M" or gender=="m"):
#     print("Good Morning Sir");
# elif (gender=="F" or gender=="f"):
#     print("Good Morning Mam");
# else:
#     print("UnIdentified Gender");


# Q3 : Accept a integer and tell if its Even / Odd

# p = int(input("Enter the number ="));

# if p%2==0:
#     print("Even Number");
# else:
#     print("Odd Number");


# Q4: Accept the name and age of the user and check if a valid voter or not ?

name = input("Enter name =")
age = int(input("Enter age ="))

if age >= 18:
    print(f"Hey {name} , you are a valid voter")
else:
    print(f"Hey {name} , unfortunately you cannot vote . Thanks !!")


# Q5: Accept a year and check if its a Leap Year or not ?

# year = int(input("Enter year="));

# if (year%400==0):
#     print(f"{year} is a Leap year");
# elif (year%400!=0):
#     if(year%100==0):
#         print(f"{year} is not a Leap year");
#     elif (year%100!=0):
#         if(year%4==0):
#             print(f"{year} is a Leap Year");
#         else:
#             print(f"{year} is not a Leap year");


# Leap Year logic :- (Kind of Like a Flow Diagram)
# Check first if the year is divisible by 400 (It will be either - Yes / No )
# if Yes, divisible by 400 - Then its a Leap Year
# if No, not divisible by 400 - Check if the year is divisible by 100 (It will be either - Yes / No )
# if Yes , divisible by 100 - Not a Leap year 
# if No , not divisible by 100 - Check if the year is divisible by 4 (It will be either - Yes / No )
# if Yes , divisible by 4 - Then its a Leap Year 
# if No , not divisible by 4 - Not a Leap Year 



# Q6:  Elif Ladder Question based on Temprature.


# temp = int(input("Enter the temprature in celcius ="));

if temp<0:
    print("Freezing Cold");
elif temp>=0 and temp<10:
    print("very cold");
elif temp>=10 and temp<20:
    print("Cold");
elif temp>=20 and temp<30:
    print("Pleasent");
elif temp>=30 and temp<40:
    print("Hot");
else:
    print("Very Hot");





