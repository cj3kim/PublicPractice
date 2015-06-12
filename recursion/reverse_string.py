
def reverse_string(string):
    if len(string) == 1: return string

    last_letter = string[-1]

    return last_letter + reverse_string(string[:-1])

string = reverse_string('hello world')
print 'string: {0}'.format(string)

