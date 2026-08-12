while True:

    try:
        opt = int(input("""Choose an option:
        1 - Create a new password
        2 - View saved password
        Enter your option here: """))
    except ValueError:
        print("Choose a valid option.")
        continue

    if opt == 1:
        new_password = input("Enter new password here: ")
        confirm_password = input("Enter password again for confirmation: ")

        if new_password == confirm_password:
            with open("password_manager", "w") as file:
                file.write(new_password)
                print("Password saved successfully.")
        else:
            print("Password is not matching. Try again.")

    elif opt == 2:
        with open("password_manager", "r") as file:
            password = file.read()
            print(password)

    stop_or_continue = input(
        "Enter STOP to kill the program, enter GO to run it again: " ).upper()
    
    if stop_or_continue == "STOP":
        break