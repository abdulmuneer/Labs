'''
Created on May 12, 2012

@author: MUNEER
'''

def similarity_index(mystring, start_index):
    count = 0
    try:
        while mystring[count]==mystring[start_index+count]:
            count += 1
        else:
            return count
    except:
        return count
    
def get_output(mystring):
    length = len(mystring)
    longest_matching_indices = (similarity_index(mystring, i) for 
                                i in xrange(length))
    return sum(longest_matching_indices)

def main():
    num_of_tests = int(raw_input())
    mystrings = [raw_input() for tests in xrange(num_of_tests)]
    for strings in mystrings:
        print get_output(strings)

if __name__ == '__main__':
    main()
    
    
    