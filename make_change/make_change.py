

def give_change(n, currency_units):
    change = {}
    last_index_currency_units = currency_units.length - 1

    i = 0
    while (last_index_currency_units > i):
        current_unit = currency_units[i]
        if (current_unit <= n):
            n -= current_unit
            change[current_unit] += 1
        else:
            i += 1

    return change
