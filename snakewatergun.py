import random

no_of_round = 10
choices = ["Snake", "Water", "Gun"]



computer_point = 0
human_point = 0

while no_of_round != 0:

    computer = random.choice(choices)
    print("1 for Snake\n2 for Water\n3 for Gun")
    human_input = input("What's your choice: ")
    if human_input == 1:
        human = "Snake"
    elif human_input == 2:
        human = "Water"
    else:
        human = "Gun"

    if computer == "Snake" and human == "Snake":
        print("This round tied !")
        print(f"Your guess {human} and computer guess is {computer} \n")
        print(f"Computer_point is {computer_point} and your point is {human_point} \n ")

    elif human == "Snake" and computer == "Gun":
        computer_point = computer_point + 1
        print(f"Your guess {human} and computer guess is {computer} \n")
        print("Computer wins 1 point \n")
        print(f"Computer_point is {computer_point} and your point is {human_point} \n ")

    elif human == "Snake" and computer == "Water":
        human_point = human_point + 1
        print(f"Your guess {human} and computer guess is {computer} \n")
        print("Human wins 1 point \n")
        print(f"Computer_point is {computer_point} and your point is {human_point} \n")

    elif computer == "Water" and human == "Water":
        print("This round tied !")
        print(f"Your guess {human} and computer guess is {computer} \n")
        print(f"Computer_point is {computer_point} and your point is {human_point} \n ")

    elif human == "Water" and computer == "Snake":
        computer_point = computer_point + 1
        print(f"Your guess {human} and computer guess is {computer} \n")
        print("Computer wins 1 point \n")
        print(f"Computer_point is {computer_point} and your point is {human_point} \n ")

    elif human == "Water" and computer == "Gun":
        human_point = human_point + 1
        print(f"Your guess {human} and computer guess is {computer} \n")
        print("Human wins 1 point \n")
        print(f"Computer_point is {computer_point} and your point is {human_point} \n")

    elif computer == "Gun" and human == "Gun":
        print("This round tied !")
        print(f"Your guess {human} and computer guess is {computer} \n")
        print(f"Computer_point is {computer_point} and your point is {human_point} \n ")

    elif human == "Gun" and computer == "Snake":
        human_point = human_point + 1
        print(f"Your guess {human} and computer guess is {computer} \n")
        print("Human wins 1 point \n")
        print(f"Computer_point is {computer_point} and your point is {human_point} \n")

    elif human == "Gun" and computer == "Water":
        computer_point = computer_point + 1
        print(f"Your guess {human} and computer guess is {computer} \n")
        print("Computer wins 1 point \n")
        print(f"Computer_point is {computer_point} and your point is {human_point} \n ")

    else:
        print("You have entered wrong  input. Check it out\n")

    no_of_round = no_of_round - 1
    print(f"{no_of_round} left out of 10\n")

if computer_point > human_point:
    print(f"Computer won by {computer_point - human_point} points\n")
    print(f"Your point is {human_point} and computer point is {computer_point}\n")

elif computer_point < human_point:
    print(f"Human won by {human_point - computer_point} points\n")
    print(f"Your point is {human_point} and computer point is {computer_point}\n")

else:
    print("The conclusion is a TIE ! Play Again, maybe.")
