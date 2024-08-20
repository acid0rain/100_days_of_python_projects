# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary


# name will be key, bid will be value
# once all bids are set, convert to list, loop and apply bubble sort algo

more_bidders = True
auction_bids = {}

while more_bidders:

    bidder_name = input("What is your name? ")  # key
    bid = int(input("What if your maximum bid? "))  # value
    auction_bids[bidder_name] = bid

    keep_bidding = input("Are there any more bidders? Yes or No? ").lower()
    if keep_bidding == "no":
        more_bidders = False
        break
    elif "yes":
        print("\n" * 100) # clear screen

print(auction_bids)


def sort_by_highest_bidder(bidding_dictionary):

    bids_list = list(bidding_dictionary.items()) #unpack items and convert to list

    n = len(bids_list)

    for bid in range(n): # passes through all elements in the list
        for i in range(n - bid -1):  # loop to compare each element side by side
            if bids_list[i][1] < bids_list[i+1][1]:  # compare bid values not the tuples (keys)
                bids_list[i], bids_list[i+1] = bids_list[i+1], bids_list[i]   # swapping

    auction_bids = dict(bids_list)

    highest_key, highest_value = next(iter((auction_bids.items())))
    print(f" Highest bidder is: {highest_key}! With a bid of ${highest_value}")
    return auction_bids

sort_by_highest_bidder(auction_bids)