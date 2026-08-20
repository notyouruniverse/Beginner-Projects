
to_do = []

while True:
    print("\n----------To do list----------")
    print("1. Enter Tasks\n2.View Pending Tasks\n3.Finish Tasks")
    x = int(input("Choose an option (1/2/3): "))
    
    if x == 1:
        n = int(input("Enter how many tasks you wish to add: "))
        for i in range(n):
            task = input("Enter Task: ").title()
            to_do.append(task)
        print(to_do)
        continue

    elif x == 2:
        print(to_do)

    elif x == 3:
        task = input("Enter Task you would like to Finish: ").title()
        to_do.remove(task)
        print("Task completed successfully!")
        print(to_do)

    p = input("Enter STOP to exit, Enter GO to restart program: ").upper()
    if p == "STOP":
        break



    
