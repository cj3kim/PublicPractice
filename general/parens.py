from collections import deque

def parensBalanceCheck(string):
    stack_level = 0;
    stack = deque([])
    starting_braces = { "(": ")", "{": "}", "[": "]"}
    ending_braces   = { ")": "(", "}": "{", "]": "["}

    for i, _char in enumerate(string):
        if _char in starting_braces:
            stack.append((stack_level, _char))
            stack_level += 1

        if _char in ending_braces:
            if len(stack) == 0: return False
            else:
                unknown_brace = ending_braces[_char]
                pair = stack[-1]
                start_brace = pair[1]

                if start_brace == unknown_brace:
                    stack.pop();
                    stack_level -= 1
                else:
                    return False


    return False if len(stack) > 0 else True

def test_answer():
    string = "(){}"
    assert parensBalanceCheck(string) == True

    string = ")(){}"
    assert parensBalanceCheck(string) == False

    string = "({[]})"
    assert parensBalanceCheck(string) == True

    string = "({([])})"
    assert parensBalanceCheck(string) == True

    string = "({([])}) () ({ (){}([])})"
    assert parensBalanceCheck(string) == True

    string = "({[()}]) ({[]})"
    assert parensBalanceCheck(string) == False

    string = "({[()}])"
    assert parensBalanceCheck(string) == False

    string = "({[}])"
    assert parensBalanceCheck(string) == False



