from operator import itemgetter, mul

ary = [1,2,3]
expected = [6, 3, 2]

def compute_pseudo_product(ary):
    setA = set(range(len(ary)))
    def compute_product(k):
        keys = setA.difference(set([k]))
        return reduce(mul, map(lambda k: ary[k], keys))

    return [ compute_product(k) for k,v in enumerate(ary) ]


print compute_pseudo_product(ary)

print compute_pseudo_product([0,0,0,0])
