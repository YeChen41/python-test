# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#def move(n, a, b, c):
#    if n==1:
#        print(a,'-->',c)
#    else:
#        move(n-1,a,c,b)
#        print(a,'-->',c)
#        move(n-1,b,a,c)
#        
#move(3,'a','b','c')

#L = ['Hello', 'World', 18, 'Apple', None]
#print ([s.lower() for s in L if isinstance(s,str)])

#def fib(max):
#    n, a, b = 0, 0, 1
#    while n < max:
#        yield b
#        a, b = b, a + b
#        n = n + 1
#    return 'done'
#    
#f = fib(6)
#for n in fib(6):
#    print(n)

def triangles():
    l=[1]

    while True:
        yield l
        ll=l.copy()
        ll.insert(0,0)
        ll.append(0)
        n=len(ll)
        l.append(1)
        
        for i in range(n-2):     
            
            l[i]=ll[i]+ll[i+1]
#            l.append(ll[i]+ll[i+1])
n = 0
for t in triangles():
    print(t)
    n = n + 1
    if n == 10:
        break            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
