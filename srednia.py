#!/usr/local/bin/python3.7

# -*- coding: utf-8 -*-

import sys


kop = sys.argv


d = len(kop) 

    
if (d == 1):
    s = "Dolnośląskie"
else:
    s = kop[1]
    
if (d > 2):
    
    bruce = kop[2]
else:
    bruce = 2010

    

bruce = int(bruce)




class wiesia:
    """Main class"""
    def __init__(self):
        print("zadanie srednia")
    
    def read(self):
        print("otwieranie i zamykanie pliku")
    def main(self,k,w,list,l,s,bruce):
        self.k = 0
        self.w = 0
        self.list = {}
        self.l = 0
        self.s = s
        self.bruce = bruce
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
         
        yy1 = "przystąpiło"
        yy2 = "zdało"
        
        
      
        
        
        for i in range(37,613):
            
            
            x2 = k[i]
            
            d = int(x2[4])
            q = int(x2[3])
            bruce2 = int(bruce)
                 
            if ((s == x2[0]) and  ( q == bruce2) and ( yy1 == x2[1] ) ):
                x110 += 1
                x1000 += d
       
            if ((s == x2[0]) and  ( q == bruce2) and ( yy2 == x2[1] ) ):
                y110 += 1
                y1000 += d
       
            
        x10 = x1000 // x110            
        y10 = y1000 // y110
        w = (y10 / x10 ) * 100
      
        
        
    
        
        print("procentowa zdawalność dla :",s)
        print("w roku ", bruce2)
        print("wynosi" ,w,"procent")
        
grzegorz = wiesia()



grzegorz.main(0,0,{},0,s,bruce)
    
