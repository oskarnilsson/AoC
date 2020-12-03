import logging, sys
import numpy as np


# noinspection SpellCheckingInspection
class Wire:
    # logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)

    totalnumberofwires = 0  # This will only keep track of total number of instances

    def __init__(self, *args):
        self.segments = []
        self.numberOfSegments = 0
        self.end_pos = [0, 0]
        if len(args) > 0:
            for arg in args[0]:
                self.add_segment(arg)

        type(self).totalnumberofwires += 1
        self.id_for_crossing_segments = []

    def add_segment(self, instruction):
        logging.debug('Adding segment %s to wire', instruction)
        # ID for segment and instruction for segment
        seg = Wiresegment(self.numberOfSegments, instruction, self.end_pos)
        self.segments.append(seg)
        self.numberOfSegments += 1
        # Update wire end position to latest segments end point
        self.end_pos = seg.end
        logging.info("Added segment to wire. %d segments so far", self.numberOfSegments)

    def check_for_crossings(self, wire):
        # self is wire one
        # wire is wire two
        crossings = []
        cross_id_1 = []
        cross_id_2 = []
        # For every segment in this line
        for segment in self.segments:
            # Find any overlap w/ each segment in wire.segments
            for other_segment in wire.segments:
                # Compare segment with other_segment
                p = segment.start
                r = np.multiply(segment.dir, segment.length)
                q = other_segment.start
                s = np.multiply(other_segment.dir, other_segment.length)
                rxs = self.cross(r, s)
                if rxs != 0:
                    # Calculate u = (q-p) x r / (r x s)
                    qp = self.sub(q,p)
                    nom = self.cross(qp, r)
                    u = nom/rxs
                    if 0 < u < 1:
                        # Calculate t = (q-p) x s / (r x s)
                        nom = self.cross(qp, s)
                        t = nom/rxs
                        if 0 < t < 1:
                            print("Intesection")
                            #Crossing coordinates
                            crossing = q + u*s
                            crossings.append(crossing)
                            cross_id_1.append(segment.id)
                            cross_id_2.append(other_segment.id)

        self.id_for_crossing_segments = cross_id_1
        wire.id_for_crossing_segments = cross_id_2
        return crossings

    @staticmethod
    def cross(v, w):
        # 2D cross product - scalar
        prod = v[0]*w[1] - v[1]*w[0]
        return prod

    @staticmethod
    def sub(v, w):
        return [v[0]-w[0], v[1]-w[1]]

    def get_segment(self, id):
        return self.segments[id]

    def __del__(self):
        type(self).totalnumberofwires -= 1


# noinspection SpellCheckingInspection
class Wiresegment:
    # logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)

    def __init__(self, id, command, pos):
        self.id = id
        self.dir = [0, 0]  # Normal vector
        self.length = 0
        self.end = []
        logging.info("New Wiresegment, id: %d", id)
        self.start = pos
        self.lay_wire(command)

    def lay_wire(self, command):
        self.dir = self.get_direction(command)
        self.length = int(command[1:])
        self.end = self.update_end_pos(self.start, self.dir, self.length)

    @staticmethod
    def update_end_pos(start, direction, length):
        path = np.multiply(direction, length)
        end = start + path
        return end

    @staticmethod
    def get_direction(move):
        dir_string = move[0]
        if dir_string == "R":
            return [1, 0]
        elif dir_string == "L":
            return [-1, 0]
        elif dir_string == "D":
            return [0, -1]
        elif dir_string == "U":
            return [0, 1]
        else:
            raise Exception("Direction not handled!")
