items_purchased = [" Apple",
                   "Grapes",
                   "SOocks",
                   "Shirt(USpollo)",
                   "Pants(USollo)",
                   "Shirt(uspollo)",
                   "Salt(3Kg)",
                   "Sos(2Litre)"
                   ,"Sugar(3Kg)",
                   "Rice(5Kg)",
                   "Oil(2lire)",
                     "Wheat(5Kg)",
                     "Pulses(2Kg)",]
total_cost = 0
print("----------------BILLING SYSTEM--------------------")

for item in items_purchased:
    print(f"Items purchased are :",item)
    cost = float(input("Enter cost of item:"))
    quantity = float(input("Enter quantity of item:"))
    
    total_price = cost * quantity
    print("Total cost of item ",item,"Rupees",total_price)
    total_cost += total_price
    print("------------------------TOTALL BILL-------------------")
    print("Total cost of al items purchased is :",total_cost,"Rupees")
    
