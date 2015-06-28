from num2words import num2words

def print_change(unit_counts, _type):
    ary = convert_unit_counter_to_words(unit_counts, _type)
    message = convert_bills_to_sentence(ary)
    print message

def convert_unit_counter_to_words(unit_counts, _type):
    return ["{0} {1}".format(num2words(v), currency_to_string(v,k, _type)) for k,v in unit_counts.iteritems() if v != 0 ]

def currency_to_string(count, unit, _type):
    string_ary = ["$", str(unit)] if _type == "dollars" else [ str(unit), u'\u00A2'.encode('utf-8')]

    #if count > 1:
        #string_ary.append("s")

    string = "".join(string_ary)
    return string

def convert_bills_to_sentence(bills):
    last = bills.pop()
    if len(bills) == 0:
        return "Here's " + last + "."

    string = ", ".join(bills)
    result = "Here's " + string +  ", and " + last + "."
    return result

