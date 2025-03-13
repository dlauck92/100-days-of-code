bids = {}
continue_bidding = True

def find_highest_bidder(bidding_dict):
    highest_bid = 0
    for bidder in bidding_dict:
        bid_amount = bidding_dict[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder

    print(f"The winner is {winner} with a bid of ${highest_bid}.")

while continue_bidding:
    # Validate name input
    name = input("What is your name? \n").strip()
    while not name:
        print("Name cannot be empty. Please enter a valid name.")
        name = input("What is your name? \n").strip()

    # Validate bid input
    while True:
        try:
            bid = int(input("How much will you bid? \n"))
            if bid <= 0:
                print("Bid cannot be negative or zero. Please enter a positive amount.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a numeric value for your bid.")

    bids[name] = bid
    should_continue = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
    
    if should_continue == "no":
        continue_bidding = False
        find_highest_bidder(bids)
    elif should_continue == "yes":
        continue_bidding = True
        print("\n" * 20)
    else:
        print("Invalid input. Please type 'yes' or 'no'.")