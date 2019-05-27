#!/usr/local/bin/python3.7



# -*- coding: utf-8 -*-






import sys


kop = sys.argv


d = len(kop) 

 
    

if (d == 1):
    s = "Dolnośląskie"
    g = "Kujawsko-pomorskie"
    jo ="bo"
    print("Nie podałeś województwa domyślne jest Dolnośląskie i Kujawsko-pomorskie") 
    print()
else:
    s = kop[1]
    g = kop[2]



class wiesia:
    """Main class"""
    def __init__(self):
        print("porównywujemy województwa")
    
    def read(self):
        print("otwieranie i zamykanie pliku")
    def main(self,k,w,list,l,s,g):
        self.k = 0
        self.w = 0
        self.list = {}
        self.l = 0
        self.s = s
        self.g = g
        
        
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
            
        
            v[i] = w
            
            k[i] = d
      
            
            
        vv = []   
        d = 0
        x110 = 0
        x1000 = 0
        y110 = 0
        y1000 = 0
        
        w110 = 0
        w1000 = 0
        z110 = 0
        z1000 = 0
        
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
        
        ##
        
        w210 = 0
        w2000 = 0
        z210 = 0
        z2000 = 0
        
        w310 = 0
        w3000 = 0
        z310 = 0
        z3000 = 0  
        
        w410 = 0
        w4000 = 0
        z410 = 0
        z4000 = 0  
        
        w510 = 0
        w5000 = 0
        z510 = 0
        z5000 = 0 
                
        w610 = 0
        w6000 = 0
        z610 = 0
        z6000 = 0
       
        w710 = 0
        w7000 = 0
        z710 = 0
        z7000 = 0 
        
        w810 = 0
        w8000 = 0
        z810 = 0
        z8000 = 0 
        
        w910 = 0
        w9000 = 0
        z910 = 0
        z9000 = 0 
        
        
       
         
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
            q2 = x2[2]
            
            if ((s == x2[0]) and  ( q == aaa0) and ( yy1 == x2[1] ) ):
                x110 += 1
                x1000 += d
       
            if ((s == x2[0]) and  ( q == aaa0) and ( yy2 == x2[1] ) ):
                y110 += 1
                y1000 += d
            
                 
         
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
                
            if ((s == x2[0]) and  ( q == aaa5) and ( yy2 == x2[1] ) ):
                y710 += 1
                y7000 += d  
            
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
                
            ######
            if ((g == x2[0]) and  ( q == aaa0) and ( yy1 == x2[1] ) ):
                w110 += 1
                w1000 += d
                
       
            if ((g == x2[0]) and  ( q == aaa0) and ( yy2 == x2[1] ) ):
                z110 += 1
                z1000 += d
            #
            if ((g == x2[0]) and  ( q == aaa1) and ( yy1 == x2[1] ) ):
                w210 += 1
                w2000 += d
       
            if ((g == x2[0]) and  ( q == aaa1) and ( yy2 == x2[1] ) ):
                z210 += 1
                z2000 += d
            #    
            if ((g == x2[0]) and  ( q == aaa2) and ( yy1 == x2[1] ) ):
                w310 += 1
                w3000 += d
       
            if ((g == x2[0]) and  ( q == aaa2) and ( yy2 == x2[1] ) ):
                z310 += 1
                z3000 += d
                
            #
            if ((g == x2[0]) and  ( q == aaa3) and ( yy1 == x2[1] ) ):
                w410 += 1
                w4000 += d
       
            if ((g == x2[0]) and  ( q == aaa3) and ( yy2 == x2[1] ) ):
                z410 += 1
                z4000 += d  
                
            #
            if ((g == x2[0]) and  ( q == aaa4) and ( yy1 == x2[1] ) ):
                w510 += 1
                w5000 += d
       
            if ((g == x2[0]) and  ( q == aaa4) and ( yy2 == x2[1] ) ):
                z510 += 1
                z5000 += d  
            #
            if ((g == x2[0]) and  ( q == aaa5) and ( yy1 == x2[1] ) ):
                w610 += 1
                w6000 += d
       
            if ((g == x2[0]) and  ( q == aaa5) and ( yy2 == x2[1] ) ):
                z610 += 1
                z6000 += d  
            
            #
            
            if ((g == x2[0]) and  ( q == aaa6) and ( yy1 == x2[1] ) ):
                w710 += 1
                w7000 += d
       
            if ((g == x2[0]) and  ( q == aaa6) and ( yy2 == x2[1] ) ):
                z710 += 1
                z7000 += d  
            
            # 
            if ((g == x2[0]) and  ( q == aaa7) and ( yy1 == x2[1] ) ):
                w810 += 1
                w8000 += d
       
            if ((g == x2[0]) and  ( q == aaa7) and ( yy2 == x2[1] ) ):
                z810 += 1
                z8000 += d  
            
            #
            if ((g == x2[0]) and  ( q == aaa8) and ( yy1 == x2[1] ) ):
                w910 += 1
                w9000 += d
       
            if ((g == x2[0]) and  ( q == aaa8) and ( yy2 == x2[1] ) ):
                z910 += 1
                z9000 += d  
        
        
              
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
        
        #           
        scala10  = w1000 // w110            
        scala100 = z1000 // z110
        scala1 = (scala100 / scala10 ) * 100
        
       
        
        scala20 = w2000 // w210            
        scala200 = z2000 // z210
        scala2 = (scala200 / scala20 ) * 100
        
 
        
        scala30 = w3000 // w310            
        scala300 = z3000 // z310
        scala3 = (scala300 / scala30 ) * 100
        
        
        
        scala40 = w4000 // w410            
        scala400 = z4000 // z410
        scala4 = (scala400 / scala40 ) * 100
        
        
        
        scala50 = w5000 // w510            
        scala500 = z5000 // z510
        scala5 = (scala500 / scala50 ) * 100
        
        
        
        scala60 = w6000 // w610            
        scala600 = z6000 // z610
        scala6 = ( scala600 / scala60 ) * 100
        
        
        
        scala70 = w7000 // w710            
        scala700 = z7000 // z710
        scala7 = (scala700 / scala70 ) * 100
        
        
        
        scala80 = x8000 // x810            
        scala800 = y8000 // y810
        scala8 = (scala800 / scala80 ) * 100
        
        
        
        
        
        
        
        scala90 = x9000 // x910            
        scala900 = y9000 // y910
        scala9 = (scala900 / scala90 ) * 100
        
        
        
        if (w1 < scala1):
            print("Województwo: ",g,"ma większa zdawalność worku",aaa0)
        else:
            print("Województwo :",s,"ma większa zdawalność worku",aaa0)
        
        print()
        
               
        if (w2 < scala2):
            print("Województwo: ",g,"ma większa zdawalność w roku",aaa1)
        else:
            print("Województwo :",s,"ma większa zdawalność w roku",aaa1)
        
        print()
        
        if (w3 < scala3):
            print("Województwo: ",g,"ma większa zdawalność w roku",aaa2)
        else:
            print("Województwo :",s,"ma większa zdawalność w roku",aaa2)
            
        print()
        
        if (w4 < scala4):
            print("Województwo: ",g,"ma większa zdawalność w roku",aaa3)
        else:
            print("Województwo :",s,"ma większa zdawalność w roku",aaa3)
            
        print()
        
        if (w5 < scala5):
            print("Województwo: ",g,"ma większa zdawalność w roku",aaa4)
        else:
            print("Województwo :",s,"ma większa zdawalność w roku",aaa4)
        print ()
        if (w6 < scala6):
            print("Województwo: ",g,"ma większa zdawalność w roku",aaa5)
        else:
            print("Województwo :",s,"ma większa zdawalność w roku",aaa5)
            
        print()
        
        if (w7 < scala7):
            print("Województwo: ",g,"ma większa zdawalność w roku",aaa6)
        else:
            print("Województwo :",s,"ma większa zdawalność w roku",aaa6)
        
        print()
        
        if (w8 < scala8):
            print("Województwo: ",g,"ma większa zdawalność w roku",aaa7)
        else:
            print("Województwo :",s,"ma większa zdawalność w roku",aaa7)
        
        print()
        
        
        if (w9 < scala9):
            print("Województwo: ",g,"ma większa zdawalność w roku",aaa8)
        else:
            print("Województwo :",s,"ma większa zdawalność w roku",aaa8)   
        
            
grzegorz = wiesia()



grzegorz.main(0,0,{},0,s,g)