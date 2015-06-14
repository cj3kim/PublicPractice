from collections import deque

def reverse_ary(ary):
    last_value = ary.pop()
    if len(ary) > 0: reverse_ary(ary)
    ary.appendleft(last_value)

ary = range(10)
d = deque(ary)

print 'd: {0}'.format(d)
mem_address_old = hex(id(d))
reverse_ary(d)
mem_address_new = hex(id(d))

print 'ary: {0}'.format(d)
print 'mem_address_old: {0}'.format(mem_address_old)
print 'mem_address_new: {0}'.format(mem_address_new)

def reverse(ary):
    ary_length = len(ary)

    i = 0;
    while (i < ary_length):
        last_value = ary.pop()
        ary.insert(i, last_value)
        i += 1

    return ary

b = range(15)
print 'b: {0}'.format(b)
ary = reverse(b)
print 'ary: {0}'.format(ary)
print 'b: {0}'.format(b)



