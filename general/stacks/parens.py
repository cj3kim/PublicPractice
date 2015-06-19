from collections import deque

def parens_balance_check(string):
    stack = deque([])
    starting_braces = { "(": ")", "{": "}", "[": "]"}
    ending_braces   = { ")": "(", "}": "{", "]": "["}

    for i, _char in enumerate(string):
        if _char in starting_braces:
            stack.append(_char)
        if _char in ending_braces:
            if len(stack) == 0: return False
            else:
                unknown_brace = ending_braces[_char]
                start_brace = stack[-1]

                if start_brace == unknown_brace:
                    stack.pop();
                else:
                    return False


    return False if len(stack) > 0 else True

def test():
    string = "(()((())()))"
    assert parens_balance_check(string)

    string = "(){}"
    assert parens_balance_check(string) == True

    string = ")(){}"
    assert parens_balance_check(string) == False

    string = "({[]})"
    assert parens_balance_check(string) == True

    string = "({([])})"
    assert parens_balance_check(string) == True

    string = "({([])}) () ({ (){}([])})"
    assert parens_balance_check(string) == True

    string = "({[()}]) ({[]})"
    assert parens_balance_check(string) == False

    string = "({[()}])"
    assert parens_balance_check(string) == False

    string = "({[}])"
    assert parens_balance_check(string) == False


print "We can solve the problem because of the stack architecture.\n"

print """
    Each time we push a start brace onto the stack, we implicitly acknowledge an increment in
    depth. When we find an end brace, we compare it to the top of the stack to see if it
    matches the start brace. If the start and end brace do not form a proper pair, it means the
    parenthenses aren't balanced in the string. If they do match, we pop the stack to decrement
    our implicit depth and continue our balance checking. \n 
"""
print """
    This technique allows us to traverse all depths and check the balance 
    of parens - nested or in sequence - found at each depth. It feels almost like recursion.
"""



