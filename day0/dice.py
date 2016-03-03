from random import randint

how_many_dice = int(input("How many dice would you like to roll?"))
sides_of_dice = int(input("How many sides should each die have?"))

for count in range(how_many_dice):
    print(randint(1, sides_of_dice))
