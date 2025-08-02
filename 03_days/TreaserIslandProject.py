print("Welcome to Treasure island. Your mission is to find the treasure")
path =input("enter left or right to move")
if(path =="right"):
    print("Game Over")
elif(path =="left"):
    bath = input("enter do you want to swim or wait")
    if bath =="swim":
        print("Game Over")
    else:
        door=input("which door you want to enter red yellow blue")
        if door == "red" or door ==  "blue":
            print("Game over")
        elif door =="yellow":
            print("Your won Hurry up!")  
        else:
            print("you have entered wrong input")
else:
    print("you have entered wrong input")