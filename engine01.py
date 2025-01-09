
def solve_tetris_line(line):

    # -- 1. Define the rigid shapes (row offsets, col offsets)
    #    We define row=0 at the *bottom* of the shape, so that placing the shape
    #    at base-row R means a square with offset_row = r_off is at row = R + r_off.
    #    The offsets below match the illustration, reading upward from the bottom.
    shapes = {
        'Q': [(0,0), (0,1), (1,0), (1,1)],  # 2x2 square 
        'Z': [(0,1), (0,2), (1,0), (1,1)],  # Z shape
        'S': [(0,0), (0,1), (1,1), (1,2)],  # S shape
        'T': [(0,1), (1,0), (1,1), (1,2)],  # T shape 
        'I': [(0,0), (0,1), (0,2), (0,3)],  # I shape, horizontal 
        'L': [(0,0), (0,1), (1,0), (2,0)],  # L shape 
        'J': [(0,0), (0,1), (1,1), (2,1)],  # J shape (mirrored L) 
    }

    # -- 2. Create an empty grid.  We'll store True/False for "occupied?".
    #    Row 0 is the bottom, row 99 is the top, columns 0..9.
    ROWS = 100
    COLS = 10
    grid = [[False]*COLS for _ in range(ROWS)]

    def can_place(r, c, shape_offsets):
        """
        Check if placing the given shape with base-row = r, left-column = c
        collides or goes out of bounds.  Return True if it's valid (no collision).
        """
        for (r_off, c_off) in shape_offsets:
            rr = r + r_off
            cc = c + c_off
            # Check row out of range or column out of range
            if not (0 <= rr < ROWS):
                return False
            if not (0 <= cc < COLS):
                return False
            # Check if occupied
            if grid[rr][cc]:
                return False
        return True

    def place_shape(r, c, shape_offsets):
        """
        Actually place the shape squares into the grid (mark them True).
        """
        for (r_off, c_off) in shape_offsets:
            rr = r + r_off
            cc = c + c_off
            grid[rr][cc] = True

    def remove_full_rows():
        r = 99
        while r > 0:
            if all(grid[r][c] for c in range(COLS)):
                # print (r)
                # Remove row r: shift everything above down by 1
                for rr in range(r, 0, -1):
                    grid[rr] = grid[rr-1][:]
                # The topmost row (index ROWS-1) becomes empty
                grid[0] = [False]*COLS
                # Do NOT increment r, because we need to check the same row again
                # after shifting (the row that was above r is now at r).
            else:
                r -= 1
        return grid

    tokens = [x.strip() for x in line.split(',')]
    for token in tokens:
        # e.g. "Q0" => shape=Q, left_col=0
        shape_letter = token[0]
        left_col = int(token[1])

        shape_offsets = shapes[shape_letter]

        # Start from row=0 and go up until you can't place at row+1
        row_placement = 0
        # Keep going while you can place at row_placement+1
        while can_place(row_placement+1, left_col, shape_offsets):
            row_placement += 1

        # Now place the shape at row_placement
        place_shape(row_placement, left_col, shape_offsets)

        # Check for full rows and remove them
        remove_full_rows()

    # -- 4. After all pieces, compute the final height = max row occupied + 1
    for r in range(ROWS):
        for c in range(COLS):
            if grid[r][c]:
                final_height = 100-r
                return [grid, final_height]
            else:
                pass


if __name__ == "__main__":

    # Example 1:
    # Input: "I0,I4,Q8"
    # The result described: bottom row fills, gets removed, final height = 1
    example1 = "I0,I4,Q8"
    print("Example 1 input: ", example1)
    print("Example 1 output:", solve_tetris_line(example1)[1])
    print()

    # Example 2:
    # Input: "T1,Z3,I4"
    # No full row forms, final height = 4
    example2 = "T1,Z3,I4"
    print("Example 2 input: ", example2)
    print("Example 2 output:", solve_tetris_line(example2)[1])
    print()

    # Example 3:
    # Input: "Q0,I2,I6,I0,I6,I6,Q2,Q4"
    # The final height described is 3
    example3 = "Q0,I2,I6,I0,I6,I6,Q2,Q4"
    print("Example 3 input: ", example3)
    print("Example 3 output:", solve_tetris_line(example3)[1])
    print()

    #
    # If you want to run against an entire file "input.txt" via stdin, you can do:
    #
import sys
for line in sys.stdin:
    line = line.strip()
    if not line:
        continue
    print(solve_tetris_line(line)[1])

