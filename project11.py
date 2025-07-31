balance = 5000
pin = "1234"
correct_pin = input("Enter your pin:")
if correct_pin == pin:
   
    while True:
        print("\n Menue")
        print("1. Check balance")
        print("2. Cash withdraw")
        print("3. Deposite")
        print("4. Exite")
        choice = int(input("Enter any choice of 1-4"))
        if choice ==1:
            print("Your balance is",balance)
        elif choice ==2:
            amount = int(input("Enter the amount you want to withdraw"))
            if amount < balance:
                print("Yor amount is withdrawed sucessfully",amount)
            else:
                print("Insufficient balance")    
        elif choice ==3:
            deposit_amount = int(input("Enter amount you want to deposit:"))        
            balance +=deposit_amount
            print("Your amount is deposited sucessfullly",deposit_amount)
            print("Your new balance is ",balance)
        elif choice ==4:
            print("Thank you for using our bank") 
            break   
        else:
            print("Entered wrong choice ")    
else:
    print("Entered pin is incorrect,try again")            



        

