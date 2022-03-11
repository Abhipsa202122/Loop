#PRIME NO. IS NOT DIVISIBLE BY ANY OTHER NO.EXCEPT ITSELF AND 1.
a=int(input("enter no."))
i=1
c=0
while i<=a:
    if a%i==0:
       c+=1
    i+=1
if c==2:
   print(a,"is prime no")
else:
   print(a,"is not prime no")    
           