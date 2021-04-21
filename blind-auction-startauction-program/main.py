from replit import clear
from art import logo


print(logo)
print("welcome to bro auction")
bid = {}

bidding_finsihed = False
#for loop in dictionary loops in keys not values 
def highest_bid(bid_record):
    highest_bid = 0
    for bidders in bid_record:
        bid_amount = bid_record[bidders]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidders
    print(f"the winner is {winner} wwith a bid of {highest_bid}")


while  not bidding_finsihed: #while this is false  
    name = input("what is your name: ")
    price = int(input("what is your bid: ?"))
    bid[name] = price #that is how you add entery to dicontary(key + value)
    another = input("are there another bidders yes or no: ")
    if another == "no":
        highest_bid(bid)
        break
    elif another == "yes":
        clear()    



