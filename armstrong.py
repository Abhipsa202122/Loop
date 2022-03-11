#Armstrong  no.
num=int(input("enter no"))
i=0
sum=0
a=num
while i<=num:
	digit=(num%10)(num%10)(num%10)
	sum=sum+digit
	num=num//10
if a==sum:
	print('armstrong no')
else:
	print('not')
i+=1