import display
import random
import time

display.scroll("Ready")
print("Ready")
r = random.randint(1, 6)
print(r)
while True:
    display.scroll(r)
    time.sleep(0.5)
