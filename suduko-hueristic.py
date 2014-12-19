
# coding: utf-8

# In[11]:

from collections import defaultdict


# In[59]:

#Nov 26 Hard
nov_26_hard = """ 1
4 7
  3
4
 3
 7
3
  6
 5
7
 3
8
28

 67
  1
 8
  2
 9
2
  8
 1
 4
  9
8
7 9
 6
"""


# In[4]:

#Nov 24, easy
nov_24_easy = '''721



 71
6
53
  9
8 7
 72
9


3 6


  4
68
2 4
8
 67
  7
43



341
'''


# In[5]:

def build_grid(puzzle):
    puzzle_lines = puzzle.splitlines()
    grid = []
    for output_line in generate_output_lines():
        grid.append(generate_output_row(output_line, puzzle_lines))
    return grid

def generate_output_row(row_indexes, _input):
    output_row = []
    for row_index in row_indexes:
        values = _input[row_index]
        for column_index in (0, 1, 2):
            try:
                input_value = values[column_index]
            except IndexError:
                value = None
            else:
                value = input_value.isdigit() and int(input_value)
            output_row.append(value)
    return output_row

def generate_output_lines():
    for grid_row_index in (0, 1, 2):
        for nine_block_row_index in (0, 1, 2):                
            yield [nine_block_row_index + (offset * 3) + (grid_row_index * 9) for offset in (0, 1, 2)]


# In[42]:

class GridSquare(object):
    all_possible_values = set(range(1, 10))
    def __init__(self, value, row, column, sub_grid):
        self.value = value
        self.row = row
        self.column = column
        self.sub_grid = sub_grid
        self.row.add(self)
        self.column.add(self)
        self.sub_grid.add(self)
     
    @property
    def possible_values(self):
        same_row_values = self.collection_values(self.row)
        same_column_values = self.collection_values(self.column)
        same_sub_grid_values = self.collection_values(self.sub_grid)
        return (((self.all_possible_values - same_row_values) - same_column_values) - same_sub_grid_values)
    
    @staticmethod
    def collection_values(collection):
        return set(square.value for square in collection if square.value)
    
    def __repr__(self):
        return self.value and str(self.value) or ' '


# In[17]:

sub_grid_map = {0 : 0, 
                1 : 0, 
                2 : 0, 
                3 : 1, 
                4 : 1, 
                5 : 1, 
                6 : 2, 
                7 : 2, 
                8 : 2}
def link_grid(grid):
    rows = [set() for _ in range(9)]
    columns = [set() for _ in range(9)]
    sub_grids = defaultdict(set)
    empty_squares = set()
    dynamic_grid = [[] for _ in range(9)]
    
    for y in range(9):
        for x in range(9):
            value = grid[y][x]
            row = rows[y]
            column = columns[x]
            sub_grid = sub_grids[(sub_grid_map[x], sub_grid_map[y])]
            square = GridSquare(value, row, column, sub_grid)
            if not value:
                empty_squares.add(square)
            dynamic_grid[y].append(square)
    return dynamic_grid, empty_squares


# In[74]:

def solve(empty_squares):
    next_square = sorted(empty_squares, key=lambda square : len(square.possible_values))[0]
    empty_squares.remove(next_square)
    if not empty_squares:
        next_square.value = next_square.possible_values.pop()
        return True
    else:
        for possible_value in next_square.possible_values:
            next_square.value = possible_value
            solution = solve(empty_squares)
            if solution:
                return True
            else:
                continue
        else:
            next_square.value = None
            empty_squares.add(next_square)
            return False
            


# In[78]:

grid = build_grid(nov_26_hard)
linked_grid, empty_squares = link_grid(grid)
get_ipython().magic(u'prun solve(empty_squares)')


# In[72]:

linked_grid


# In[ ]:



