'''
Program to convert between hindu-roman numerals
Created on May 27, 2012

@author: MUNEER
'''

import re

#global variables
ROMAN_VALUES = {
                 'I':1,
                 'V':5,
                 'X':10,
                 'L':50,
                 'C':100,
                 'D':500,
                 'M':1000
                 }
HINDU_VALUES = {
                  1:'I',
                  5:'V',
                  10:'X',
                  50:'L',
                  100:'C',
                  500:'D',
                  1000:'M'
                  }

def roman_to_hindu(number):
    '''
    Converts roman numbers to hindu numbers
    '''
    hindu_number = 0
    for i in range(len(number)):
        #identify if the literal is in a negative position 
        # a negative position is a number that is less than the next number.
        # e.g: in 'XL' the 'X' is in -ve position.
        try:
            is_negative = ROMAN_VALUES[number[i]] < ROMAN_VALUES[number[i+1]]
        except:#IndexError for the last number
            is_negative = False
        
        #subtract the numbers in negative position. Add others.
        if is_negative:
            hindu_number -= ROMAN_VALUES[number[i]]
        else:
            hindu_number += ROMAN_VALUES[number[i]]
    return hindu_number
    
        
        
def hindu_to_roman(number):
    '''
    converts hindu numbers to roman numbers
    '''
    roman = ''
    while number:
        if number >=1000:
            thousands = number/1000
            roman = roman + 'M'*thousands
            number = number%1000
        elif number >= 900:
            roman = roman + 'CM'
            number -= 900
        elif number >= 500:
            roman = roman+'D'
            number -= 500
        elif number >= 400:
            roman = roman + 'CD'
            number -= 400
        elif number >= 100:
            hundreds = number/100
            number = number%100
            roman = roman + 'C'*hundreds
        elif number >= 90:
            roman = roman + 'XC'
            number -= 90
        elif number >=50:
            roman = roman + 'L'
            number -= 50
        elif number >=40:
            roman = roman + 'XL'
            number -= 40
        elif number >=10:
            tens = number/10
            number = number%10
            roman = roman + 'X'*tens
        elif number == 9:
            roman = roman + 'IX'
            number = 0
        elif number >=5:
            roman = roman + 'V' + 'I'*(number-5)
            number = 0
        elif number == 4:
            roman = roman + 'IV'
            number = 0
        elif number > 0:
            roman = roman + 'I'*number
            number = 0
        else:
            roman = ''
            number = 0
    return roman

def isvalid(roman):
    '''
    validates a roman number
    '''
    pattern = """
    ^                   # beginning of string
    M{0,4}              # thousands - 0 to 4 M's
    (CM|CD|D?C{0,3})    # hundreds - 900 (CM), 400 (CD), 0-300 (0 to 3 C's),
                        #            or 500-800 (D, followed by 0 to 3 C's)
    (XC|XL|L?X{0,3})    # tens - 90 (XC), 40 (XL), 0-30 (0 to 3 X's),
                        #        or 50-80 (L, followed by 0 to 3 X's)
    (IX|IV|V?I{0,3})    # ones - 9 (IX), 4 (IV), 0-3 (0 to 3 I's),
                        #        or 5-8 (V, followed by 0 to 3 I's)
    $                   # end of string
    """
    match = re.search(pattern, roman, re.VERBOSE)
    return True if match else False
    
    
def main():
    '''
    Takes input, identifies if it is hindu or roman and converts to the other.
    '''
    number_string = raw_input(
            "Enter the number to convert. (type is auto detected)").upper()
    if set(number_string).issubset(
                            set([str(i) for i in xrange(10)])
                            ):
        print hindu_to_roman(int(number_string))
    elif set(number_string).issubset(
                                     set('IVXLCDM')
                                     ):
        if not isvalid(number_string):
            print "Invalid roman numerals"
            return
        print roman_to_hindu(number_string)
    else:
        print "Invalid input.."
        

if __name__ == '__main__':
    #print roman_to_hindu('MMMDCXVIII')
    #print hindu_to_roman(564)
    main()
