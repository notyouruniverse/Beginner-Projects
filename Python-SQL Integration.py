import sqlite3

connection = sqlite3.connect("blank_database.db")
cursor = connection.cursor()
db_name = input("Enter Table name: ")

query = f"""CREATE TABLE {db_name}(
            Name VARCHAR(30),
            Roll_Number INT(2) PRIMARY KEY,
            Physics INT(3),
            Chemistry INT(3),
            Mathematics INT(3),
            Computer_Science INT(3),
            English INT(3)
            );"""

while True:
    print("""\n1. Create a Table and Add Records" 
2. Edit records" 
3. Delete Records" 
4. Edit Table Columns
5. Drop Available Tables
6. Evaluate Total and Percentage
7. Enter Custom Code""")
    try:
        opt = int(input("Enter an option: "))
    except ValueError:
        print("Input a valid Data Type!!")
        continue

    if opt == 1:
        try:
            cursor.execute(query)
            connection.commit()
            cursor.execute(f"SELECT * FROM {db_name}")
            rows = cursor.fetchall()
            print(rows)
        except sqlite3.OperationalError:
            print("Table with same name exists. Try Another name.")
        
        n = int(input("\nEnter how many records you wish to add: "))
        for i in range(n):
            try:
                name = input("\nEnter Student Name: ").title()
                roll_no = int(input("Enter Student Roll Number (Avoid repetitive numbers): "))
                physics = int(input("Enter Physics Marks: "))
                chemistry = int(input("Enter Chemistry Marks: "))
                math = int(input("Enter Mathematics Marks: "))
                cs = int(input("Enter Computer Science Marks: "))
                eng = int(input("Enter English marks: "))
            except ValueError:
                print("Enter valid data type!!")
                continue
            
            try:
                cursor.execute(f"INSERT INTO {db_name} VALUES ('{name}','{roll_no}','{physics}','{chemistry}','{math}','{cs}','{eng}')")
                connection.commit()
            except sqlite3.IntegrityError:
                print("Student with given Roll Number already exists. Skipping this record.")
            cursor.execute(f"SELECT * FROM {db_name}")
            print("---------- RECORD SAVED! ----------")
            print(cursor.fetchall())


    elif opt == 2:
        m = int(input("\nEnter how many record you would like to edit: "))
        for j in range(m):
            try:
                record_name = input("Enter student name to edit: ").title()
                edit_record = input("Enter entry to be edited: ").title()
                new_record = input("Enter new record to be added: ")
                cursor.execute(f"UPDATE {db_name} SET {edit_record} = ? WHERE Name = ?",(new_record, record_name))
                connection.commit()
                cursor.execute(f"SELECT * FROM {db_name}")
                print(cursor.fetchall())
            except sqlite3.OperationalError:
                print("Invalid name or column name, Try again.")


    elif opt == 3:
        o = int(input("\nEnter how many record you wish to delete: "))
        cursor.execute(f"SELECT * FROM {db_name}")
        print(cursor.fetchall())
        for record in range(o):
            record_rn = int(input("Enter Roll Number of student you would delete: "))
            cursor.execute(f"DELETE FROM {db_name} WHERE Roll_Number = ?", (record_rn,))
            connection.commit()
            print("---------- RECORD DELETED! ----------")
        cursor.execute(f"SELECT * FROM {db_name}")
        print(cursor.fetchall())


    elif opt == 4:
        w = int(input("\nEnter number of columns you would like to add: "))
        for column in range(w):
            column_name = input("Enter new column name: ")
            try:
                cursor.execute(f"ALTER TABLE {db_name} ADD {column_name}")
                connection.commit()
            except sqlite3.OperationalError:
                print("Given column already exists. Skipping this record.")
            cursor.execute(f"SELECT * FROM {db_name}")
            print(cursor.fetchall())
            print("Message: Use Option 2 to enter values into empty records.")

    elif opt == 5:
        drop_table = input("Enter name of table to be dropped: ")
        warning = int(input("THIS ACTION IS NON-REVERSIBLE, ENTER 1 TO DROP, 0 TO REVERT: "))
        if warning == 1:
            cursor.execute(f"DROP TABLE {drop_table}")
            connection.commit()
        else:
            print(f"Table {db_name} is not dropped.")

    elif opt == 6:
        try:
            cursor.execute(f"ALTER TABLE {db_name} ADD Total")
            connection.commit()
            cursor.execute(f"UPDATE {db_name} SET Total = Physics + Chemistry + Mathematics + Computer_Science + English")
            connection.commit()
            cursor.execute(f"ALTER TABLE {db_name} ADD Percentage")
            connection.commit()
            cursor.execute(f"UPDATE {db_name} SET Percentage = total*0.2")
            connection.commit()
            cursor.execute(f"SELECT * FROM {db_name}")    
            print(cursor.fetchall())
        except:
            print("Total and Percentage have already been calculated.")

    elif opt == 7:
        custom_code = input("""Type your custom MySQL commands here: """)
        try:
            cursor.execute(custom_code)
            connection.commit()
            cursor.execute(f"SELECT * FROM {db_name}")    
            print(cursor.fetchall())
        except sqlite3.OperationalError:
            print("Incorrect query given, Input valid command.")

    else:
        print("Invalid Input, Try Again!!")


    indicator = int(input("\nPress 1 to continue, 0 to end program: "))
    if indicator == 0:
        print("Have a Good Day..!!! :>")
        break
   
