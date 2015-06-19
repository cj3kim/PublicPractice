from operator import itemgetter, mul
from timeit import default_timer
from sys import argv

def timmy(fn):
    def decorator(*args):
        start_time = default_timer()
        result = fn(*args)
        end_time = default_timer()
        result_time = end_time - start_time
        print 'result_time: {0}'.format(result_time)
        return result

    return decorator

@timmy
def compute_pseudo_product(ary):
    setA = set(range(len(ary)))
    def compute_product(k):
        keys = setA.difference(set([k]))
        return reduce(mul, map(lambda k: ary[k], keys))

    return [ compute_product(k) for k,v in enumerate(ary) ]


ary = range(int(argv[1]))
ary.pop(0)
n2_computation = compute_pseudo_product(ary)
print 'n2_computation: {0}'.format(n2_computation)

#unfortunately, this is O(n^2)



@timmy
def get_products_of_all_ints_except_at_index(int_array):

    # we make an array with the length of the input array to
    # hold our products
    products_of_all_ints_except_at_index = [1] * len(int_array)
    
    # for each integer, we find the product of all the integers
    # before it, storing the total product so far each time
    product = 1
    i = 0
    while i < len(int_array):
        products_of_all_ints_except_at_index[i] = product
        product *= int_array[i]
        i += 1
    
    # for each integer, we find the product of all the integers
    # after it. since each index in products already has the
    # product of all the integers before it, now we're storing
    # the total product of all other integers
    product = 1
    i = len(int_array) - 1
    while i >= 0:
        products_of_all_ints_except_at_index[i] *= product
        product *= int_array[i]
        i -= 1

    return products_of_all_ints_except_at_index


print get_products_of_all_ints_except_at_index(ary)
