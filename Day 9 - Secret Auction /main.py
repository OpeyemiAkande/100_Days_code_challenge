# This is a blind auction function

def bid_func():

    print('Welcome to the secret Auction Program')
    
    bidders = {}
    response = 'y'
    while response == 'y':

        name = input('Please enter your name: \n')
        bid = int(input('Please enter your bid price: \n'))

        bidders[name] = bid
        response = input('Are there any more bidders in the room? Y or n\n').lower()

    # else: 
    #     bidders_max = 0
    #     for key in bidders:
    #         if bidders[key] > bidders_max:
    #             bidders_max = bidders[key]
        
    #     for key in bidders:
    #         if bidders[key] == bidders_max:
    #             print(f'The highest bidder is {key} with ${bidders[key]}')
    
    else: 
      bidders_max = 0
      for bidder in bidders:
        bid_amount = bidders[bidder]
        if bid_amount > bidders_max:
          bidders_max = bidder_amount
          winner = bidder
      print(f'Winner is {winner} with ${bidders_max})
                

bid_func()


