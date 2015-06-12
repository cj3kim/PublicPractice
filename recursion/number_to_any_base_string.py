
def convertBase10IntToAnyBase(n, base):
    conversion_string = "0123456789ABCDEF"
    if n < base:
        return conversion_string[n]
    else:
        return convertBase10IntToAnyBase(n/base, base) + conversion_string[n%base]

a = convertBase10IntToAnyBase(10, 10)
b = convertBase10IntToAnyBase(10, 2)
c = convertBase10IntToAnyBase(10, 16)

print 'a: {0}'.format(a)
print 'b: {0}'.format(b)
print 'c: {0}'.format(c)
