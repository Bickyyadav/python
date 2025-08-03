import random

EASY_LEVEL=10
HARD_LEVEL=5

def check_Answer(user_guess,actual_guess):
    if user_guess > actual_guess:
        print("to hight")
    elif user_guess <actual_guess:
        print("Too low")
    else:
        print(f"your go it ! the answer was {actual_guess}" )


#function to  set difficulty
def set_difficulty():
    level = input("choose a difficulty .Type 'easy' or 'hard' ").lower()
    if level =="easy":
        return EASY_LEVEL
    else:
        return  HARD_LEVEL





# choose the number between 1 to 100
print("welcome to the guessing game 1 to 100")
answer = random.randint(1,100)

# let the user guess the number
guess = int(input("enter the number between 1 to 100"))
turns= set_difficulty()
print(f"the number of attempts left to guess the number {turns}")

# function check the user guess the number against actual number 


#track teh number to run to reduce by 1 if they get it wrong

#Repeat the guessing functionality if they get it wrong.