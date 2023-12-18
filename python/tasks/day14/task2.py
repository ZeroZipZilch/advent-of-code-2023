import re
import sys
import itertools
import math
import collections


def run(input_rows: list[str]):
  rows = [list(row) for row in input_rows]
  
  for _ in range(100):
    tilt_north(rows)
    tilt_west(rows)
    tilt_south(rows)
    tilt_east(rows)

    for row in rows:
      print(''.join(row))
    
    print(" ")
    
    total = calculate_load(rows)
    
    print(" ")
    print(" ")

  total = calculate_load(rows)

  
  
  print(total)


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