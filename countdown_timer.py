import time
import sys

my_timer = int(input("Enter the time ine seconds: "))

for x in range(my_timer, 0, -1):
    seconds = x % 60
    minutes = int(x / 60) % 60
    hours = int(x / 3600)
    sys.stdout.write(f"\r{hours:02}:{minutes:02}:{seconds:02}")
    sys.stdout.flush()
    time.sleep(1)
    
sys.stdout.write("\rTIME's UP!\n")