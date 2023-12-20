import copy
from functools import cache
import hashlib
import pathlib
from json import dumps as json_dumps
import re
import sys
import itertools
import math
import collections
from tqdm import tqdm


def run(input_rows: list[str]):
  rows = [list(row) for row in input_rows]
  cycle_cache = {}
  cycle_order = []


  # with pathlib.Path('python/tasks/day14/output').open("w") as f:
  #   f.write('')
  # with pathlib.Path('python/tasks/day14/iterations-output').open("w") as f:
  #   f.write('')

  #   total = calculate_load(rows)
  #   f.write(f"BEFORE START - TOTAL: {total}\n")

  #   f.write('\n'.join([''.join(row) for row in rows]))
  #   f.write('\n')
  #   f.write('\n')
  
  for _ in tqdm(range(1000)):
    rows = cycle(copy.deepcopy(rows))

  total = calculate_load(rows)

  
  
  print(total)


def cycle(rows):
  rows = tilt_north(rows)
  rows = tilt_west(rows)
  rows = tilt_south(rows)
  rows = tilt_east(rows)

  return rows


def tilt_north(rows):
  row_length = len(rows[0])
  number_of_rows = len(rows)

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

        first_possible_row += 1

  return rows


def tilt_west(rows):
  row_length = len(rows[0])
  number_of_rows = len(rows)

  for y in range(number_of_rows):
    first_possible_column = 0

    for x in range(row_length):
      cell = rows[y][x]

      if cell == '#':
        first_possible_column = x + 1
        continue
    
      if cell == 'O':
        rows[y][x] = "."
        rows[y][first_possible_column] = "O"
        
        first_possible_column += 1

  return rows


def tilt_south(rows):
  row_length = len(rows[0])
  number_of_rows = len(rows)

  for x in range(row_length):
    first_possible_row = number_of_rows - 1

    for y in range(number_of_rows - 1, -1, -1):
      cell = rows[y][x]

      if cell == '#':
        first_possible_row = y - 1
        continue
    
      if cell == 'O':
        rows[y][x] = "."
        rows[first_possible_row][x] = "O"
        
        first_possible_row -= 1

  return rows


def tilt_east(rows):
  row_length = len(rows[0])
  number_of_rows = len(rows)

  for y in range(number_of_rows):
    first_possible_column = row_length - 1

    for x in range(row_length - 1, -1, -1):
      cell = rows[y][x]

      if cell == '#':
        first_possible_column = x - 1
        continue
    
      if cell == 'O':
        rows[y][x] = "."
        rows[y][first_possible_column] = "O"
        
        first_possible_column -= 1

  return rows


def calculate_load(rows):
  total = 0

  row_length = len(rows[0])
  number_of_rows = len(rows)

  for x in range(row_length):
    for y in range(number_of_rows):
      cell = rows[y][x]

      if cell == 'O':
        total += (number_of_rows - y)

  return total