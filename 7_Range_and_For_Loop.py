# --------------------------RANGE Function--------------------------------

# Range function accepts 3 parameters (start , stop , step) - we call it "triple S"
# In this function giving stop value is essential. You can skip the start and step (if you do not provide these values
# it will take the default values)

# Default values of
# start = 0
# step  = 1

# Range function can be present in 3 forms -
# 1. range(5) - providing only the stop value i.e range(stop)
# 2. range(1,6)- providing start and stop value i.e range(start , stop)
# 3. range(1,11,2)- providing start , stop and step i.e range(start , stop , step)
#


# Just printing the Range Function
# print(range(5),".....Range with stop value");
# print(range(2,20), "...range with start and stop value");
# print(range(1,21,1),"...range with start, stop and step value");
# print(range(1,21,3),"...range with start, stop and step value");


# --------------------------------For Loop with Range-------------------------


# ---------Loops with Numbers-------------

# Example 1->(Since stop=5 , so 0 till 4 will be the values)
# for i in range(5):
#     print(i);


# Example 2 ->(Since start =2 and stop =20 and will stop at 19 , so 2 till 19 will be the values )
# for i in range(2,20):
#     print(i);


# Example 3 ->(Since start=1 , stop =21 and will stop at 20 and step =2 ,explanation below )
# for i in range(1,21,2):
#     print(i);

# (1,3,5,7,9,11,13,15,17,19)
# Dry run
# 1 - yes
# 2
# 3 -yes
# 4
# 5 -yes
# 6
# 7-yes
# 8
# 9 -yes
# 10
# 11-yes
# 12
# 13-yes
# 14
# 15-yes
# 16
# 17-yes
# 18
# 19-yes
# 20

# ------- QUESTIONS-------

# Q1 : Print numbers fromm 16 to 1

# for i in range(16,0,-1):
#     print(i);


# Q2 : Print numbers fromm 20 to 50

# for i in range(20,51,1):
#     print(i);


# Q3 : Print numbers fromm -3 to -15

# for i in range(-3, -16 , -1):
#     print(i);


# Q3 : Print table of any number

# num = int(input("Enter number ="));

# 1st method
# for i in range(1, 11, 1):
#     print(num,"x",i,"=",num*i);


# 2nd method
# for i in range(5,51,5):
#     print(i);

# 3rd method
# for i in range(num, (num*10)+1, num):
#     print(i);


# -----------Loops with Strings---------------


# We can iterate the Strings in 2 ways -
# 1. thru the index
# 2. Directly iterating on string


text = "Hello this is Pushan Verma"


# 1. Calculating the length of string and then getting the character sitting at that index

# print(len(text),"...length of the text");

# for i in range(len(text)):
#     print(text[i]);


# 2. Directly iterating on String

# for i in text:
#     print(i);


# -----------break , Continue and Else Statement ---------------


# 1. break statement (whenever the Python encounters a break statement , it just stops at that value  )

# for i in range(20):
#     if (i==15):
#         break;
#     else:
#         print(i);

# Explanation -> Since we havent mentioned the start and step , it will take the default values - start(0) and step(1).
# Here the loop stops at 14 , bcoz we have given the condition that it will stop at 15.


# 2. continue statement (whenever you encounter the continue statement , only for that value it will skip and the rest will continue as it is )


# for i in range(20):
#     if i == 15:
#         continue
#     else:
#         print(i)

# Explanation -> Since we have mentioned that at i==15 continue , that means skip the value 15 and print all rest .


# 3. Else statement ( V. Imp )
# Else Statement works with break statement.
# If break does not work then Else will work.
# If break works then Else would not work .

# note: Usually we see ,  else is connected with if . But , else is also connected with for loop also


for i in range(1, 21):
    if i == 15:
        print("....Break statement is executed")
        break
    else:
        print(i)
else:
    print("....Break statement is not executed");


# Here the O/p will be -> Break statement is executed.


print("----------------------------")

for i in range(1, 21):
    if i == 57:
        print("....Break statement is executed")
        break
    else:
        print(i)
else:
    print("....Break statement is not executed")


# Here the O/p will be -> Break statement is not executed.
