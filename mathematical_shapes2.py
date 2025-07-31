def calculate_rectangle_perimeter(length,berth):
    return  2 *(length + berth)
def calculate_rectangle_area(length,berth):
    return length * berth
def calculate_square_perimeter(side):
   return 4 * side
def caculate_square_area(side):
    return side ** 2
def calculate_triangle_perimeter(a,b,c):
    return a + b + c
def calculate_triangle_area(base,height):
    return 1/2 * (base * height)

while True:
    print("/n 1. Rectangle")
    print("2.Square")
    print("3.Trianle")
    shape_choice = int(input("Enter the shape choice(1/2/3) to be calculated"))

#-----------RECTANGLE----------------------------------

    if shape_choice ==1:
        choice = int(input("For calculating ,enter 1 for perimeter and 2 for area"))
        if choice ==1:
            print("Perimeter of traingle")
            L=float(input("Enter the length"))
            B=float(input("Enter the breth"))
            print("calculaing perimeter of recatangle")
            print("This is perimeter of traingle",calculate_rectangle_area(L,B),"units")
        elif choice ==2:
            print("Area of triangle")
            L=input(print("Entered length"))
            B=input(print("Enter breth"))
            print("This is Area of rectangle",calculate_rectangle_area(L,B),"units")

         
        else:
            print("entered wrong choice")   

            #-------------SQUARE------------------------------

    elif shape_choice ==2:
        print("Selected shape square")            
        int(input("For calculating , enter 1 for perimeter and 2 for area"))
        if choice ==1:
            print("Square perimeter")
            S = float(input("Enter value of side"))
            print("This is perimeter of Square",calculate_square_perimeter(S),"units")
        elif choice ==2:
            print("Area of square")    
            S=float(input("Entered value of side"))
            print("This is area of square",caculate_square_area(S),"units")   
        else:
            print("Entered wrong choice")  
    elif shape_choice ==3:
        print("Entered shape is TRIANGLE")          
        int(input(("Click 1 for Perimeter and 2 for Area")))
        if choice ==1:
            print("Perimeter of Triangle")
            A=float(input("Enter value of a"))
            B=float(input("Enter the value of b"))
            C=float(input("Enter the value of c"))
            print("The perimeter of triangle",calculate_triangle_perimeter(A,B,C),"units")
        elif choice ==2:
            print("Area of triangle")    
            B=float(input("Enter base value"))
            H=float(input("Enter height value"))
            print("The Area of triangle",calculate_triangle_area(B,H),"units")
        else:
            print("Entered wrong choice")    
    else:
        print("Entered wrong shape number")
        






    