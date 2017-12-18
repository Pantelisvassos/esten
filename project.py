def fibo(x):
	if x==1:
		return 1
	elif x==2:
		return 1
	else:
		return fibo(x-1)+fibo(x-2)
def fibo2(x):
	if x==1:
		return 1
	elif x==2:
		return 1
	else:
		for i in range(x+1):
			a=x-1
			b=x-2
			f=a+b
			return f
					
	






x = input('give a number\n')
import time
start = time.time()
print fibo2(x)
end = time.time()
print 'time', end-start 

