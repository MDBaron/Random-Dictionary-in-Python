'''
Created on Feb 21, 2013

@author: Fig Newton
'''
'''
Created on Feb 17, 2013

@author: Your name
'''
import sys

def print_words(filename):
    """ Print all words and their counts in sorted order """
    return

def print_top(filename, n):
    """ Print words that have top n counts in sorted order """
    return

###

# This basic command line argument parsing code is provided and
# calls the print_words() and print_top() functions which you must define.
def main():
    if len(sys.argv) < 3:
        print 'usage: ./wordcount.py {--count | --topcount} file num-of-top-words'
        sys.exit(1)

        option = sys.argv[1]
        filename = sys.argv[2]
    if option == '--count':
        print_words(filename)
    elif option == '--topcount':
        print_top(filename, sys.argv[3])
    else:
        print 'unknown option: ' + option
        sys.exit(1)

if __name__ == '__main__':
    main()