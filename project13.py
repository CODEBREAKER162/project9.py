print("This is marks calculator")
students = []
while True:
    name = input("Enter your name(or type stop to finish):")
    if name.lower() == "stop":
        break
    marks_input = input("Enter your marks:")
    try:
        marks_input_int = int(marks_input)
        if marks_input_int < 0:
            print("Please enter a non-negative number for marks")
            continue
    except ValueError:
        print("Please enter a valid number for marks")
        continue
    marks_input = marks_input_int
    
    if marks_input >= 90:
        grade = "O"
    elif marks_input >= 80:
        grade = "A+"    
    elif marks_input >= 70:
        grade = "A"    
    elif marks_input >= 60:
        grade = "B+"    
    elif marks_input >= 50:
        grade = "B"    
    elif marks_input >= 40:
        grade = "C+"    
    else:
        grade = "F"    
    students.append((name, marks_input, grade))
    print(f"{name}, your marks are {marks_input} and your grade is {grade}")
    print("_"*30)

print("Final report")
for student in students:
    print("name:", student[0])
    print("marks:", student[1])
    print("Grade:", student[2])
    print("_"*30)


