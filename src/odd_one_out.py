'''
detects the two digit odd numbers occurring in a string.
Created on May 25, 2012

@author: MUNEER
'''
import re

def search_odd_twodigits(string=None):
    '''
    returns a list of two digit odd numbers occurring in a string.
    '''
    rg = re.compile(r'(?<!\d)\d{2}(?!\d)')#pattern for 2-digit numbers
    matches = re.findall(rg, string)
    odd_twodigit_numbers = [int(match) for match in matches
                       if int(match)%2] if matches else None
    return odd_twodigit_numbers

def main():
    input_string = raw_input("Enter the string..")
    numbers = search_odd_twodigits(input_string)
    print  numbers if numbers else "No Matches.."

if __name__ == '__main__':
    x = search_odd_twodigits(
        r"A#xlj$adsfj182xcvd91$233$lkjiopl%911asdxcit*13Xasdfc")
    