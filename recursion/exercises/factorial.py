
def computeFactorial(n):
    return n if n == 1 else n * computeFactorial(n-1)


a = computeFactorial(10)
b = computeFactorial(3)
c = computeFactorial(4)

print 'a: {0}'.format(a)
print 'b: {0}'.format(b)
print 'c: {0}'.format(c)


