'''
    斐波那契数列-生成器实现
'''

def fib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
        yield a 

def main():
    for value in fib(20):
        print (value)

if __name__='__main__':
    main()
