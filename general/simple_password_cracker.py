import string
from itertools import product

#only for exploration
LOWERCASE_A_TO_Z = [i for i in string.lowercase[:26]]

def crack_it(unknown_string, password_length):
    g = product(LOWERCASE_A_TO_Z, repeat=password_length)

    for password in g:
        string_password = "".join(password)
        print string_password
        if string_password == unknown_string: return string_password

    return False


def permutations(iterable, r=None):
    # permutations('ABCD', 2) --> AB AC AD BA BC BD CA CB CD DA DB DC
    # permutations(range(3)) --> 012 021 102 120 201 210
    pool = tuple(iterable)
    n = len(pool)
    r = n if r is None else r
    if r > n:
        return
    indices = range(n)
    cycles = range(n, n-r, -1)
    yield tuple(pool[i] for i in indices[:r])
    while n:
        for i in reversed(range(r)):
            cycles[i] -= 1
            if cycles[i] == 0:
                indices[i:] = indices[i+1:] + indices[i:i+1]
                cycles[i] = n - i
            else:
                j = cycles[i]
                indices[i], indices[-j] = indices[-j], indices[i]
                yield tuple(pool[i] for i in indices[:r])
                break
        else:
            return


def test_crack_it():
    #password_length = 2
    #unknown_string  = "az"
    #assert crack_it(unknown_string, password_length) == "az"

    password_length = 5
    unknown_string  = "hello"
    assert crack_it(unknown_string, password_length) == "hello"



def all_perms(string):
    if len(string) <=1:
        yield string
    else:
        for perm in all_perms(string[1:]):
            for i in range(len(perm)+1):
                #nb string[0:1] works in both stringing and list contexts
                yield perm[:i] + string[0:1] + perm[i:]
