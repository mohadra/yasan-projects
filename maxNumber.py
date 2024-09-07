a = float (input("Enter a number for a : "))
b = float (input("Enter a number for b : "))
c = float (input("Enter a number for c : "))
d = float (input("Enter a number for d : "))
if a < b :
    minNumber1= a
else :
    minNumber1 = b
if c < d :
    minNumber2 = c
else :
    minNumber2 = d
if   minNumber1 >  minNumber2 :
    print ("Min = ", minNumber2)
else :
    print ("Min = ", minNumber1)
