

#https://www.interviewcake.com/question/recursive-string-permutations

def perm_recursive_string(characters):
    if len(characters) == 2:
        result = [characters[1], characters[0]]
        return result
    else:
        first = characters[:1]
        rest  = characters[1:]
        first.extend(perm_recursive_string(rest))
        return first







old_text = 'a,b,c,d,e'
text = old_text.split(',');


def generate(text):
    strings = []
    permutations = len(text) - 1
    for c in text:
        i = 0
        while (permutations > i):
            text = perm_recursive_string(text)
            print 'text: {0}'.format(text)
            strings.append(text)
            i += 1
        text.append(text.pop(0))
generate(text)


def get_permutations(string):
    # base case
    if len(string) <= 1:
        return [string]

    all_chars_except_last = string[:-1]
    last_char = string[-1]

    # recursive call: get all possible permutations for all chars except last
    permutations_of_all_chars_except_last = get_permutations(all_chars_except_last)



get_permutations('abcde')
