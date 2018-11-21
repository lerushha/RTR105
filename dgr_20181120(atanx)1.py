Python 3.6.7 (default, Oct 22 2018, 11:32:17) 
[GCC 8.2.0] on linux
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
============== RESTART: /home/aaa/RTR105/dgr_20181120(atanx).py ==============
Lietotāj, lūdzu, ievadi argumentu (x): 13
standarta atan(13.00) =   1.49
Izdruka no liet.f. a0 =   1.00 S0 =   1.00
Izdruka no liet.f. a499 =    inf S499 =    inf
Izdruka no liet.f. a500 =    inf S500 =    inf
mans atan(13.00) =    inf
                        500                                    
                      _______                                  
                x     \                                   2 k  
              ______   \           (2*k)!             ( x  )   
atan(13.00)=   _____    \ _____________________* ___________    
              /   2     /         2  k                      2 k
            \/ 1+x     /      (k)! *4 *(2*k+1)        (1+(x))  
                      /______                                  
                         k=0                                   
                              2       2  
                        (2*k-1)      x   
rekurences reizinatajs:___________*______
                        2*(2*k+1)      2 
                                    1+x  
>>> 
