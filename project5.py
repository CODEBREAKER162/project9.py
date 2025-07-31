print("welcome")
correct_password = "INdian777"
tries = 0

while tries<3:
    password = input("Enter you password:")
    if password == correct_password:
        print("unlocked")
        break
    else:
        print("not unlocked")
        tries += 1
    if tries ==3:
        print("too many attempts")
        