hrsin = input("Enter Hours:")
h = float(hrsin)
#changed  hours to mumber with float 
#begin function called compute pay
# h is hour , r is rate  
def computepay (h,r):

    if h <= 40 :
       p = r * h
    else :
       p = r * 40 + (1.5 * r * (h - 40))
    return p
 #   
p = computepay(h ,10.5)
print("Pay",p)


#print computepay(hrs, 10.5)