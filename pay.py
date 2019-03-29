hrsin = input("Enter Hours:")
hrs = float(hrsin)
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
p = computepay(hrs ,10.5)
print("Pay",p)

#hrs_st = raw_input("Enter Hours:")
#hrs = float(hrs_st)
#print computepay(hrs, 10.5)