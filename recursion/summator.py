

ary = [x for x in range(0,10) if x % 2]

def recursive_summator(ary):
    popped_value = ary.pop(0)

    return popped_value + recursive_summator(ary) if len(ary) > 0 else popped_value;

total_sum = recursive_summator(ary)
print 'total_sum: {0}'.format(total_sum)


