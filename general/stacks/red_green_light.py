
from collections import deque


lane_a = deque(range(0,100))
lane_b = deque(range(0,100))


traffic_light = True

while (len(lane_a) > 0 and len(lane_b) > 0 ):
    if traffic_light: lane_a.pop()
    else: lane_b.pop()

    if (len(lane_a) % 5 == 0 or len(lane_b) % 5 == 0):
        traffic_light = not traffic_light
        print '--------------------'
        print 'green' if traffic_light else 'red'
        print "lane_a", "lane_b"
        print len(lane_a), len(lane_b)




