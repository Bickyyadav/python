# if condition:
#     if condition:
#         do this 
#     else:
#         do this
# else: 
#     do this

#Nested if else statement 
    # height = int(input("Enter your height"))
    # Age = int(input("enter your age"))

    # if height >120:
    #     print("can Ride")
    #     if Age > 18:
    #        print("you have to pay $12")
    #     else:
    #         print("you have to pay $7")
    # else: 
    #     print("cannot ride")


#elif statement 
    # if condition:
    #     do A
    # elif condition:
    #     do B
    # else:
    #     do this


Age = int(input("enter your age"))
bill = 0

if Age > 18:
    print("you can pay $8")
    bill = 2
elif Age >15:
    print("you have to pay $5")
    bill=3
elif Age >13:
    bill = 5
    print("you have to pay $5")
else:
    print('you have to pay the $4')

wants_photo = input("Do you want to take photo or not ")
if wants_photo == "y":
    bill = bill +3 
    print(f"total bill is {bill}")
else:
    print(f"your bill is {bill}")

