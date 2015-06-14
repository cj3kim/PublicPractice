
import sys


def hanoi(pegs, start, target, n):
    calls += 1
    if n == 1: #the base case
        pegs[target].append(pegs[start].pop())
        print '-------------------'
        print pegs
    else:
        #n - 1 is the 'rest' of the problem that needs to be solved
        #in the previous algorithm, we passed around arrays instead of counts
        aux = 3 - start - target
        hanoi(pegs, start, aux, n-1) #n-1 here means the first two disks from the start pole is transferred to the aux
        hanoi(pegs, start, target, 1)
        hanoi(pegs, aux, target, n-1)



n = int(sys.argv[1])
pegA = [x for x in reversed(range(n)) ]
pegB = []
pegC = []
hanoi([pegA, pegB, pegC], 0, 2, n)

