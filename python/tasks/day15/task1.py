import re
import sys
import itertools
import math
import collections


def run(input: list[str]):
  totals = 0

  hashes = [[ord(char) for char in list(row)] for row in input[0].split(',')]

  for hash in hashes:
    total = 0

    for char in hash:
      total += char
      total *= 17
      total %= 256
    
    totals += total

  print(totals)