'''
Created on Feb 21, 2013

@author: Fig Newton
'''
'''
Created on Feb 16, 2013

@author: Your Name
'''
    
def both_ends(s):
    if (len(s) > 2):
        return (s[0:2]+s[-2:])
    else:
        return ('')    
  
def fix_start(s):
    return s.replace(s[0:1],'*')

def mix_up(a, b):
    one = a
    two = b
    
    temp = one
    last = one[0:1] + two[1:]
    first = two[0:1] + temp[1:] 
    return (first + ' ' + last)

def not_bad(s):
    negative = s.find('not')
    fodder = None
    if (negative != -1):
        if (s.find('bad') != -1):
            badPart = s.find('bad')
            if (negative < badPart):
                fodder = s[negative:]
    if(fodder is None):
        return s
    else:                
        return s.replace(fodder,'good')
    

def front_back(a, b):
   
    return (a[0:(len(a)//2)] + b[0:(len(b)//2)] + a[(len(a)//2):len(a)] + b[(len(b)//2):len(b)])
    