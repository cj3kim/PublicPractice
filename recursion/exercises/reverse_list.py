def reverse_list(ary):
    last_value = ary.pop()
    if len(ary) > 0: reverse_list(ary)
    ary.insert(0, last_value)

# why did i fail the second time?
# I started from the first value when I needed to concentrate on the second value


def reverse_list_two(ary):
    first_value = ary.pop(0)
    if len(ary) > 0: reverse_list_two(ary) #array stops running after there's nothing left to pop
    ary.append(first_value) #base case for an array
    print 'ary: {0}'.format(ary)



ary = range(10)
reverse_list_two(ary)
print 'ary: {0}'.format(ary)



