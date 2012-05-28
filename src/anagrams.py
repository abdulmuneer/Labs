'''
Created on May 9, 2012

@author: MUNEER
'''
from pprint import pprint
def print_anagrams(list_of_strings):
    '''
    prints the anagrams present in the input list.
    Removes the first word and compares with all other words.
    Remove the found anagrams too from the list.
    Iterate until the list is reduced to an empty list
    '''
    anagrams, key = {},1
    while(list_of_strings):
        initial_word = list_of_strings.pop(0)
        anagrams_list = [words for words in list_of_strings 
                    if sorted(words)==sorted(initial_word)]
        if anagrams_list:
            anagrams[key] = [initial_word] + anagrams_list
            key += 1
        for words in anagrams_list:
            #less things to check for in the next iteration
            list_of_strings.remove(words)
        
    for lists in anagrams.values():
        for words in lists:
            print words,
        print '\n'

if __name__ == '__main__':
    print_anagrams(['abroad', 'aces', 'about', 'aboard', 'case','abdoar', 'esac','eee'])