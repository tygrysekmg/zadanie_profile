#!/usr/local/bin/python3.7



# -*- coding: utf-8 -*-






import sys


kop = sys.argv


d = len(kop) 
 
    



if (d == 1):
    s = "Dolnośląskie"
else:
    s = kop[1]
    






class wiesia:
    """Main class"""
    def __init__(self):
        print("zadanie srednia2")
    
    def read(self):
        print("otwieranie i zamykanie pliku")
    def main(self,k,w,list,l,s):
        self.k = 0
        self.w = 0
        self.list = {}
        self.l = 0
        self.s = s
        
        text_file = open("2.txt","r")
        lines = text_file.readlines()
        
        l = 0
        k = {}
        v = {}
        x = []
        for line in lines:
        
            
        
            
                
                list[w] = line
                
                w += 1
                
                
                
                
                
                
         
        for i in range(37,613):
            #print(list[i])
            f = list[i]
            d = f.split(";")
            
        # w = d.split("\")
            v[i] = w
            
            k[i] = d
            
        vv = []   
        d = 0
        x110 = 0
        x1000 = 0
        y110 = 0
        y1000 = 0
        
        
        
        d = 0
        
        x210 = 0
        x2000 = 0
        y210 = 0
        y2000 = 0
        
        x310 = 0
        x3000 = 0
        y310 = 0
        y3000 = 0  
        
        x410 = 0
        x4000 = 0
        y410 = 0
        y4000 = 0  
        
        x510 = 0
        x5000 = 0
        y510 = 0
        y5000 = 0 
        
        x610 = 0
        x6000 = 0
        y610 = 0
        y6000 = 0 
        
        x710 = 0
        x7000 = 0
        y710 = 0
        y7000 = 0 
        
        x810 = 0
        x8000 = 0
        y810 = 0
        y8000 = 0 
        
        x910 = 0
        x9000 = 0
        y910 = 0
        y9000 = 0 
         
        yy1 = "przystąpiło"
        yy2 = "zdało"
        
            
        aaa0 = 2010
        aaa1 = 2011
        aaa2 = 2012
        aaa3 = 2013
        aaa4 = 2014
        aaa5 = 2015
        aaa6 = 2016
        aaa7 = 2017
        aaa8 = 2018
      
        
        
        for i in range(37,613):
            
            
            x2 = k[i]
            
            d = int(x2[4])
            q = int(x2[3])
            
                 
            if ((s == x2[0]) and  ( q == aaa0) and ( yy1 == x2[1] ) ):
                x110 += 1
                x1000 += d
       
            if ((s == x2[0]) and  ( q == aaa0) and ( yy2 == x2[1] ) ):
                y110 += 1
                y1000 += d
            #
            if ((s == x2[0]) and  ( q == aaa1) and ( yy1 == x2[1] ) ):
                x210 += 1
                x2000 += d
       
            if ((s == x2[0]) and  ( q == aaa1) and ( yy2 == x2[1] ) ):
                y210 += 1
                y2000 += d
            #    
            if ((s == x2[0]) and  ( q == aaa2) and ( yy1 == x2[1] ) ):
                x310 += 1
                x3000 += d
       
            if ((s == x2[0]) and  ( q == aaa2) and ( yy2 == x2[1] ) ):
                y310 += 1
                y3000 += d
                
            #
            if ((s == x2[0]) and  ( q == aaa3) and ( yy1 == x2[1] ) ):
                x410 += 1
                x4000 += d
       
            if ((s == x2[0]) and  ( q == aaa3) and ( yy2 == x2[1] ) ):
                y410 += 1
                y4000 += d  
                
            #
            if ((s == x2[0]) and  ( q == aaa4) and ( yy1 == x2[1] ) ):
                x510 += 1
                x5000 += d
       
            if ((s == x2[0]) and  ( q == aaa4) and ( yy2 == x2[1] ) ):
                y510 += 1
                y5000 += d  
            #
            if ((s == x2[0]) and  ( q == aaa5) and ( yy1 == x2[1] ) ):
                x610 += 1
                x6000 += d
       
            if ((s == x2[0]) and  ( q == aaa5) and ( yy2 == x2[1] ) ):
                y610 += 1
                y6000 += d  
            
            #
            
            if ((s == x2[0]) and  ( q == aaa6) and ( yy1 == x2[1] ) ):
                x710 += 1
                x7000 += d
       
            if ((s == x2[0]) and  ( q == aaa6) and ( yy2 == x2[1] ) ):
                y710 += 1
                y7000 += d  
            
            # 
            if ((s == x2[0]) and  ( q == aaa7) and ( yy1 == x2[1] ) ):
                x810 += 1
                x8000 += d
       
            if ((s == x2[0]) and  ( q == aaa7) and ( yy2 == x2[1] ) ):
                y810 += 1
                y8000 += d  
            
            #
            if ((s == x2[0]) and  ( q == aaa8) and ( yy1 == x2[1] ) ):
                x910 += 1
                x9000 += d
       
            if ((s == x2[0]) and  ( q == aaa8) and ( yy2 == x2[1] ) ):
                y910 += 1
                y9000 += d  
            
        x10 = x1000 // x110            
        y10 = y1000 // y110
        w1 = (y10 / x10 ) * 100
        
        x20 = x2000 // x210            
        y20 = y2000 // y210
        w2 = (y20 / x20 ) * 100
      
        
        x30 = x3000 // x310            
        y30 = y3000 // y310
        w3 = (y30 / x30 ) * 100
        
        x40 = x4000 // x410            
        y40 = y4000 // y410
        w4 = (y40 / x40 ) * 100
      
        x50 = x5000 // x510            
        y50 = y5000 // y510
        w5 = (y50 / x50 ) * 100
        
        x60 = x6000 // x610            
        y60 = y6000 // y610
        w6 = (y60 / x60 ) * 100
        
        x70 = x7000 // x710            
        y70 = y7000 // y710
        w7 = (y70 / x70 ) * 100
        
        x80 = x8000 // x810            
        y80 = y8000 // y810
        w8 = (y80 / x80 ) * 100
        
        x90 = x9000 // x910            
        y90 = y9000 // y910
        w9 = (y90 / x90 ) * 100
     
        print("procentowa zdawalność dla :",s)
        print("w roku", aaa0)
        print("wynosi" ,w1,"procent")
                     
        print("procentowa zdawalność dla :",s)
        print("w roku", aaa1)
        print("wynosi" ,w2,"procent")
        
        print("procentowa zdawalność dla :",s)
        print("w roku", aaa2)
        print("wynosi" ,w3,"procent")
        
        print("procentowa zdawalność dla :",s)
        print("w roku", aaa3)
        print("wynosi" ,w4,"procent")
        
        print("procentowa zdawalność dla :",s)
        print("w roku", aaa4)
        print("wynosi" ,w5,"procent")
        
        print("procentowa zdawalność dla :",s)
        print("w roku", aaa5)
        print("wynosi" ,w6,"procent")
        
        print("procentowa zdawalność dla :",s)
        print("w roku", aaa6)
        print("wynosi" ,w7,"procent")
        
        print("procentowa zdawalność dla :",s)
        print("w roku", aaa7)
        print("wynosi" ,w8,"procent")
        
        print("procentowa zdawalność dla :",s)
        print("w roku", aaa8)
        print("wynosi" ,w9,"procent")
            
grzegorz = wiesia()



grzegorz.main(0,0,{},0,s)