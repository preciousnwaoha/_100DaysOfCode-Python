from art import logo

# from replit import clear # will only work in replit
#HINT: You can call clear() to clear the output in the console.

print(logo)
print("Weclome to the auction game.")

bid_data = {}

def who_bid_max():
  max = 0
  max_bidder = ""
  for key in bid_data:
    if bid_data[key] > max:
      max_bidder = key
  return max_bidder


def biding():
  name = input("What is your name: ")
  bid = int(input("What's your bid: $"))
  bid_data[name] = bid

def start_auction():
  more_bidders = True
  while more_bidders:
    biding()
    anyone = input("Any more bidders, 'yes' or 'no'").lower()
    if anyone == "no":
      more_bidders = False
    if anyone == "yes":
      # clear() # only works in replit
  max_bidder = who_bid_max()
  print(f"{max_bidder} won the auction, sold for ${bid_data[max_bidder]}")
    
start_auction()