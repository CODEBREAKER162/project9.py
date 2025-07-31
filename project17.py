#Using tupples
students = [
    ("charith" , 18 ,   "A+"),
    ("Arun", 18, "A"),
    ("Chinni",19, "O")


]
for student in students:
    
    name , age , grade = student
    print("-"*30)
    print("Name is :",name)
    print("Age is :",age)
    print("Grade is :",grade)
    
