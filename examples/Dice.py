import random
import display

display.scroll("Ready")
while True:
    input("enter to roll the dice..")
    r = random.randint(1, 6)
    print("rolled a", r)
    display.scroll(r)
