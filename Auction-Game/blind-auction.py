logo = r'''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''

print(logo)

list_of_bidders = {}
auction_active = True

while auction_active:
    name = input("What is your name?: ")
    amount = int(input("What amount are you willing to bid?: $"))
    list_of_bidders[name] = amount
    answer = input("Are there any more bidders? Type 'yes' if any, else 'no' \n").lower()
    print(answer)
    if answer == "yes":
        print("\n" * 100)
    else:
        print("\n" * 100)
        auction_active = False
    
highest_bid_value = 0
bid_winner = ""

for person in list_of_bidders:
    if list_of_bidders[person] > highest_bid_value:
        highest_bid_value = list_of_bidders[person]
        bid_winner = person

print(f"The winner is {bid_winner} with a bid of ${highest_bid_value}")
