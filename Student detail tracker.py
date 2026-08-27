
details = []

while True:
    print("\n----------Personal Details----------")
    try:
        opt = int(input("1. Create New Account\n2. View Existing Accounts\n3. Edit Existing Record\nEnter your Choice(1/2/3): "))
    except ValueError:
        print("Invalid Input. Please try again.")
        continue

    if opt == 1:
        print("\n----------Creating New Account----------")
        m = int(input("Enter How student would you like to enter: "))
        for p in range(m):
            name = input("Enter Name of Student: ")
            age = int(input("Enter Age of Student: "))
            roll_no = input("Enter Student's roll no: ")
            course = input("Enter student's course: ")
            phone = int(input("Enter Student's Phone Number: "))
            
            student = {
                "Name": name, 
                "Age": age,
                "Roll Number": roll_no, 
                "Course Of Study": course, 
                "Phone Number": phone
            }

            details.append(student)
            print("----------Account Successfully Created!----------")
            print(student)

    elif opt == 2:
        print("\n----------Existing Accounts----------")
        if not details:
            print("No accounts have been created yet.")
        else:
            for q in details:
                print(q)

    elif opt == 3:
        print("\n----------Editing Record Details----------")
        print("1.Name\n2.Age\n3.Roll Number\n4. Course Of Study\n5. Phone Number")
        search = input("Enter student name to search for: ")
        
        
        if not details:
            print("No student records exist to edit.")
        else:
            if details["Name"] == search:
                try:
                    n = int(input("How many fields would you like to edit? "))
                    for i in range(n):
                        record = input("Enter field name exactly (e.g., Name, Age, Roll Number): ")
                        entry = input("Enter new detail: ")
                        
                        if record in ["Age", "Phone Number"]:
                            details[record] = int(entry)
                        else:
                            details[record] = entry
                    print("Updated Details:", details)
                except ValueError:
                    print("Invalid input number.")
            else:
                print("Student not found.")

    stop = input("\nEnter STOP to end program, GO to repeat program again: ").upper()
    if stop == "STOP":
        break


print("Program exited successfully.")
