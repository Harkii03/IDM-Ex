import random
import time
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
    
if __name__ == '__main__':
    dice()