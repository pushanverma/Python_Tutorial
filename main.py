







# 4.4------ Dictionary(Objects , its just that Keys must be in Double Quotes )------

employee ={
    "name" :"Pushan",
    "empId": 123456,
    "intern" : False, 
    "hobbies" :["Badminton", "Watching Movies", "Listening to Music", "Walking"]
}

print(employee, type(employee) ,"...Object")

#Inserting a New key in Object 


# Deleting a Key in Object 


# Accessing a Key in Object 


# Changing the Data of a particular key in Object 








# 4.5 -----Sequence Type (List , Tuple and Range)-----


# 4.5.1 List ( Array )


# Only Numbers 
list_a = [10,30,20];
# print(list_a, type(list_a) ,"....list a");

# Only Boolean Values 
list_b =[True , False , False , True];

# Only String values 
list_c =["Hello","my","is","Pushan","Verma"];


#Array inside Array 
list_d =[[10,20],[30,40],[50,60]];


#Objects inside Array 

obj1 ={
    "name" :"Pushan",
    "age": 25,
    "is_Student": True 
}

obj2={

}

list_e =[]



# 
list_e =[10,True, 20, "Pushan", ];







# 4.5.2 Tuple






# 4.5.3 Range 



# 4.6 -------Mix of List and Dictonary--------
# (i.e Array inside Object and Objects inside Array )


# 4.6.1 Array inside Object 





# 4.6.2 Object inside Array 





# 4.7 ------Sets(Stores Distinct Values)-----




#------------------------------------------------------------------------------------------------------













# 4.4------ Dictionary(Objects , its just that Keys must be in Double Quotes )------

employee = {
    "name": "Pushan",
    "empId": 123456,
    "intern": False,
    "hobbies": ["Badminton", "Watching Movies", "Listening to Music", "Walking"],
    "fav_employee": {
        "name": "Bosu Bade Babu",
        "empId": 69,
    },
}

# Checking the type of Employee - Dictionary
# print(type(employee), "....employee")

# Accessing the name of the employee
# print(employee["name"], "...Dictionary / Object")

# Accessing the name of Favourite employee
# print(employee["fav_employee"]["name"], "....fav employee")

# Accessing the first Hobby of the employee
# print(employee["hobbies"][1], ".....Hobby no. 1")


# 4.5------ Sequence Type ------


# 4.5.1  List (Array that can be modified i.e Mutable)


# Only Numbers
list_a = [10, 30, 20]
# print(list_a, type(list_a) ,"....list a");

# Only Boolean Values
list_b = [True, False, False, True]

# Only String values
list_c = ["Hello", "my", "is", "Pushan", "Verma"]


# Array inside Array
list_d = [[10, 20], [30, 40], [50, 60]]


# Object inside Array
list_e = [
    {"name": "Pushan", "age": 25},
    {"name": "Bosu Bade ", "age": 28},
    {"name": "Dakshesh Gandhe ", "age": 24},
]


# Mix of everything in Array(Number , Boolean Value , String , Object , Array )
list_f = [
    11,
    12,
    True,
    False,
    "Pushan",
    "Verma",
    {"emp_id": 12345, "emp_name": "Bosu Bade Babu"},
    [[1, 2], [3, 4, 5], [6, 7]],
]


# 4.5.2 Tuple(Tuple is also an Array which cannot be modified i.e Immutable)

# Main Difference is in List we use [] and in Tuple we use ()

tuple_a = (10, 20, 30, 40)

tuple_b = ("Pushan ", "Verma ", "is ", "my ", "name ")

tuple_c = (
    {
        "name": "Pushan Verma",
        "age": 25,
        "job": "AV Tech ",
    },
    {"name": "Dakshesh Singh", "age": 24, "job": "Campus Well Rec"},
    {"name": "Dheeraj Kandikattu", "age": 26, "job": "Don's"},
)


# 4.5.3 Range

