# # # print("Hello World!")
# # # print("Good Morning☀️")
# # # name = "Optimus"
# # # print(name)------>this is variable type 
# # # age = 20
# # # print(age)


# # #for i in range(1,8):
# #  #    print(i,"Hello World!")
# # # for i in range(5):
# # # print("Hello world")




# # #  balance= 10000
# # # print("welcome")
# # # pin = "93987"
# # # entered_pin = input("Enter your pin")
# # # if entered_pin != pin:
# # #         print("Entered pin is incorrect")
# # #         exit()
# # #         while True:
# # #                 print("\n Menue")
# # #                 print("1 . check balance")
# # #                 print("2 . Withdraw cash")
# # #                 print("3. Deposit")
# # #                 print("4. exit")
# # #                 enter_choice = input("Enter your choice (1/2/3/4)")
# # #                 if enter_choice ==1:
# # #                     print("checking the balance amount" )
# # #                     print(balance)
# # #                 elif enter_choice == 2:
# # #                   amount = float(input("Enter the amount to be withdrawed"))
# # #                   if amount > balance:
# # #                       print("Insufisient balance")
# # #                   else:
# # #                       balance -= amount

# # #                       print("WWith drawel${amount} sucessfully ")
# # #                       print("Remaining balance ${balance}")
# # #                 elif enter_choice ==3:
# # #                     amount = float(input("Enter depositing amount"))
# # #                     amount += balance
# # #                     print("Now balance amount is ${amount},new balance is ${balance}")
# # #                 elif enter_choice ==4:
# # #                      print("Thank you for using our Bank")
# # #                 else:
# # #                      print("Wrong choice")
                    
   

# # # for i in range(0,10):
# # #     if i == 5:
# # #         break
# # #     print(i)
# # #     if i ==3:
# # #         continue
# # #     print(i)
    



# # def greet(name):
# #     print("Hello World",name)
# # greet("Harish")
# # greet("Geetha")
# # greet("Babitha")
    


# def add(a,b):
#     return a + b
# result =add(2,6)
# print("add",result)
# #







print('This is for Perimeter of Rectangle')
def calculate_perimeter(length,berth):
    perimeter = 2 * (length + berth)
    return perimeter
L = float(input("Enter length of rectangle:"))
W = float(input("Enter width of the rectangle:"))
result = calculate_perimeter(L,W)
print("This is Perieter of rectangle",result,"units")
print("This is for Area of Rectangle")
def calculate_area(length,width):
    area = length * width
    return area
L=float(input("Enter length of rectangle:"))
B=float(input("Enter width of rectangle:"))
result = calculate_area(L,B)
print("The area of rectangle",result)
print("This is perimter of triangle")
def calcuate_square_perimeter(side):
    perimter = 4 * side
    return perimter
S=float(input("Enter the side of square:"))
result = calcuate_square_perimeter(S)
print("This is the perimeter of Square ",result,"units")
print("This is area of square")
def mesure_square_area(side):
    area = side **2
    return area
S=float(input("Enter the side of square"))
result = mesure_square_area(S)
print("Thisis the area of the sqaure",result,"units")
print("This is perimeter of triangle ")
def calculate_triangle_perimeter(side1,side2,side3):
    perimeter = side1 + side2 + side3
    return perimeter
S1 = float(input("Enter the value of side one:"))
S2 = float(input("Enter the value of side two:"))
S3 = float(input("Enter the value of side three:"))
result = calculate_triangle_perimeter(S1,S2,S3)
print("The perimeter of the triangle is ",result,"units")
print("This is area of triangle")
def calculate_triangle_area(base,height):
    area = 1/2*(base * height)
    return area
B = float(input("Enter the base value of triangle:"))
H = float(input("Enter the value of height:"))
result = calculate_triangle_area(B,H)
print("This is the Area of Triangle",result,"units")







fruits = ["Bannana", "Apple", "Mango", "Goa", "Pineapple"]
fruits.append("Orange")
fruits.insert(0,"Graps")
fruits.remove("Bannana")
fruits.pop(2)
fruits.sort()
fruits.reverse()
fruits.count("Apple")
fruits.index("Goa")
fruits.clear()
# fruits.extend(["Kiwi", "Papaya"])  # Example of extending the list with more items
# fruits = ["Kiwi", "Papaya"]  # Resetting the list after clearing

print(fruits)








# # fruits = ["Apple","Bannana","Goa"]
# # for fruit in fruits:
# #     print("I like",fruit)
# #     print(len(fruit),"Lettters in",fruit)

# fruits = ["Apple","Bannana","Goa"]
# i =0
# while i < len(fruits):
#     print(fruits[i])
#     i +=2--->skipping each second item

# word ="Charith"-----> string with for loop
# for words in word:
#     print(words)



# word ="charith"
# i =0----> this is while loop using while loop
# while i<len(word):
#     print(word[i])
#     i+=1
    
