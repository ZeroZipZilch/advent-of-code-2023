import re
import sys
import itertools
import math
import collections


def run(input_rows: list[str]):
  rows = [list(row) for row in input_rows]

  row_length = len(rows[0])
  number_of_rows = len(rows)
  total = 0
  
  for x in range(row_length):
    first_possible_row = 0

    for y in range(number_of_rows):
      cell = rows[y][x]

      if cell == '#':
        first_possible_row = y + 1
        continue
    
      if cell == 'O':
        rows[y][x] = "."
        rows[first_possible_row][x] = "O"
        
        total += (number_of_rows - first_possible_row)

        first_possible_row += 1
  
  print(total)