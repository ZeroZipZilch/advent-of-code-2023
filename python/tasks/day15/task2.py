import re
import sys
import itertools
import math
import collections


def run(input: list[str]):
  boxes = [[] for i in range(256)]

  hashes = [row for row in input[0].split(',')]

  for hash in hashes:
    letters, symbol, focal_length, box_number = parse_hash(hash)
    hash_box_index = index(letters, boxes[box_number])

    if symbol == '-' and hash_box_index != -1:
      boxes[box_number] = [hash for hash in boxes[box_number] if not hash.startswith(letters)]
    elif symbol == '=':
      if hash_box_index == -1:
        boxes[box_number].append(hash)
      else:
        boxes[box_number][hash_box_index] = hash


  for i, box in enumerate(boxes):
    if len(box) > 1:
      print(f"Box #{i}:", box)

  print(calculate_focusing_power(boxes))


def parse_hash(hash: str):
  letters, symbol, *focal_length = list(filter(None, re.split(r'(\w+)([-=]+)(\d*)', hash)))
  focal_length = int(focal_length[0]) if focal_length else None

  letter_value = 0
  
  for char in list(letters):
    letter_value += ord(char)
    letter_value *= 17
    letter_value %= 256

  return letters, symbol, focal_length, letter_value


def index(search: str, box: list[str]):
  return next((i for i in enumerate(box) if search in i[1]), [-1,-1])[0]


def calculate_focusing_power(boxes: list[str]):
  total = 0

  for box_index, box in enumerate(boxes):
    box_number = box_index + 1

    for slot_index, hash in enumerate(box):
      slot_number = slot_index + 1

      focal_length = parse_hash(hash)[2]

      total += (box_number * slot_number * focal_length)

  return total