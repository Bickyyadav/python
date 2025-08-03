#ask the user for input
# name=input("what is your name\n")
# price = int(input("what is your bit\n $")
# )

# bids={}
#save data to the dictionary {name:price}
# bids[name] = price

#whether user want to continue new bids or not
#compare the highest bit in dictionary
def find_highest_bidder(bidding_dictionary):
    winner=""
    highest_bid=0
    for i in bidding_dictionary:
        bid_amount = bidding_dictionary[i]  
        if bid_amount > highest_bid:
            highest_bid=bid_amount
            winner = i  
    print("the winner is {winner} and the bid is {highest_bid}")


should_continue = input("Are there is any bids continue? Type Yes, or No\n")

continue_bitting=True
while continue_bitting:
    name=input("what is your name\n")
    price = int(input("what is your bit\n $"))
    bids[name]=price 
    should_continue = input("Are there is any bids continue? Type Yes, or No\n").lower()
    if should_continue =="no":
        continue_bitting=False
        find_highest_bidder(bids)
        



