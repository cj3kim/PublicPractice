
#give_change :: Int -> [Int] -> {Int}
def give_change(n, currency_units):
    change = init_change(currency_units)
    last_index_currency_units = len(currency_units) - 1

    i = 0
    while (last_index_currency_units >= i):
        current_unit = currency_units[i]
        if (current_unit <= n):
            n -= current_unit
            change[current_unit] += 1
        else:
            i += 1

    return change

# init_change :: [Int] -> {Int}
def init_change(currency_units):
    change = {}
    for v in currency_units:
        change[v] = 0
    return change

