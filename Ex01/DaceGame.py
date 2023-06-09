import random
import time

def hello():
    print("What is your name?")
    global name 
    name = input("> ")
    print(f"Hello, {name}!")

def dice():
    sum = 0
    print("Rolling the dice...")
    time.sleep(2)
    for i in range(1, 3):
        num = random.randrange(6)
        sum += num
        print(f"Die {i}: {num}")
        time.sleep(1)
    print(f"Total value: {sum}")
    judge(sum)

def judge(sum):
    if sum > 7:
        print(f"{name} won!")
    else:
        print(f"{name} lost.")

    
if __name__ == '__main__':
    hello()
    time.sleep(1)
    dice()