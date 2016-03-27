'''
Created on Feb 21, 2013

@author: Fig Newton
'''
'''
Created on Feb 16, 2013

@author: Jane
'''
import ast
import mystring
import mylist
import remotekeypad
import Configurator

def myPrint():
    star = "*"
    space = ' ' 
    count = 4
    for p in range(0,5):
        print ((space * count)+ star +(space * count)) 
        
        star += "**"
        count -= 1
         

# a predefined main function
# that takes care of input test cases from configuration file
def main():
    print ('myPrint')
    myPrint()
    print
  
    Configurator.write_conf()
  
    print ('String: both_ends')
    cases = ast.literal_eval(Configurator.get_conf('String', 'both_ends'))
    for case in cases:
        print (case + ' -> ' + mystring.both_ends(case))
        print

    print ('String: fix_start')
    cases = ast.literal_eval(Configurator.get_conf('String', 'fix_start'))
    for case in cases:
        print (case + ' -> ' + mystring.fix_start(case))
        print
  
        print ('String: mix_up')
        cases = ast.literal_eval(Configurator.get_conf('String', 'mix_up'))
    for case in cases:
        print (case),
        print (' -> ' + mystring.mix_up(case[0], case[1]))
        print
  
    print ('String: not_bad')
    cases = ast.literal_eval(Configurator.get_conf('String', 'not_bad'))
    for case in cases:
        print (case + ' -> ' + mystring.not_bad(case))
    print
  
    print ('String: font_back')
    cases = ast.literal_eval(Configurator.get_conf('String', 'front_back'))
    for case in cases:
        print (case),
        print (' -> ' + mystring.front_back(case[0], case[1]))
    print
  
    print ('List: match_ends')
    cases = ast.literal_eval(Configurator.get_conf('List', 'match_ends'))
    for case in cases:
        print (case),
        print (' -> '),
        print (mylist.match_ends(case))
    print
  
    print ('List: front_x')
    cases = ast.literal_eval(Configurator.get_conf('List', 'front_x'))
    for case in cases:
        print (case),
        print (' -> '),
        print (mylist.front_x(case))
    print
  
    print ('List: sort_last')
    cases = ast.literal_eval(Configurator.get_conf('List', 'sort_last'))
    for case in cases:
        print (case),
        print (' -> '),
        print (mylist.sort_last(case))
    print
  
    print ('List: remove_adjacent')
    cases = ast.literal_eval(Configurator.get_conf('List', 'remove_adjacent'))
    for case in cases:
        print (case),
        print (' -> '),
        print (mylist.remove_adjacent(case))
    print
  
    print ('List: linear_merge')
    cases = ast.literal_eval(Configurator.get_conf('List', 'linear_merge'))
    for case in cases:
        print (case),
        print (' -> '),
        print (mylist.linear_merge(case[0], case[1]))
    print
  
    print ('Remote:')
    width = ast.literal_eval(Configurator.get_conf('Remote', 'width'))
    x = ast.literal_eval(Configurator.get_conf('Remote', 'x'))
    y = ast.literal_eval(Configurator.get_conf('Remote', 'y'))
    remote = remotekeypad.remotekeypad(width, x, y)
    cases = ast.literal_eval(Configurator.get_conf('Remote', 'keys'))
    for case in cases:
        remote.get_moves(case)
        print

# Standard boilerplate to call the main() function.
if __name__ == '__main__':
    main()