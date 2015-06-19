
deliveries = []


#try this in n time

def find_missing_drone(deliveries):
    delivery_hash = {}

    for v in deliveries:
        if v in delivery_hash: delivery_hash[v] += 1
        else: delivery_hash[v] = 1

    for k,v in delivery_hash.iteritems():
        return key if v == 1 else False;

def find_undelivered_breakfast(delivery_ids):

    unique_delivery_id = 0

    for delivery_id in delivery_ids:
        unique_delivery_id ^= delivery_id

    return unique_delivery_id
