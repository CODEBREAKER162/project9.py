# ------- ❶ Helper functions -------
def square_area(side):
    return side * side                   # or side ** 2

def square_perimeter(side):
    return 4 * side

def rectangle_area(length, width):
    return length * width

def rectangle_perimeter(length, width):
    return 2 * (length + width)

def triangle_area(base, height):
    return 0.5 * base * height

def triangle_perimeter(a, b, c):
    return a + b + c
# -----------------------------------

while True:                                              # Main menu loop
    print("\n=== SHAPE CALCULATOR ===")
    print("1. Square")
    print("2. Rectangle")
    print("3. Triangle")
    print("4. Exit")

    shape_choice = input("Choose a shape (1‑4): ")

    # ---------- Square ----------
    if shape_choice == "1":
        print("\nYou chose SQUARE")
        calc_choice = input("Press 1 for Area, 2 for Perimeter: ")

        if calc_choice == "1":
            s = float(input("Enter side length: "))
            print("Area of square =", square_area(s))
        elif calc_choice == "2":
            s = float(input("Enter side length: "))
            print("Perimeter of square =", square_perimeter(s))
        else:
            print("Invalid choice!")

    # ---------- Rectangle ----------
    elif shape_choice == "2":
        print("\nYou chose RECTANGLE")
        calc_choice = input("Press 1 for Area, 2 for Perimeter: ")

        if calc_choice == "1":
            l = float(input("Enter length: "))
            w = float(input("Enter width : "))
            print("Area of rectangle =", rectangle_area(l, w))
        elif calc_choice == "2":
            l = float(input("Enter length: "))
            w = float(input("Enter width : "))
            print("Perimeter of rectangle =", rectangle_perimeter(l, w))
        else:
            print("Invalid choice!")

    # ---------- Triangle ----------
    elif shape_choice == "3":
        print("\nYou chose TRIANGLE")
        calc_choice = input("Press 1 for Area, 2 for Perimeter: ")

        if calc_choice == "1":
            b = float(input("Enter base   : "))
            h = float(input("Enter height : "))
            print("Area of triangle =", triangle_area(b, h))
        elif calc_choice == "2":
            a = float(input("Enter side a : "))
            b = float(input("Enter side b : "))
            c = float(input("Enter side c : "))
            print("Perimeter of triangle =", triangle_perimeter(a, b, c))
        else:
            print("Invalid choice!")

    # ---------- Exit ----------
    elif shape_choice == "4":
        print("Goodbye! ✨")
        break                                            # leave the while‑loop

    else:
        print("Invalid shape choice! Please try again.")


