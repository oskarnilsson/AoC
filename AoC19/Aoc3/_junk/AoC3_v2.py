import numpy as np
import matplotlib.pyplot as plt


class Wire:

    def __init__(self):
        # Set start point to "visited"
        self.visitedRow = np.zeros(1, np.int)
        self.visitedColumn = np.zeros(1, np.int)
        self.position = [0, 0]

    def update_path(self, direction, length):
        # Update position (wire end) using initial pos self.position
        startRow, startCol = self.position[0], self.position[1]
        endRow, endCol = self.calculate_end_pos(direction, length, [startRow, startCol])
        self.position = [endRow, endCol]
        # Update wire path
        if startRow != endRow:
            # We have moved row wise
            if startRow < endRow:
                rowvec = np.arange(startRow + 1, endRow + 1)
            else:
                rowvec = np.arange(endRow, startRow + 1)

            self.visitedRow = np.append(self.visitedRow, rowvec)
            colvec = np.ones_like(rowvec) * endCol
            self.visitedColumn = np.append(self.visitedColumn, colvec)
        else:
            # We have moved column wise
            if startCol < endCol:
                colvec = np.arange(startCol + 1, endCol + 1)
            else:
                colvec = np.arange(endCol, startCol + 1)

            self.visitedColumn = np.append(self.visitedColumn, colvec)
            rowvec = np.ones_like(colvec) * endRow
            self.visitedRow = np.append(self.visitedRow, rowvec)

    @staticmethod
    def calculate_end_pos(direction, length, past_position):
        new_pos = past_position[:]
        addit = length
        if direction == "R":
            # Increment columns
            new_pos[1] += addit
        elif direction == "U":
            # Decrement rows
            new_pos[0] -= addit
        elif direction == "L":
            # Decrement columns
            new_pos[1] -= addit
        elif direction == "D":
            # Increment rows
            new_pos[0] += addit

        return new_pos[0], new_pos[1]

    def get_wire_vec(self, start_pos, end_pos, direction):
        sr, sc = start_pos[0], start_pos[1]
        er, ec = end_pos[0], end_pos[1]

        if direction == "R":
            # Increase cols - from start to end
            move_cols = np.arange(sc+1, ec+1)
            move_rows = np.ones_like(move_cols)*sr
        elif direction == "L":
            # "Decrease" cols - from end to start
            move_cols = np.arange(ec+1, sc+1)
            move_rows = np.ones_like(move_cols)*sr
        elif direction == "D":
            # Increase rows - from start to end
            move_rows = np.arange(sr+1, er+1)
            move_cols = np.ones_like(move_rows)*sc
        elif direction == "U":
            # "Decrease" rows - from end to start
            move_rows = np.arange(er+1, sr+1)
            move_cols = np.ones_like(move_rows)*sc

        return move_rows, move_cols

if __name__ == "__main__":
    # w1 = "R75,D30,R83,U83,L12,D49,R71,U7,L72"
    # w2 = "U62,R66,U55,R34,D71,R55,D58,R83"
    w1 = "R8,U5,L5,D3"
    w2 = "U7,R6,D4,L4"

    w1 = list(w1.split(","))
    w2 = list(w2.split(","))

    wire_one = Wire()
    m_rack = []
    m_cack = []
    for wire in w1:
        start_row, start_col = wire_one.position[0], wire_one.position[1]
        end_row, end_col = wire_one.calculate_end_pos(wire[0], int(wire[1:]), wire_one.position)
        m_r, m_c = wire_one.get_wire_vec([start_row, start_col], [end_row, end_col], wire[0])
        #wire_one.update_path(wire[0], int(wire[1:]))
        m_rack = np.append(m_rack, m_r)
        m_cack = np.append(m_cack, m_c)
        plt.plot(m_cack, m_rack, 'ro')
        plt.show()

    wire_two = Wire()
    for wire in w2:
        wire_two.update_path(wire[0], int(wire[1:]))
        plt.plot(wire_one.visitedColumn, wire_one.visitedRow, 'ro')
        plt.plot(wire_two.visitedColumn, wire_two.visitedRow, 'bo')
        plt.show()

    # for i in range(len(w1)):
    #   wire_one.update_path(w1[i][0], int(w1[i][1:]))
    #  wire_two.update_path(w2[i][0], int(w2[i][1:]))
    # Check for intersections
    # In common visited rows and cols
    # common_rows, w1_rind, w2_rind = np.intersect1d(wire_one.visitedRow, wire_two.visitedRow, return_indices=True)
    # common_cols, w1_cind, w2_cind = np.intersect1d(wire_one.visitedColumn, wire_two.visitedColumn, return_indices=True)
    # crossings = np.intersect1d(common_rows, common_cols)
    # Crossing @ (-5, 6)

    plt.plot(wire_one.visitedColumn, wire_one.visitedRow, 'ro')
    plt.plot(wire_two.visitedColumn, wire_two.visitedRow, 'bo')
    plt.show()
