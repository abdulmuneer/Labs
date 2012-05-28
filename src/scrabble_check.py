'''
Created on May 12, 2012

@author: MUNEER
'''
import time
def check(myword):
    try:
        with open('sowpods.txt') as scrabblefile:
            for lines in scrabblefile.readlines():
                if myword.lower()==lines.strip().lower():
                    print "\nACCEPTED Word..\n"
                    return True
            else:
                print "\nWord '%s' NOT accepted\n"%myword
                return True
    except:
        print"Dictionary not found in the path."
        print "Please copy sowpods.txt file to the same directory as program"
        print "and re run the program again.."
        x = raw_input("Hit enter key to exit")
        return False

def main():
    running_status = True
    while running_status:
        myword = raw_input("Enter the word to be checked.. \
        \n(Enter '~' to exit the program)\nword:")
        running_status = False if myword.startswith('~') else check(myword)
        if not running_status:
            print "Exiting.."
            time.sleep(1)
            print "Good Bye.."
            time.sleep(0.5)
            
            
if __name__ == '__main__':
    main()            
    