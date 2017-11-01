#N^4 time


def n4_substring_matcher(stringA, stringB):
    print """
        In this block of code, we loop through all possible permutations with repeats
    """
    longest_substring = ""
    for i, ic in enumerate(stringA):
        for j, jc in enumerate(stringA):
            for k, kc in enumerate(stringB):
                for l, lc in enumerate(stringB):
                    substringA = stringA[i:j]
                    if (substringA == stringB[k:l]):
                        if len(substringA) > len(longest_substring):
                            longest_substring = substringA
    return longest_substring


#N3 time
def n3_substring_matcher(stringA, stringB):
    longest_substring = ""
    for i, ic in enumerate(stringA):
        for j, jc in enumerate(stringA):
            if i > j: continue
            for k, kc in enumerate(stringB):
                if k+(j-i) > len(stringB): break
                substringA = stringA[i:j]
                substringB = stringB[k:j-i] # j-i is the current length of substring searched for from index k
                if (substringA == substringB) and (len(substringA) > len(longest_substring)):
                    longest_substring = substringA

    return longest_substring


def test_n4():
    stringA = "hello, my name is chris"
    stringB = "my name is Andrew, hello"
    assert n4_substring_matcher(stringA, stringB) == "my name is "

def test_n3():
    #Uncomment these when you have an O(n) search algorithm

    #fileA = open("basehead.txt", "r")
    #fileB = open("cybrtrsh.txt", "r")

    #stringA = fileA.read().replace('\n', '')
    #stringB = fileB.read().replace('\n', '')

    stringA = "hello, my name is chris"
    stringB = "my name is Andrew, hello"
    assert n3_substring_matcher(stringA, stringB) == "my name is "


