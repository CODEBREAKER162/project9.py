from_station= input("Enter from station:")
to_station = input("Enter to station:")
print("From staion",from_station,"---->",to_station,"To")

def passenger_details(index):
    print(f"\nEnter details for Passenger {index}:")
    name = input("Name: ")
    age = input("Age: ")

    while True:
        phone = input("Phone Number (10 digits): ")
        if len(phone) == 10 and phone.isdigit():
            break
        else:
            print("❌ Invalid phone number. Please enter exactly 10 digits.")

    # Choose coach
    print("Select coach type:")
    print("1. AC (₹1000)")
    print("2. Sleeper (₹700)")
    print("3. General (₹400)")

    while True:
        coach_choice = input("Enter coach choice (1/2/3): ").strip()
        if coach_choice == "1":
            coach = "AC"
            price = 1000
            break
        elif coach_choice == "2":
            coach = "Sleeper"
            price = 700
            break
        elif coach_choice == "3":
            coach = "General"
            price = 400
            break
        else:
            print("❌ Invalid coach choice. Please enter 1, 2, or 3.")

    return [name, age, phone, coach, price]

# 🌀 Main Booking Loop
while True:
    print("\n🚆 Booking Options:")
    print("1. Tatkal Ticket")
    print("2. Pre Booking")
    print("3. Live Booking")
    print("4. Exit")

    choice = input("Enter your choice (1/2/3/4): ").strip()

    if choice == "4":
        print("👋 Exiting Booking System. Thank you!")
        break

    if choice in ["1", "2", "3"]:
        print("\n✅ Booking selected.")
        all_passengers = []
        total_price = 0
        passenger_index = 1

        while True:
            passenger = passenger_details(passenger_index)
            all_passengers.append(passenger)
            total_price += passenger[4]
            passenger_index += 1

            another = input("Add another passenger? (yes/no): ").strip().lower()
            if another != "yes":
                break

        print("\n🎫 Booking Summary:")
        for p in all_passengers:
            print(f"Name: {p[0]}, Age: {p[1]}, Phone: {p[2]}, Coach: {p[3]}, Price: ₹{p[4]}")
        
        print(f"\n💰 Total Amount to be Paid: ₹{total_price}")

        again = input("\nDo you want to book another set of tickets? (yes/no): ").strip().lower()
        if again != "yes":
            print("👍 Thank you for booking. Have a great day!")
            break

    else:
        print("❌ Invalid input. Please choose 1, 2, 3, or 4.")



    






        
        
        




            

        
        








