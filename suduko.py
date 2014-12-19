
# coding: utf-8

# In[8]:

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


# In[9]:

def build_grid(puzzle):
    puzzle_lines = puzzle.splitlines()
    grid = []
    for output_line in generate_output_lines():
        grid.append(generate_output_row(output_line, puzzle.splitlines()))
    return grid

def generate_output_row(row_indexes, _input):
    output_row = []
    for row_index in row_indexes:
        values = _input[row_index]
        for column_index in (0, 1, 2):
            try:
                input_value = values[column_index]
            except IndexError:
                value = False
            else:
                value = input_value.isdigit() and int(input_value)
            output_row.append(value)
    return output_row

def generate_output_lines():
    for grid_row_index in (0, 1, 2):
        for nine_block_row_index in (0, 1, 2):                
            yield [nine_block_row_index + (offset * 3) + (grid_row_index * 9) for offset in (0, 1, 2)]


# In[10]:

def next_square(x, y):
    if x == 8:
        return 0, y + 1
    else:
        return x + 1, y


# In[11]:

all_nums = set(range(1, 10))

def check_grid(suduko_grid, last_update_x, last_update_y):
    row = suduko_grid[last_update_y]
    digits = [item for item in row if item]
    if len(digits) != len(set(digits)):
        return False
    if all(row) and set(row) != all_nums:
        return False
    
    column = [row[last_update_x] for row in suduko_grid]
    digits = [item for item in column if item]
    if len(digits) != len(set(digits)):
        return False
    if all(column) and set(column) != all_nums:
        return False
    
    return test_sub_grid(suduko_grid, last_update_x, last_update_y)


# In[12]:

sub_grid_indexes = {
                   0 : (0, 1, 2), 
                   1 : (0, 1, 2), 
                   2 : (0, 1, 2), 
                   3 : (3, 4, 5), 
                   4 : (3, 4, 5),
                   5 : (3, 4, 5),
                   6 : (6, 7, 8), 
                   7 : (6, 7, 8), 
                   8 : (6, 7, 8)
                   }
def test_sub_grid(suduko_grid, x, y):
    x_sub_grid_indexes = sub_grid_indexes[x]
    y_sub_grid_indexes = sub_grid_indexes[y]
    sub_grid_digits = [suduko_grid[y][x] for x in x_sub_grid_indexes for y in y_sub_grid_indexes]
    if all(sub_grid_digits) and set(sub_grid_digits) != all_nums:
        return False
    else:
        return True


# In[13]:

def grid_copy(grid):
    return [row[:] for row in grid] #faster than copy.deepcopy

def solve(suduko_grid, x=0, y=0):
    if not suduko_grid[y][x]:
        next_x, next_y = next_square(x, y)
        for guess in range(1, 10):
            suduko_grid[y][x] = guess
            if check_grid(suduko_grid, x, y):
                if x == y == 8:
                    return suduko_grid
                else:
                    solution = solve(grid_copy(suduko_grid), next_x, next_y)
                    if solution:
                        return solution
                    else:
                        pass
        return False
    else:
        if x == y == 8:
            return suduko_grid
        else:
            next_x, next_y = next_square(x, y)
            return solve(grid_copy(suduko_grid), next_x, next_y)
                


# In[18]:

get_ipython().magic(u'prun solve(build_grid(nov_26_hard))')


# In[17]:

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


# In[ ]:



