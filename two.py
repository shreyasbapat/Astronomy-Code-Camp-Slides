def check(n):
	print (str(n)+ (" Even " if n%2==0 else " Odd ")+ str(n*n) )

for x in range(1,101):
	check(x)
