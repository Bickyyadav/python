print("Welcome to python pizza Deliveries")
size=input("whats size pizza do you want? S, M, L")
pepperoni = input("do you want pepperoni on pizza? y or n")
extra_cheese = input("do you want extra cheese on pizza? y or n")

bill = 0

if size == "s":
    bill+=15
elif size == "m":
    bill+=20
else:
    bill+=25

if pepperoni == "y":
    if size == "s":
        bill+=2
    else:
     bill+=3

if extra_cheese=="y":
    bill+=1

print(f"your final bill is ${bill}")




