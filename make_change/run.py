from make_change import compute_change_for_dollars
from string_currency import currency_to_string, convert_bills_to_sentence, convert_unit_counter_to_words, print_change

print """ Welcome to your bank!"""
continue_session = True

while (continue_session):
    user_input = raw_input("Please the amount you would like to withdraw in the form $100.23 or $100. We will then give you change. \n")
    amount = float(user_input)
    result = compute_change_for_dollars(amount)

    for k,v in result.iteritems():
        if v: print_change(v, k)

    finished_input = str(raw_input("Would you like to logout? Please enter the character 'y' or 'n'. \n")).replace("\r", "")

    continue_session = False if finished_input == "y" else True
    if continue_session == False: print "Goodbye." 
    else: print "Restarting..."




