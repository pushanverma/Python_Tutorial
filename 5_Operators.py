# ------------------------------Operators in Python------------------------------


# 1.----------------------------- Arithmetic Operators---------------------------------


# Addition
a = 10
b = 20
# print(a + b, "....Addition ")

# Subtraction
# print(b - a, "....Subtraction")

# Multiplication
# print(a * b, ".....Multiplication ")


# Division
# print(b / a, "....Division")


# Floor Division

# print(12 // 5, "...Floor Division")
# print(int(12 / 5), "...Converting the decimal value to int");
# Mimicking the Floor division


# note: Floor Division removes the point values i.e if answer comes 3.8 -> it will remove 0.8 , it will give answer -3

# Exponential / Power
# print(5**2,"....5 to the Power of 2");

# note: In python , we can calculate a bigger power also as Python is made in such a way to support big numbers .

# print(5**100,"....5 to the Power of 100");


# Modulus
# This operator gives the remainder after the division.

# print(33%5,"....Remainder");


# 2. ----------------Assignment Operators(=) and Compound Assignment Operations----------------------

# a = int(input("Enter a="));

# a+=20;

# a+=40;

# a+=60;

# print(a,"...value of a")


# note: Python does not support Pre-(Increment / Decrement ) or Post- (Increment / Decrement)

b = 10


# Trying Pre-Increment and Decrement in Python

# print(++b,".....Pre-Increment in Python");   # value remains same i.e 10
# print(--b,"..... Pre-Decrement in Python");  # value remains same i.e 10


# note: Why they remain same ?  - the reason to this is python treats
# +(+x) , where '+' is treated as Unary operator and not a increment operator ,Similary with  -(-x) too.


# Trying Post-Increment and Decrement in Python

# print(b++,"....Trying Pre-Increment in Python");   # not supported in Python
# print(b-- ,"....Trying Pre-Increment in Python");   # not supported in Python


# Compound Assignment Operator

# print("-----------------------------------------------------------");

x1 = 10
x1 += 10
# print(x1,"...Compound Assignment Addition ");

x2 = 10
x2 -= 5
# print(x2,"...Compound Assignment Subtraction");

x3 = 10
x3 *= 10
# print(x3,"...Compound Assignment Multiplication");

x4 = 10
x4 /= 10
# print(x4,"...Compound Assignment Division");

x5 = 10
x5 //= 3
# print(x5,"...Compound Assignment Floor Division");

x6 = 9
x6 %= 5
# print(x6,"...Compound Assignment Modulus");

x7 = 5
x7 **= 2
# print(x7,"...Compound Assignment Power");


# ------------------------------- Comparison Operators---------------------------------

# note: Comparison Operators will always provide a Boolean result

# 6 Types of Comparison Operators :  < , > , <= , >= , == , !=


# less than and more than operators
# print(5<3,"....5 is more than 3 so - False");
# print(6>2,"....6 is more than 2 so - True");


# less than and more than operators with equality
# print(5<=3,"....5 is more than 3 and not equal to 3 - False");
# print(5<=6,"....5 is less than 6 and not equal 6 - True(since , one of the comparison is correct)");


# print(2>=6,"....2 is not more than 6 and not equal to 6 - False");
# print(6>=2,"....6 is more than 2 and not equal to 2 - True");


# note: Python does not have === like Js , where we also check the dataType of the variable

# note: Strings in Python are comapred lexicographically(comparing one word to other word)

# How to compare Strings

# Less than and more than operators

# 1 Comparing the Characters of Strings 

print("a" < "b", "...True")
# because while comparing python converts the characters of the string to its Ascii value / Unicode value and then compares(internally it gets the Ascii value from the ord() function)
# Here the Ascii value of a =97 and the Ascii value of b =98 ,
# So b is bigger than a .


# Comparing "A" with "a"
print("a">"A","....True"); # it is true bcoz the Ascii value of "a" = 97 and Ascii value of "A" = 65.
# So a > A .

# 2 Comparing the Full Strings

#  (apple vs banana)
print("apple" < "banana",".....True");  # it is True bcoz , Python compares character by character. Let me explain you with steps -
# Step 1 -> a vs b -> Ascii value of a=97 , Ascii value of b =98 , So b wins . 
#  Therefore the comparison stops here and 2nd String is bigger than 1st . 


#(apple vs apricot)
print("apple"<"apricot","....True"); 
# Since we know that Python compares the Strings character by character 
# The first two characters of both the Strings are same i.e "ap" so they cant decide which one is greater but ,
# 3rd charcter of both the strings i.e "p" vs "r" ,and here we can see that Ascii value of r > Ascii value of p . 
# So , 2nd String will be greater .


# (a vs apple) or (app vs apple) - In both 2nd String will be greater 
print("a" < "apple" ,".....True");
# Since first two characters of the String is same i.e "a" , so can't compare that.
# and here the first String is finished so the remaining will be greater than 1st one . 

# (z vs apple) or (zoo vs apple)
print("z" > "apple",".....True");
# Here the first String is z and a , and Ascii value of z > Ascii value of a , So comparison stops and 
# 1st String is bigger than 2nd one .
# note: Length of String does not matter all the time , the character matters .


# 3 Comparing equal Strings 

print("apple"=="apple",".....True");
# Since all the characters inside the String matches , therefore True 

print("apple"=="Apple","......False");
# Even though the word is same , but since the 2nd String 1st character is Capitalised and since we know that 
# python compare the ascii values of the characters while comparing .
# Ascii value of a(97) > Ascii value of A(65) , So False


print("apple" != "Apple","....True");



# 4 Comparing the Numbers present inside the String

print("10" < "2","....False");
# Why is 10 smaller than 2 ?
# This is because as usual , Python compare the characters so 1 vs 2 . 
# Ascii value of 1 is 49 and Ascii value of 2 is 50. SO , comparison stops here and 2nd string is bigger than 1st 


# 5 With Space 

print("apple" == " apple","...False");
# Notice that the 2nd STring has a space right in the starting , So according to Python 
# it starts comparing the characters - So compares "a vs whitespace" , 
# Ascii value of a(97) > Ascii value of whitespace(32) . SO they are not equal , rather 1st one is greater than 2nd .
print("apple" > " apple","...True");


# 6 Comparing String with Numbers 

print("abc"> "1","....True");
# This is because as usual we compare the characters of the strings and "a" vs "1" , So 
# Ascii value of a(97) > Ascii value of 1(32) . So , 1st String is greater than 2nd String.

# print("a" > 32,"....Error");
# You cannot compare a String with Number here . You can only compare as shown above .



# -------------------------------Logical Operators---------------------------------



