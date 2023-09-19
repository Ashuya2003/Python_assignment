user_input = input("Enter a month (e.g., January): ").capitalize()

if user_input in ["September", "October", "November"]:
    print("The season is Autumn.")
elif user_input in ["December", "January", "February"]:
    print("The season is Winter.")
elif user_input in ["March", "April", "May"]:
    print("The season is Spring.")
elif user_input in ["June", "July", "August"]:
    print("The season is Summer.")
else:
    print("Invalid input. Please enter a valid month.")
