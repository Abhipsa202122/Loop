#primary no:
a=int(input("enter no"))
i=1
f=0
while i<=a:
    if a%i==0:
       f+=1
    i+=1
if f==2:
   print(a,"is prime no.")
else:
   print(a,"is not prime no")             
