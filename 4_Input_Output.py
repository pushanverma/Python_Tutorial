# Taking Input from user in terminal

name = input("Enter your name =")
age = input("Enter age =")
employee_id = input("Enter employee_id =")


# note: Remember that input always return a String . So if you want to use as Number dont forget to convert it from String to Number

print(type(name), "....type of name")
print(type(age), "....type of age")
print(type(employee_id), "....type of employee_id")


# Output
# So there are two methods to output
# 1. To break the strings in between
# 2. Formatted String


# 1. Breaking the string in between
print(
    "Hello my name is -",
    name,
    " , my age is -",
    age,
    "and my employee id is -",
    employee_id,
)

# 2. Formatted String

print(
    f"Hello my name is - {name} , my age is - {age} and my employee id is - {employee_id}"
)
