from timeit import default_timer
from sys import argv

def timmy(fn):
    def decorator(*args):
        start_time = default_timer()
        print 'args: {0}'.format(args)
        fn(*args)
        end_time = default_timer()
        result_time = end_time - start_time
        print 'result_time: {0}'.format(result_time)

    return decorator

#n times to do the fib sequence
@timmy

#def fibonacci_print(previous, start, n):
    #_next = previous + start
    #string = str(_next)
    #return string if n == 0 else string + fibonacci_print(start, _next, n-1)

#fibonacci_print(0, 1, int(argv[1]))

def iter_fib(n):
    start = 1
    previous = 0

    string = ""

    while (n > 0):
        _next = start + previous
        string += str(_next)
        previous = start
        start    = _next

        n -= 1

    return string


start_time = default_timer()
string = iter_fib(int(argv[1]))
end_time = default_timer()

result_time = end_time - start_time

print 'result_time: {0}'.format(result_time)

storage = {}

def compute_result(key):
    if key in storage:
        return storage[key]
    else:
        result = c_fib(key)
        storage[key] = result
        return result

def c_fib(n):
    if (n < 2):
        return n
    else:
        key_left = n-1
        key_right = n-2

        result_left  = compute_result(key_left)
        result_right = compute_result(key_right)

        return result_left + result_right



start_time = default_timer()
result = c_fib(int(argv[1]))
end_time = default_timer()


result_time = end_time - start_time
print 'result_time: {0}'.format(result_time)



__fib_cache = {}
def fib(n):
    if n in __fib_cache:
        return __fib_cache[n]
    else:
        __fib_cache[n] = n if n < 2 else fib(n-2) + fib(n-1)
        return __fib_cache[n]

start_time = default_timer()
result = fib(int(argv[1]))
end_time = default_timer()


result_time = end_time - start_time

print 'result_time: {0}'.format(result_time)


def cachify(fn):
    cache = {}
    def decorated_fn (*args):
        if (args in cache):
            return cache[args]
        else:
            cache[args] = fn(*args)
            return cache[args]

    return decorated_fn




@cachify
def my_fib(n):
    if n < 2:
        return n
    else:
        return my_fib(n-1) + my_fib(n-2)


@timmy
def print_fib(m, fn):
    string = ""
    n = 0
    while (m > 0):
        fn(n)
        m -= 1
        n += 1


print 'print_fib: {0}'.format(print_fib)
print_fib(int(argv[1]), my_fib)


def memoize(f):
    cache = {}
    def decorated_function(*args):
        if args in cache:
            return cache[args]
        else:
            cache[args] = f(*args)
            return cache[args]
    return decorated_function

@memoize
def fib_a(n):
    return n if n < 2 else fib_a(n-2) + fib_a(n-1)


print_fib(int(argv[1]), fib_a)

