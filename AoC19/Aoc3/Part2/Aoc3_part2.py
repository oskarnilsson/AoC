import numpy as np
import logging, sys
from Aoc3.Wiremodule.WireClasses import Wire
from operator import add

logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)


def dist(v, w):
    # Distance between two points - Manhattan style
    dx = abs(v[0] - w[0])
    dy = abs(v[1] - w[1])
    if dx != 0:
        return dx
    else:
        return dy


if __name__ == "__main__":
    # Run
    #w1 = "R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51"
    #w2 = "U98,R91,D20,R16,D67,R40,U7,R15,U6,R7"
    # ans 135, 410
    #w1 = "R75,D30,R83,U83,L12,D49,R71,U7,L72"
    #w2 = "U62,R66,U55,R34,D71,R55,D58,R83"
    # ans 159, 610
    #w1 = "R8,U5,L5,D3"
    #w2 = "U7,R6,D4,L4"
    # ans 6, 30
    f = open("C:/Users/jaosn/Documents/Python/AoC/Aoc3/Data/3_w1.txt", "r")
    w1 = f.readline()
    s1 = list(w1.split(","))
    f.close()
    f = open("C:/Users/jaosn/Documents/Python/AoC/Aoc3/Data/3_w2.txt", "r")
    w2 = f.readline()
    s2 = list(w2.split(","))

    s1 = list(w1.split(","))
    s2 = list(w2.split(","))
    w1 = Wire(s1)
    w2 = Wire(s2)

    print("Starting check for intersections")
    crossings = w1.check_for_crossings(w2)
    crossings = np.array(crossings, np.int)
    print("Crossings: ")
    print(crossings)
    manhattans = []
    for cross in crossings:
        manhattans.append(abs(cross[0]) + abs(cross[1]))
    print("Manhattan distances: ")
    print(manhattans)
    print("Min distance is: ", min(manhattans))

    # Calculate signal delay for each intersection
    cc = 0

    time_delay_1 = []
    time_delay_2 = []
    path_ack = 0
    for cross in crossings:
        # ID for segment of each crossing
        # Accumulate path length up to the crossing segment
        for j in range(w1.id_for_crossing_segments[cc]):
            segment = w1.get_segment(j)
            path_ack += segment.length
        # Add the distance in last segment UP to the crossing
        segment = w1.get_segment(w1.id_for_crossing_segments[cc])
        # Length to crossing
        ltc = dist(segment.start, cross)
        path_ack += ltc
        time_delay_1.append(path_ack)
        # Reset sum
        path_ack = 0

        # Wire two
        for j in range(w2.id_for_crossing_segments[cc]):
            segment = w2.get_segment(j)
            path_ack += segment.length
        segment = w2.get_segment(w2.id_for_crossing_segments[cc])
        # Length to crossing
        ltc = dist(segment.start, cross)
        path_ack += ltc
        time_delay_2.append(path_ack)
        # Reset sum
        path_ack = 0

        cc += 1
    # Total time delay - add the shit!
    ttd = list(map(add, time_delay_1, time_delay_2))
    print(ttd)
    print("Min delay: ", min(ttd))