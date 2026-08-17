while True:

    print("----------Personal Details----------")
    try:
        opt = int(input("""1. Create New Account\n2. View Existing Accounts\n3. Edit Existing Record\nEnter your Choice(1/2/3): """))
    except ValueError:
        print("Invalid Input. Please try again.")
        continue

    if opt ==  1:
        print("\n----------Creating New Account----------")
        name = input("Enter Name of Student: ")
        age = int(input("Enter Age of Student: "))
        roll_no = input("Enter Student's roll no: ")
        course = input("Enter student's course: ")
        phone = int(input("Enter Student's Phone Number: "))
        details = {"Name": name, "Age": age, "Roll Number": roll_no, "Course of Study": course, "Phone Number": phone}

        print("----------Account Successfully Created!----------")
        print(details)

    elif opt == 2:
        with open('handbook',"w") as file:
            file.write(str(details))

        print("\n----------Existing Accounts----------")
        with open('handbook',"r") as file:
            content = file.read()
            print(content)

    elif opt == 3:
        print("\n----------Editing Record Details----------")
        record = input("Enter Record you would like to edit: ")
        entry = input("Enter new detail: ")
        details[record] = entry
        print(details)

    stop = input("Enter STOP to end program, GO to repeat program again: ").upper()
    if stop == "STOP":
        break
