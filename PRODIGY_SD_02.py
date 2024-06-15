import random
guess = random.randint(1,100)
count = 1
your = int(input(f"Enter Guess No.{count}:"))
while(guess != your):
    if guess > your:
        print("Your guess is too low")
        count+=1
        
    elif guess < your:
        print("Your guess is too high")
        count+=1
        
    your = int(input(f"Enter Guess No.{count}:"))
print(f"The number was successfully guessed in {count} attempts")