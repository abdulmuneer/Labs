'''
Created on May 6, 2012

@author: MUNEER
'''
def main():
    number_of_tests = raw_input()
    string_inputs = {}
    result_sets = {}
    count = 0
    try:
        number_of_tests = int(number_of_tests)
    except:
        print "Invalid entry.. Exiting..."
        return
    
    for test_number in range(1,number_of_tests+1):
        mystring = raw_input()
        substring = raw_input()
        if test_number!=number_of_tests:
            blank_line = raw_input()
        string_inputs[test_number] = mystring,substring
    
    for keys, values in string_inputs.items():
        result_sets[keys] = substring_matches(values)
        
    for keys, values in result_sets.items():
        #print "values", values
        print ' '.join((str(x) for x in values))
        
def substring_matches((mystring,substring)):
    len_sub = len(substring)
    len_main = len(mystring)
    matches = 0
    matching_indices = []
    if len_main<len_sub:
        return None
    
    for i in range(len_main-len_sub):
        mismatches = sum([is_different(item) 
                          for item in zip(mystring[i:i+len_sub],substring)])
        if mismatches <=1:
            matches += 1
            matching_indices.append(i)
        
    #print "matching indices",matching_indices
    return matching_indices
def is_different((item1,item2)):
    return 0 if item1==item2 else 1
'''
[1,2,3,4,5]
[1,2,4]

'''

if __name__ == '__main__':
    main()