# An Auction Program
logo = """
                         ___________
                         \         /
                          )_______(
                          |_______|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )_______(
                         /_________\
                        /`'-------'`\
                        -------------
"""
print(logo)
print("Welcome to the Bidding Platform.")
def highest_bid():
    max_key = max(auction, key = auction.get)
    max_value = auction[max_key]
    print(f"The winner is {max_key} with the bid of ${max_value}.")


auction = {}
while True:
    name = input("Enter your name: ")
    bid_price = int(input("Enter Bid Price: $"))
    auction[name] = bid_price

    choice = input("Do we have more bidders? Y/N? ").lower()
    if choice == "y":
        end = False
    elif choice == "n":
        end = True
        highest_bid()
        break
    else:
        print("Invalid Option.")
        break
