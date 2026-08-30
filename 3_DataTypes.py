# --------------------------- 3. Data Types--------------------------------


# 3.1 ---Numeric----


x1 = 10
# +ve integer
x2 = -10
# -ve integer
x3 = 0
# 0 is also in integer range

y1 = 12.4
y2 = 12 / 3
# Float number(All the decimal numbers and Fraction numbers are considered as float )

z = 2 + 3j
# Complex Number


# print(x1 , type(x1) ,"....Integer Data Type");
# print(x2 , type(x2),"....Integer Data Type");
# print(x3 , type(x3),"....Integer Data Type");


# print(y1,  type(y1), "....FloatData Type");
# print(y2,  type(y2), "....FloatData Type");

# print(z , type(z),"....Complex Number Data Type");


# 3.2 ----Boolean-----

flag1 = True
flag2 = False

# print(flag1 , type(flag1),"....Boolean Data Type");
# print(flag2, type(flag2),".....Boolean Data Type");


# 3.3 -----String-----


name = "Pushan Verma"

# print(name, type(name), "....String Data Type ")


# Positive Indexing
# print(name[0], "....0th Character in String")
# P
# print(name[6], ".....6th character in String")
# empty Space


# Negative Indexing (from behind)
# print(name[-1], ".....last character in String")
# a
# print(name[-3], "....3rd last character in String")
# r

# print(name[12], ".....accessing the character which is not present ")
# Will give you a Error(Do not Uncomment it )


# print(name[11] == name[-1], "...validating")
# Checking if the last character is equal to first character from Behind


# Getting the Unicode of a character

name_unicode = ord(name[1])
# print(name_unicode,"....Unicode of the 1st Character i.e u");


# Getting the Character from Unicode

getting_character_from_unicode = chr(name_unicode)
# print(getting_character_from_unicode,".....Getting character from Unicode i.e 117 = u");


# -------------String Slicing (Taking a set of characters out of String )---------
# name[start :end :step]

# print(name[0:6:1], "...extracting Pushan")
# extracting Pushan with Step =1
# print(name[0:11:2], "...extracting indexes that are multiple of 2")
# extracting in the multiple of 2- 0,2,4,6,8,10 positions are printed
# print(name[0:11:3], "...extracting indexes that are multiple of 3")
# extracting in the multiple of 3- 0,3,6,9 positions are printed


# Extract "Push" from the name String

# print(name[0:4:1], "....extracting Push from nameString")

# Extracting the Space from the name String

# print(name[6:7:1], "....extracting the space from nameString")


# Extracting the "erm" from the name String

# print(name[8:11:1], "...extracting the erm from nameString")


# -----------String Conversion (Taking a set of characters out of String )---------

# Note : You cannot convert a String value like "fuck" to an integer (Remember that)

# 1. Number to String Conversion

number_a = 12
string_a = str(number_a)
print(string_a, type(string_a), "...Number to String")


# 2. String to Number Conversion (Remember you cannot convert a Alphabet/ Special Symbol to a Number)

string_b = "100"
number_b = int(string_b)
print(number_b, type(number_b), "... String to Number")


# 3 & 4. (Number/ String) to Boolean
number_c1 = 12
number_c2 = 0
number_c3 = 0.0
number_c4 = 100.3

string_c1 = "Pushan"
string_c2 = ""

boolean_c1 = bool(number_c1)
boolean_c2 = bool(number_c2)
boolean_c3 = bool(number_c3)
boolean_c4 = bool(number_c4)


print(boolean_c1, "...Number to Boolean_1")

print(boolean_c2, "...Number to Boolean_2")

print(boolean_c3, "...Number to Boolean_3")

print(boolean_c4, "...Number to Boolean_4")


boolean_c5 = bool(string_c1)
boolean_c6 = bool(string_c2)

# print("----------------------------------")

print(boolean_c5, "....String to Boolean_1")

print(boolean_c6, "....String to Boolean_2")


# Note: We have only discussed around Numbers, Boolean and Strings . We will discuss about List, Tuples and Range later in detail
