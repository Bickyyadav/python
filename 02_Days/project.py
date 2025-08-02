print("Welcome to the tip calculation")
TotalBill = int(input("what was the total bill you have to pay?"))
PrecentageToPay=int(input("how much tip i would you want to pay? 10 12 or 15 percentage"))
ActualBillWithPercentage=TotalBill * (PrecentageToPay/100)
PeopleToPay=int(input("How many people do you want to split?"))
print(int(ActualBillWithPercentage)/int(PeopleToPay))



