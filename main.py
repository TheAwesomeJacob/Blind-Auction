import os
import function_bidder

print("Welcome to the blind auction!")

more_bidders = True
bids = {}

while more_bidders:
  name = input("Please enter your name: ")
  bid = int(input("Enter your bid: "))
  if_someone_more = input("There another bidders? Type 'yes' or 'no': ")

  bids[name] = bid

  os.system('clear')

  if if_someone_more == 'no':
    more_bidders = False
    function_bidder.find_highest_bidder(bids)
  elif if_someone_more == 'yes':
    more_bidders = True
  else:
    print("Wrong value!")
