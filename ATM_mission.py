balance = 10000
correct_pin ="9398730"
tries = 0
def show_menue():
   global balance
while true:
          enter_choice = input("Select any of one choice in 1/2/3/4")
print("/n 1. CHECK BALANCE")
        print("2. CASH WITHDRAW")
        print("3. CASH DEPOSITE")
        print("4. MENUE")
        if enter_choice == 1:
          print("Checking your balance...")
          print("BALANCE is ${balance}")
        elif enter_choice ==2:
          
            cash = float(input("Enter cash to be withdraw"))
            if balance >= cash:
             balance -=cash
             print("Withdrawed amount is ${cash}")
            else:
             print("Entered cash is not sufficent in you ${balance}")
        elif enter_choice ==3:
           print("Enter amount of cash to be deposited")
           balance +=cash
           print("Now your ner balance is ${balance}")
        elif enter_choice == 4:
           print("Thank you for using our ATM")
           break
        else:
           print("Entered wrong choice")   
           break
    else:
     while tries < 3:
      pin = input("Enter your pin")
       if pin == correct_pin:
        print("Unlocked")
       
       print("Enter pin is wrong")  
       tries += 1     
    if correct_pin ==3:
     print("Too many attempts try again after 24 hours")
    
              
           
              

             
           
             



    

    
       



        
        


                    

            

            