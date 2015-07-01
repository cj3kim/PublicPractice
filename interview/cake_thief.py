import sys
INFINITY = sys.maxint


#This one is O(n * k)
def max_duffel_bag_value(cake_tuples, weight_capacity):
    max_values_at_capacities = [0] * (weight_capacity + 1)

    for current_capacity in xrange(weight_capacity + 1):
        current_max_value = 0
        for cake_weight, cake_value in cake_tuples:
            if (cake_weight == 0 and cake_value != 0): return INFINITY
            if (cake_weight <= current_capacity):
                max_value_using_cake = cake_value + max_values_at_capacities[current_capacity - cake_weight]
                current_max_value = max(max_value_using_cake, current_max_value)
        max_values_at_capacities[current_capacity] = current_max_value

    return max_values_at_capacities[weight_capacity]

#This one is slower because it's O(n^n)
def max_duffel_bag_value(cake_tuples, weight_capacity):
    result = [value + max_duffel_bag_value(cake_tuples, weight_capacity - weight) for weight, value in cake_tuples if weight <= weight_capacity ]
    return (0 if weight_capacity <= 0 or len(result) == 0 else max(result))

