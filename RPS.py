print("Lets Play Rock-Paper-Scissor!")
rounds = int(input("Enter number of rounds you wish to play: "))


choice = ["Rock","Paper","Scissor"]
computer_points = 0
user_points = 0

for i in range(rounds):
    import random
    
    computer_choice = random.choice(choice)
    user_choice = input("Choose one: Rock, Paper or Scissor? ")

    if user_choice == "Rock" or user_choice == "rock" or user_choice == "ROCK" and computer_choice == "Rock":
        print("I chose Rock. We drew.")
        computer_points += 1
        user_points += 1
        print("My Score: ",computer_points)
        print("Your Score: ",user_points)

    elif user_choice == "Rock" or user_choice == "rock" or user_choice == "ROCK" and computer_choice == "Paper":
        print("I chose Paper. I get a point.")
        computer_points += 2
        print("My Score: ",computer_points)
        print("Your Score: ",user_points)

    elif user_choice == "Rock" or user_choice == "rock" or user_choice == "ROCK" and computer_choice == "Scissor":
        print("I chose Scissor. You get a point.")
        user_points +=2
        print("My Score: ",computer_points)
        print("Your Score: ",user_points)

    elif user_choice == "Paper" or user_choice == "paper" or user_choice == "PAPER" and computer_choice == "Rock":
        print("I chose Rock. You get a point.")
        user_points += 2
        print("My Score: ",computer_points)
        print("Your Score: ",user_points)

    elif user_choice == "Paper" or user_choice == "paper" or user_choice == "PAPER" and computer_choice == "Paper":
        print("I chose Paper. We Drew.")    
        user_points += 1
        computer_points += 1
        print("My Score: ",computer_points)
        print("Your Score: ",user_points)

    elif user_choice == "Paper" or user_choice == "paper" or user_choice == "PAPER" and computer_choice == "Scissor":
        print("I chose Scissors. I get a point.") 
        computer_points += 2
        print("My Score: ",computer_points)
        print("Your Score: ",user_points)

    elif user_choice == "Scissor" or user_choice == "scissor" or user_choice == "SCISSOR" and computer_choice == "Rock":
        print("I chose Rock. I get a point.")
        computer_points += 2
        print("My Score: ",computer_points)
        print("Your Score: ",user_points)

    elif user_choice == "Scissor" or user_choice == "scissor" or user_choice == "SCISSOR" and computer_choice == "Paper":
        print("I chose Paper. You get a point.")
        user_points += 2
        print("My Score: ",computer_points)
        print("Your Score: ",user_points)

    elif user_choice == "Scissor" or user_choice == "scissor" or user_choice == "SCISSOR" and computer_choice == "Scissor":
        print("I chose Scissor. We drew.")
        user_points += 1
        computer_points += 1
        print("My Score: ",computer_points)
        print("Your Score: ",user_points)
        
print("Your Final Score: ", user_points)
print("My Final Score: ",computer_points)

if user_points > computer_points:
    print("You Win.")
elif user_points == computer_points:
    print("We Drew.")
else:
    print("I win.")     

    




