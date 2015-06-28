
def compute_change_for_dollars(total_amount):
    "We will assume compute_change_for_dollars is a float for now"
    DOLLAR_UNITS = [100, 50, 20, 10, 5, 1]
    COIN_UNITS   = [25, 10, 5, 1]

    toIntRatio = 100

    #overshadow total_amount through copy by sharing.
    total_amount = int(total_amount*toIntRatio) 
    dollars = total_amount / toIntRatio
    cents   = total_amount % toIntRatio

    return {
        'dollars': give_change(dollars, DOLLAR_UNITS)
        , 'cents': give_change(cents, COIN_UNITS)
    }



#give_change :: Int -> [Int] -> {Int}
def give_change(n, currency_units):
    if n == 0: return None
    "Takes n units of currency and gives changes according to currency_units. Greedy algorithm is used."
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
    "Initializes a hash of currency_units with counters set to 0"

    change = {}
    for v in currency_units:
        change[v] = 0
    return change

