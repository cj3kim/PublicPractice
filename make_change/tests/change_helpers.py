def generate_expected_dollars_cents(dollars, cents):
    "dollars & cents are both dict where each is a subset of default"
    defaults = { 'dollars': { 100:0, 50:0, 20:0, 10:0, 5:0, 1:0 },
                   'cents': {  25:0, 10:0,  5:0, 1:0 }}

    for k, v in dollars.iteritems():
        defaults['dollars'][k] = v

    for k, v in cents.iteritems():
        defaults['cents'][k]   = v

    return defaults

