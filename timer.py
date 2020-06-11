# To use this script, install:
# python -m pip install threading

# Import the module
import threading

# Define a function timer

def timer():
    print("Time is out!!!")

# Define variables

upUntil = 5.0
timeUp = threading.Timer(upUntil, timer)

timeUp.start()