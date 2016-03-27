'''
Created on Feb 21, 2013

@author: Fig Newton
'''
import random
import sys

def mimic_dict(filename):
    
    mimic_dict = {}
    f = open(filename,'r')
    text = f.read()
    f.close()
    words = text.split()
    before = ' '
    for w in words:
        if not before in mimic_dict:
            mimic_dict[before] = [w]
        else:
            mimic_dict[before].append(w)    
    
        before = w
    return mimic_dict


def print_mimic(mimic_dict, word, n):
    """Given mimic dict and start word, prints n random words."""
    i = 0
    while (i < n):
        word = random.choice(mimic_dict.get(word,' '))
        i += 1
    print word + ' ' 


# Provided main(), calls mimic_dict() and mimic()
def main():
    if len(sys.argv) != 3:
        print 'usage: ./mimic.py file-to-read num-of-random-words'
        sys.exit(1)

    dic = mimic_dict(sys.argv[1])
    print_mimic(dic, '', sys.argv[2])


if __name__ == '__main__':
    main()