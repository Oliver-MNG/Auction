import os

from art_day9 import logo
print(logo)

print("Welcome to the auction!")

auction = {}

def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ''
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner in {winner} with a bid of {highest_bid}$ ")

bidding_finished = False

while not bidding_finished:
    name = input("Enter your name: ")
    bid = int(input("Enter you bid: "))
    auction[name] = bid
    auc_member = input("Is there any other auction members left? 'yes' or 'no':\n")
    if auc_member == 'no':
        bidding_finished = True
        find_highest_bidder(auction)
    elif auc_member == 'yes':
        os.system('clear')

