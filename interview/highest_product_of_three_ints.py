from sys import argv
from operator import mul
from itertools import combinations

from timeit import default_timer

def timmy(fn):
    def decorator(*args):
        start_time = default_timer()
        result = fn(*args)
        end_time = default_timer()
        result_time = end_time - start_time
        print 'result_time: {0}'.format(result_time)
        return result

    return decorator

ary = eval(argv[1])

@timmy
def computeHighestProductOfThreeInts(ary):
    ary.sort()
    return reduce(mul, ary[-3:])

result = computeHighestProductOfThreeInts(ary)

print 'This one only deals with positive use cases'
print 'result: {0}'.format(result)


@timmy
def optimizedComputeHighestProductOfThreeInts(ary):
    ary.sort()
    smallest = ary[:3]
    largest  = ary[-3:]
    smallest.extend(largest)
    integers = set(smallest)

    choose = 3
    all_possible_combos = [comb for comb in combinations(integers, choose)]

    return max(map(lambda x: reduce(mul,  x), all_possible_combos))


result = optimizedComputeHighestProductOfThreeInts(ary)
print 'optimized result: {0}'.format(result)



@timmy
def highest_product_of_3(array_of_ints):
    if len(array_of_ints) < 3:
        raise Exception("Less than 3 items!")

    # We're going to start at the 3rd item (at index 2)
    # so pre-populate highests and lowests based on the first 2 items.
    # The alternative is starting these as None and checking below if they're set
    # I think this is a little cleaner, but it's debatable.
    highest = max(array_of_ints[0], array_of_ints[1])
    lowest = min(array_of_ints[0], array_of_ints[1])

    highest_product_of_two = array_of_ints[0] * array_of_ints[1]
    lowest_product_of_two = array_of_ints[0] * array_of_ints[1]

    # Except this one--we pre-populate it for the first /3/ items.
    # This means in our first pass it'll check against itself, which is fine.
    highest_product_of_three = array_of_ints[0] * array_of_ints[1] * array_of_ints[2]

    # walk through items, starting at index 2
    for current in array_of_ints[2:]:

        # do we have a new highest product of 3?
        # it's either the current highest, 
        # or the current times the highest product of two
        # or the current times the lowest product of two
        highest_product_of_three = max(
            highest_product_of_three,
            current * highest_product_of_two,
            current * lowest_product_of_two)

        # do we have a new highest product of two?
        highest_product_of_two = max(
            highest_product_of_two,
            current * highest,
            current * lowest)

        # do we have a new lowest product of two?
        lowest_product_of_two = min(
            lowest_product_of_two,
            current * highest,
            current * lowest)

        # do we have a new highest?
        highest = max(highest, current)

        # do we have a new lowest?
        lowest = min(lowest, current)

    return highest_product_of_three


most_optimized = highest_product_of_3(ary)
print 'most_optimized: {0}'.format(most_optimized)
