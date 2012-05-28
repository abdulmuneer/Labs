'''
Created on May 9, 2012

@author: MUNEER
'''


def get_final_amount(initial_amount, bet_results):
    if initial_amount < 1:
        print 'Initial amount is not a sufficient for the bet' 
        return None
    
    inhand_amount, next_bet = initial_amount, 1
    multiplying_factor = {'W':1,'L':-1}
    
    for results in bet_results:
        if results not in ('W','L'):
            print 'Invalid results entered'
            return None
        if next_bet > inhand_amount:
            print 'no more money to bet.Returning the in_hand money..'
            return inhand_amount
        inhand_amount += next_bet*multiplying_factor[results]
        next_bet = 1 if results=='W' else 2*next_bet
        
    return inhand_amount

if __name__ == '__main__':
    print get_final_amount(15, 'LLLWLLLLW')
    print get_final_amount(12, 'WWWWWWWW')
    x = raw_input()
    
    










