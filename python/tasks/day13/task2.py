import re
import sys
import itertools
import math
import collections


def run(input_rows: list[str]):
  add = 1

  matching_indexes, patterns = parse_input(input_rows, add)


  vertical_patterns = []
  horizontal_matching_indexes = []
  horizontal_patterns = []
  
  for i, matches in enumerate(matching_indexes):
    if len(matches) > 0 and count_intersections(matches, patterns[i]) == len(patterns[i]) - 1:
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


def count_intersections(match_rows, patterns):
  intersection_dict = dict()

  for i, matches in enumerate(match_rows):
    for match in enumerate(matches):
      for j in match:
        if j not in intersection_dict:
          intersection_dict[j] = 0

        intersection_dict[j] += 1
      
  # Get the key of the highest value in the dict
  intersection_value = 0
  intersection_amount = max(intersection_dict.values())

  if intersection_amount == len(patterns[i]):
    intersection_value = max(intersection_dict, key=intersection_dict.get, default=0)

  return intersection_value


def calculate_total(vertical_matches, horizontal_matches, vertical_patterns, horizontal_patterns):
  total = 0
  
  for i, matches in enumerate(vertical_matches):
    intersection_dict = dict()

    for match in matches:
      for j in match:
        if j not in intersection_dict:
          intersection_dict[j] = 0

        intersection_dict[j] += 1
        
    # Get the key of the highest value in the dict
    intersection_value = 0
    intersection_amount = max(intersection_dict.values())

    if intersection_amount == len(vertical_patterns[i]):
      intersection_value = max(intersection_dict, key=intersection_dict.get, default=0)
    
    # if len(intersects) > 1:
    #   print("ERROR: More than 1 intersects found in vertical matches")
    
    # if len(intersects) == 0:
    #   print("ERROR: No intersects found in vertical matches")
    #   print(matches)

      # for pattern in vertical_patterns[i]:
      #   print(pattern)

    # if len(intersects) == 1:
    #   intersection_value = intersects.pop()
    total += (intersection_value)

    if intersection_value < 0:
      print("ERROR: Negative intersects found in vertical matches")

  for i, matches in enumerate(horizontal_matches):
    # intersects = set.intersection(*map(set, matches))
    # intersection_value = 0

    # if len(intersects) > 1:
    #   print("ERROR: More than 1 intersects found in horizontal matches")
      
    # if len(intersects) == 0:
    #   print("ERROR: No intersects found in horizontal matches")

    #   for pattern in horizontal_patterns[i]:
    #     print(pattern)

    # if len(intersects) == 1:
    #   intersection_value = intersects.pop()
    #   total += intersection_value
    intersection_dict = dict()

    for match in matches:
      for j in match:
        if j not in intersection_dict:
          intersection_dict[j] = 0

        intersection_dict[j] += 1
        
    # Get the key of the highest value in the dict
    intersection_value = 0
    intersection_amount = max(intersection_dict.values())

    if intersection_amount == len(horizontal_patterns[i]):
      intersection_value = max(intersection_dict, key=intersection_dict.get)
    if intersection_value < 0:
      print("ERROR: Negative intersects found in horizontal matches")

    total += 100 * intersection_value

  return total