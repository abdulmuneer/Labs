'''
Created on May 25, 2012
@author: MUNEER
prints the input sentence in reversed words.
'''
def reverse(sentence):
    '''
    returns a sentence with words arranged in reverse order
    '''
    return ' '.join(reversed(sentence.split()))

if __name__ == '__main__':
    sentence = 'a'
    while sentence:
        sentence = raw_input("Enter the sentence:\n")
        print reverse(sentence),'\n\n'