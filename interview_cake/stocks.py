import operator
import random

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

stock_prices_yesterday = map(lambda x: random.uniform(-100,100) + x, [500] * 1000)

@timmy
def profit(ary):
    i = 0
    peaks = {}
    valleys = {}
    previous = 0 

    while (len(ary) > i):
        current = ary[i]
        _next = ary[i+1] if i != len(ary)-1 else 0

        if   previous < current and current > _next: peaks[i] = current 
        elif previous > current and current < _next: valleys[i] = current

        previous = current
        i += 1

    valley_keys = valleys.keys
    calculate_profit = lambda peak_key, valley_key: peaks[peak_key] - valleys[valley_key]

    profits = {}

    for peak_key in peaks:
        for valley_key in valleys: 
            if peak_key > valley_key:
                profits[(peak_key, valley_key)] = calculate_profit(peak_key, valley_key)

    best_profit = max(profits.iteritems(), key=operator.itemgetter(1))
    return  best_profit


print profit(stock_prices_yesterday)

@timmy
def best(ary):
    i = 0
    min_price  = ary[0]
    max_profit = ary[1] - ary[0]

    while (len(ary) > i):
        current = ary[i]
        min_price = min(min_price, current)
        potential_price = current - min_price
        max_profit = max(max_profit, potential_price)
        i += 1

    return max_profit


print best(stock_prices_yesterday)



