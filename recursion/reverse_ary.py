
def reverse_ary(ary):
    last_value = ary.pop()
    if len(ary) > 0: reverse_ary(ary)
    ary.insert(0,last_value)

ary = range(10)
mem_address_old = hex(id(ary))

reverse_ary(ary)
mem_address_new = hex(id(ary))

print 'ary: {0}'.format(ary)
print 'mem_address_old: {0}'.format(mem_address_old)
print 'mem_address_new: {0}'.format(mem_address_new)
