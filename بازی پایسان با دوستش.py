from sys import *
from random import *

for i in range(5):
    
    pn1 = randint(1,6)
    pn2 = randint(1,6)
    
    pfn1 = randint(1,6)
    pfn2 = randint(1,6)
    
    print("pysan :",pn1,pn2,"  pysan's friend :",pfn1,pfn2)


    if pn1 == pn2 and pfn1 != pfn2 :
        print("pysan is winner")
        exit()
    
    elif pfn1 == pfn2 and pn1 != pn2 :
        print("pysan's friend is winner")
        exit()
    elif pn1 == pn2 and pfn1 == pfn2 :
        print("You both win")
        exit()
print("Restart the program")

