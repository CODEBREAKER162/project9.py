# students_id = list()
# while True:
#     student = input("Enter your id:")
#     if student.lower() == "done":
#         break
#     students_id.add(student)
#     print("Students id information")
#     print(students_id)
    


grocery_bag = set()
while True:
    grocery_items = input("Enter what all items are required:")
    if grocery_items.lower() =="done":
        break
    if grocery_items in grocery_bag:
        print("The entered item is already in bag")
    else:
        grocery_bag.add(grocery_items)
        print("Added grocery new item")


user = input("Enter ok if you want summary of your list")
if user.lower=="ok":
      print("Summary of our set of items",grocery_bag)
else:
      print("Thank you")    




        

    




       
