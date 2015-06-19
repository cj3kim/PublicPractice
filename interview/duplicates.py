


def detectDuplicates(ary):
    value_counts = {}

    for v in ary:
        if v in value_counts:
            value_counts[v] += 1
        else:
            value_counts[v] = 1

    return value_counts


results = detectDuplicates([1,2,3,3,3,3,4,5,5,5,5,6])
print 'results: {0}'.format(results)





