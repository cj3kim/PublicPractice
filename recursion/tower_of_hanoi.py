import sys

start = [x for x in reversed(range(3))];
start.pop()
temp  = []
dest  = []

def moveDisk(start_pole, temp_pole, dest_pole):
    print '\n'
    print 'start: {0}'.format(start)
    print 'temp: {0}'.format(temp)
    print 'dest: {0}'.format(dest)
    disk = start_pole.pop(0)
    if len(start_pole) == 0:
        dest_pole.append(disk)
    else:
        moveDisk(start_pole, dest_pole, temp_pole)
        dest_pole.append(disk);
        moveDisk(temp_pole, start_pole, dest_pole)

moveDisk(start, temp, dest)

print '\n'
print 'end'
print 'start: {0}'.format(start)
print 'temp: {0}'.format(temp)
print 'dest: {0}'.format(dest)

#http://stackoverflow.com/questions/27581683/trying-to-implement-recursive-tower-of-hanoi-algorithm-with-arrays
def hanoi(pegs, start, target, n):
    assert len(pegs[start]) >= n, 'not enough disks on peg'
    if n == 1:
        pegs[target].append(pegs[start].pop())
        print '%i -> %i: %s' % (start, target, pegs)
    else:
        aux = 3 - start - target  # start + target + aux = 3
        hanoi(pegs, start, aux, n-1)
        hanoi(pegs, start, target, 1)
        hanoi(pegs, aux, target, n-1)


rangeNum = sys.argv[0]
start = [x for x in reversed(range(sys.argv[0]))];
start.pop()
hanoi([[], [], []],0, 2, 4)

