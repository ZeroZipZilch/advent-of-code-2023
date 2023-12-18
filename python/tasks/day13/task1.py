import re
import sys
import itertools
import math
import collections


def run(input_rows: list[str]):
  add = 1

  matching_indexes, patterns = parse_input(input_rows, add)

  horizontal_matching_indexes = []
  horizontal_patterns = []
  vertical_patterns = []
  
  for i, matches in enumerate(matching_indexes):
      if len(matches) > 0 and not set.intersection(*map(set, matches)):
        vertical_patterns.append([''.join(list(row)) for row in zip(*patterns[i])])
      else:
        horizontal_matching_indexes.append(matches)
        horizontal_patterns.append(patterns[i])
        
  vertical_matching_indexes = [parse_input(vertical_patterns[i], add)[0][0] for i in range(len(vertical_patterns))]

  total = calculate_total(vertical_matching_indexes, horizontal_matching_indexes, vertical_patterns, patterns)
  
  print(total)


def parse_input(input_rows: list[str], add: int):
  matching_indexes = []
  pattern_indexes = []

  patterns = []
  pattern = []

  for row in input_rows:
    if ''.join(row).strip() == '':
      matching_indexes.append(pattern_indexes)
      patterns.append(pattern)

      pattern = []
      pattern_indexes = []
    else:
      pattern.append(row)
      pattern_indexes.append(compare_sides(row, add))
  
  matching_indexes.append(pattern_indexes)
  patterns.append(pattern)

  return matching_indexes, patterns


def compare_sides(row, from_index, matching_index: list[int] = None):
  if matching_index is None:
    matching_index = []

  index_to_left, index_to_right = row[:from_index], row[from_index:]

  left = index_to_left
  right = index_to_right
  
  if len(left) < len(right):
    right = right[:from_index]

  elif len(right) < len(left):
    left = left[-len(right):]


  if left == right[::-1]:
    matching_index.append(from_index)

  if from_index < len(row):
    return compare_sides(row, from_index + 1, matching_index)

  return matching_index


def calculate_total(vertical_matches, horizontal_matches, vertical_patterns, horizontal_patterns):
  total = 0
  
  for i, matches in enumerate(vertical_matches):
    intersects = set.intersection(*map(set, matches))
    intersection_value = 0
    
    if len(intersects) > 1:
      print("ERROR: More than 1 intersects found in vertical matches")
    
    if len(intersects) == 0:
      print("ERROR: No intersects found in vertical matches")
      print(matches)

      for pattern in vertical_patterns[i]:
        print(pattern)

    if len(intersects) == 1:
      intersection_value = intersects.pop()
      total += 100 * (intersection_value)

    if intersection_value < 0:
      print("ERROR: Negative intersects found in vertical matches")

  for i, matches in enumerate(horizontal_matches):
    intersects = set.intersection(*map(set, matches))
    intersection_value = 0

    if len(intersects) > 1:
      print("ERROR: More than 1 intersects found in horizontal matches")
      
    if len(intersects) == 0:
      print("ERROR: No intersects found in horizontal matches")

      for pattern in horizontal_patterns[i]:
        print(pattern)

    if len(intersects) == 1:
      intersection_value = intersects.pop()
      total += intersection_value

    if intersection_value < 0:
      print("ERROR: Negative intersects found in horizontal matches")

  return total