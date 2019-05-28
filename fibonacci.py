'''
	斐波那契数列
	1 1 2 3 5 8 13 21 34 55 89 ...
'''
a = 0
b = 1
for x in range(0,20):
	a , b = b ,a + b
	print a 
