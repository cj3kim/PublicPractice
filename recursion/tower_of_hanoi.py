
start = [x for x in reversed(range(4))];
start.pop()
temp  = []
dest  = []

def moveDisk(start_pole, temp_pole, dest_pole):
    print '\n'
    print 'start: {0}'.format(start)
    print 'temp: {0}'.format(temp)
    print 'dest: {0}'.format(dest)



    disk = start_pole.pop(0)

    if len(start_pole) > 0:
        moveDisk(start_pole, dest_pole, temp_pole)
        dest_pole.append(disk);
        moveDisk(temp_pole, start_pole, dest_pole)
    else:
        dest_pole.append(disk)


moveDisk(start, temp, dest)
print '\n'
print 'end'
print 'start: {0}'.format(start)
print 'temp: {0}'.format(temp)
print 'dest: {0}'.format(dest)

#FUNCTION MoveTower(disk, source, dest, spare):
#IF disk == 0, THEN:
    #move disk from source to dest
#ELSE:
    #MoveTower(disk - 1, source, spare, dest)   // Step 1 above
    #move disk from source to dest              // Step 2 above
    #MoveTower(disk - 1, spare, dest, source)   // Step 3 above
#END IF

