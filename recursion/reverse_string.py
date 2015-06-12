import re 

def reverse_string(string):
    if len(string) == 1: return string

    last_letter = string[-1]

    return last_letter + reverse_string(string[:-1])

string = reverse_string('hello world')
print 'string: {0}'.format(string)


def checkForPalindrome(string):
    removeSpace = lambda string: re.sub(r'\,,\.,\?,\s', '', string)

    return True if removeSpace(reverse_string(string)) == removeSpace(string) else False

a = checkForPalindrome('lol')
b = checkForPalindrome('meow')

print 'a: {0}'.format(a)
print 'b: {0}'.format(b)
