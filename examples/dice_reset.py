import display
import random
import time

r = random.randint(1, 6)
while True:
    display.scroll(r)
    time.sleep(0.5)