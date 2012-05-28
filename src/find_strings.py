'''
Created on May 12, 2012

@author: MUNEER
'''
def get_substrings(mystring):
    string_length = len(mystring)
    substrings = set([])
    for word_length in xrange(1,string_length+1):
        for substring_counts in xrange(string_length-word_length+1):
            substrings.add(mystring[substring_counts:
                                       substring_counts+word_length])
    return substrings

def main():
    num_input_strings = int(raw_input())
    input_strings,queries = [], []
    for i in xrange(num_input_strings):
        x = raw_input()
        input_strings.append(x)
    num_of_queries = int(raw_input())
    for i in xrange(num_of_queries):
        x = int(raw_input())
        queries.append(x)
    total_sub_strings = set([])
    for each_string in input_strings:
        total_sub_strings.update(get_substrings(each_string))
    print 'subsets: ', sorted(total_sub_strings)
    for each_query in queries:
        try:
            print sorted(total_sub_strings)[each_query-1]
        except:
            print 'INVALID'

if __name__ == '__main__':
    main()   
        
        
    
        
        
        
        
