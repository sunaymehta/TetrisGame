SIMPLIFIED TETRIS ENGINE

This project implements a simplified Tetris engine in Python. It was designed according to
a specific set of rules that closely resemble standard Tetris mechanics but with significant 
simplifications:

1. No piece rotation by the user — each piece has a fixed orientation.
2. Gravity — pieces drop from the top until they rest on either the bottom of the grid 
   or on top of other pieces.
3. Line clears — whenever a row is completely filled, it is removed, and everything above it
   is shifted down by one row. The contents within each row remain the same (no partial 
   "gap filling").
4. Pieces — only the Q, Z, S, T, I, L, and J Tetris shapes are used.

After reading a line of input describing a sequence of dropped pieces, the program computes
the final stack height of blocks in a 10-column, 100-row grid.

------------------------------------------------------------------------
GOALS

- Simulate a rudimentary Tetris environment without rotation, in which each piece’s
  orientation is fixed.
- Remove full rows automatically whenever a row of 10 columns is completely occupied.
- Track the final height of the stacked pieces after every piece on a line has been placed.
- Produce a numerical output (the final height) for each line of inputs in the file.

------------------------------------------------------------------------
ASSUMPTIONS

1. Grid Size:
   - Width (columns) = 10
   - Height (rows) = 100

2. Row Numbering:
   - Row 0 is at the bottom of the grid.
   - Row 99 is the top of the grid.

3. Shapes:
   - Each of the 7 Tetris pieces (Q, Z, S, T, I, L, J) is defined by exactly 4 squares
     in a fixed arrangement (no rotation).
   - The shape “offsets” are stored as (row_offset, col_offset) pairs relative to
     the bottom-left cell of the piece.

4. No Invalid Inputs:
   - We assume all input lines are valid and do not place pieces out of bounds.
   - We assume the final height does not exceed 100.

5. Dropping Logic:
   - A piece is placed by specifying something like T3, meaning a T shape’s leftmost
     column is 3.
   - The piece falls as far down as it can without overlapping existing blocks or 
     going below row 0.

6. Line Clearing:
   - If a row is completely full (all 10 columns occupied), it is removed and
     everything above shifts down one row.

7. Output:
   - After processing each line of input (which may contain multiple piece specifications),
     the program prints one integer that is the final occupied height of the stack.
   - Height = (index of highest occupied row) + 1. If no blocks are placed, height = 0.

------------------------------------------------------------------------
REPOSITORY STRUCTURE

- engine01.py
  - Contains the main logic:
    1) solve_tetris_line(line) function that processes a comma-separated list of pieces.
    2) A main() function that reads lines from a file (input.txt), applies solve_tetris_line,
       and prints the final height.

- input.txt
  - A sample input file with 10 lines, each describing a sequence of pieces.

- README.txt
  - Explains the project goals, assumptions, code flow, and how to run and interpret results.

------------------------------------------------------------------------
HOW TO RUN THE PROGRAM

1) Ensure you have Python 3 installed on your system.
2) Place engine01.py and input.txt in the same directory.
3) Open a terminal in that directory.
4) Run the script:
      python engine01.py < input.txt > output.txt
  This will read from input.txt on standard input and write each final height to output.txt.

------------------------------------------------------------------------
UNDERSTANDING THE CODE

1) Initialization:
   - A 10×100 grid is created. Each cell is initially False (empty).

2) Line Parsing:
   - A line like "Q0,I4,Z3" is split by commas into tokens: ["Q0", "I4", "Z3"].
   - Each token’s first character is the shape letter (e.g. 'Q'), and the remainder is 
     the integer column offset (e.g. 0 for "Q0").

3) Shape Offsets:
   - Each piece is stored as four (row_offset, col_offset) pairs in a dictionary called shapes.
   - Example: 'Q': [(0,0), (0,1), (1,0), (1,1)] for the 2x2 square.

4) Dropping a Piece:
   - For shape T at column 3, start at row=0 and keep incrementing while can_place(...) is True.
   - Once can_place(...) becomes False, revert to the last valid row and place the piece permanently.

5) Removing Full Rows:
   - After placing each piece, we scan from row=0 up to row=99 to find fully occupied rows.
   - If we find one, we remove it and shift everything above down, then recheck that row 
     to catch consecutive full rows.

6) Final Height:
   - After all pieces are placed and rows cleared, we look for the highest occupied row.
   - Final height = (highest row index) + 1, or 0 if no cells are occupied.

------------------------------------------------------------------------
SAMPLE INPUT AND OUTPUT

The provided input.txt has 10 lines. For each line, the program prints a single line 
with the final stack height.

Example:
  input.txt
      Q0
      I0,I4,Q8
      T1,Z3,I4
      ...

  Running:
      python engine01.py

  You will see 10 lines of output, one for each line in input.txt.

------------------------------------------------------------------------
HOW TO READ THE OUTPUT

- Each line of output is a single integer representing the maximum occupied row + 1.
- If the output is 3, that means the highest occupied row is row=2 from the bottom.
- If the output is 0, it means no cells ended up occupied (an empty grid).

------------------------------------------------------------------------
EDGE CASES

- Multiple Consecutive Full Rows:
  The code handles repeated row clears if newly shifted rows are also full.
- Pieces at Columns 8 or 9:
  The engine ensures columns do not go out of range.
- Tall Stacks:
  We assume we never exceed row index 99.
- S/Z Collisions:
  The "jutting" shape collisions are handled by the can_place(...) check 
  before dropping further.

------------------------------------------------------------------------
CONTACT / NOTES

- This is a simplified Tetris: no rotation, no user input for movement, 
  no scoring, etc.
- If you have any questions, suggestions, or want to extend it to support 
  piece rotation or a GUI, feel free to modify the script further.

Thank you for reviewing this project!
