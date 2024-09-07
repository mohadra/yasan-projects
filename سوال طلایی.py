n = int(input("tedad danesh amozan ra vared konid :"))
hazineh = 25 * n
if n % 10 == 0 :
    van = n / 10
else:
    van = int ((n / 10 ) + 1)
hazineh_kol = van * 150 + hazineh
print (hazineh_kol)
