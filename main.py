import random

number_1 = int(input("enter the lowest number: "))
number_2 = int(input("enter the highest number: "))
number = random.randint(number_1, number_2)
print(number)
level = input("Which level you want to play(easy/hard)?: ").lower()
if level == "easy":
    times = 10
else:
    times = 5
game_on = True
while game_on:
    user = int(input("Enter the number you guess: "))
    if user == number:
        print("Wow! you done a great guess")
    elif user < number:
        print("The number you guessed is lesser than the actual guess\nplease give an another try ")
        times -= 1
        print(f"You only have {times} life")
    elif user > number:
        print("The number you guessed is greater than the actual guess\nplease give an another try ")
        times -= 1
        print(f"You only have {times} life")
    if times == 0:
        game_on = False
        print("You have running out of life")
