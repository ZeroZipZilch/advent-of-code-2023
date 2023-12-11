import re
import sys
import itertools
import math
import collections

def run(input_rows: list[str]):
  input_lists = [list(row) for row in input_rows]
  expand_by = 1000000

  galaxy_coordinates, expanded_space_rows, expanded_space_columns = expand_universe(input_lists)
  total_distances = 0

  # for each index in galaxy_coordinates, loop through each index in galaxy_coordinates
  # and calculate the distance between the two
  # if the from or to coordinate is in expanded_space, add the expanded_space value to the total_distance

  for (i, from_coordinate) in enumerate(galaxy_coordinates):
    for (j, to_coordinate) in enumerate(galaxy_coordinates):
      # Loop through each object in expanded_space and check if the from or to coordinate is in it
      # if so, add the expanded_space value to the total_distance

      min_x = min(from_coordinate[0], to_coordinate[0])
      max_x = max(from_coordinate[0], to_coordinate[0])

      min_y = min(from_coordinate[1], to_coordinate[1])
      max_y = max(from_coordinate[1], to_coordinate[1])

      total_distance = get_distance(from_coordinate, to_coordinate)

      filtered_columns = list(filter(lambda i, min_x = min_x, max_x = max_x: i > min_x and i < max_x, expanded_space_columns))
      filtered_rows = list(filter(lambda i, min_y = min_y, max_y = max_y: i > min_y and i < max_y, expanded_space_rows))

      total_distance += (len(filtered_columns) * (expand_by - 1)) + (len(filtered_rows) * (expand_by - 1))

      total_distances += total_distance
  
  print(int(total_distances / 2))


def expand_universe(input_lists: list[list[str]]):
  galaxy_coordinates = list()

  expanded_space_rows = list()
  expanded_space_columns = list()

  columns = [True for _ in range(len(input_lists[0]))]

  y = 0
  x = 0

  for y in range(len(input_lists)):
    row = input_lists[y]

    if '#' not in row:
      expanded_space_rows.append(y)
      continue

    for x in range(len(row)):
      char = row[x]

      if char == '#':
        columns[x] = False

        galaxy_coordinates.append((x, y))

  for i in range(len(columns)):
    if columns[i] == True:
      expanded_space_columns.append(i)
  
  return galaxy_coordinates, expanded_space_rows, expanded_space_columns


def get_distance(from_coordinate: tuple[int, int], to_coordinate: tuple[int, int]):
  return abs(from_coordinate[0] - to_coordinate[0]) + abs(from_coordinate[1] - to_coordinate[1])