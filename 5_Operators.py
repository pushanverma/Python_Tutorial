# ------------------------------Operators in Python------------------------------


# 1.----------------------------- Arithmetic Operators---------------------------------


# Addition
a = 10
b = 20
print(a + b, "....Addition ")

# Subtraction
print(b - a, "....Subtraction")

# Multiplication
print(a * b, ".....Multiplication ")


# Division
print(b / a, "....Division")


# Floor Division

print(12 // 5, "...Floor Division")
print(int(12 / 5), "...Converting the decimal value to int");
# Mimicking the Floor division


# note: Floor Division removes the point values i.e if answer comes 3.8 -> it will remove 0.8 , it will give answer -3

#Exponential / Power 
print(5**2,"....5 to the Power of 2");

# note: In python , we can calculate a bigger power also as Python is made in such a way to support big numbers . 

print(5**100,"....5 to the Power of 100");


# Modulus 
# This operator gives the remainder after the division. 

print(33%5,"....Remainder");



# 2. ----------------Assignment Operators(=) and Compound Assignment Operations----------------------

# a = int(input("Enter a="));  

# a+=20;

# a+=40;

# a+=60;

# print(a,"...value of a") 


# note: Python does not support Pre-(Increment / Decrement ) or Post- (Increment / Decrement)

b = 10;


# Trying Pre-Increment and Decrement in Python 

print(++b,".....Pre-Increment in Python");   # value remains same i.e 10
print(--b,"..... Pre-Decrement in Python");  # value remains same i.e 10 


# note: Why they remain same ?  - the reason to this is python treats 
# +(+x) , where '+' is treated as Unary operator and not a increment operator ,Similary with  -(-x) too. 


# Trying Post-Increment and Decrement in Python 

# print(b++,"....Trying Pre-Increment in Python");   # not supported in Python 
# print(b-- ,"....Trying Pre-Increment in Python");   # not supported in Python 


# Compound Assignment Operator --------- 

print("-----------------------------------------------------------");

x1=10;
x1+=10;
print(x1,"...Compound Assignment Addition ");

x2=10;
x2-=5;
print(x2,"...Compound Assignment Subtraction");

x3=10;
x3*=10;
print(x3,"...Compound Assignment Multiplication");

x4=10;
x4/=10;
print(x4,"...Compound Assignment Division");

x5=10;
x5//=3;
print(x5,"...Compound Assignment Floor Division");

x6=9;
x6%=5;
print(x6,"...Compound Assignment Modulus");

x7=5;
x7**=2;
print(x7,"...Compound Assignment Power");










