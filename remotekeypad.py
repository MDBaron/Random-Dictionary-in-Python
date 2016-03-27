'''
Created on Feb 21, 2013

@author: Fig Newton
'''
'''
Created on Feb 16, 2013

@author: Your Name
'''
class remotekeypad:
    """constructor"""
    def __init__(self,width,x,y):
        self.h = x
        self.v = y
        self.w = width
        
    def get_row(self, c):
       
        return (ord(c)-ord('a')) / self.w

    def get_col(self, c):
       
        return (ord(c)-ord('a')) % self.w
  
    def get_moves(self,s):
        
        sequence = [s.split(',')]
        cell = ''.join(sequence[0])
        p = 0
        
        while (p < len(cell)):
            
           
            self.get_move(cell[p])
            p += 1
            
    def get_move(self, c):
        LeftRight = self.get_col(c)
        UpDown = self.get_row(c)
        #define checksum for cell
        def check():
            if((LeftRight == self.h) and (UpDown == self.v)):
                print ('enter')
        #initial check to see if the iteration begins on the desired cell                    
        check()
        
        while(self.h > LeftRight):
            print ('Left ',)
            self.h -= 1
            check()
        while(self.h < LeftRight):
            print ('Right ',)
            self.h += 1
            check()
        while(self.v > UpDown):
            print ('Up ',)
            self.v -= 1
            check()
        while(self.v < UpDown):
            print ('Down ',)
            self.v += 1
            check()
            
       
                            
    