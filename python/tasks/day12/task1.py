import re
import sys
import itertools
import math
import collections
import pathlib
from json import dumps as json_dumps

def run(input_rows: list[str]):
  row_patterns = []
  pattern_instructions = []
  total = 0

  for row in input_rows:
    pattern, instructions = row.split()

    patterns = parse_row_patterns(pattern, 0, [])

    
    pattern_values = [compare_pattern_instructions(pattern, instructions) for pattern in patterns]
    pattern_instructions.append({ "value": sum(pattern_values), "original_pattern": pattern, "patterns": patterns, "instructions": instructions })
    total += sum(pattern_values)
  
  pathlib.Path('python/tasks/day12/output').write_text(json_dumps(pattern_instructions, indent=2))
  print(total)


def parse_row_patterns(row: str, i, patterns):
  if i == len(row):
    patterns.append(row)
    return patterns
  
  if row[i] == '?':
    patterns = parse_row_patterns(row[:i] + '#' + row[i + 1:], i + 1, patterns)
    patterns = parse_row_patterns(row[:i] + '.' + row[i + 1:], i + 1, patterns)
  else:
    patterns = parse_row_patterns(row, i + 1, patterns)

  return patterns


def compare_pattern_instructions(pattern: str, instructions: str):
  split_instructions = list(map(int, instructions.split(',')))
  split_pattern = list(map(len, filter(None, pattern.split('.'))))

  if len(split_instructions) != len(split_pattern):
    return 0
  
  for i in range(len(split_instructions) - 1, -1, -1):
    if split_instructions[i] == split_pattern[i]:
      del split_pattern[i]
      del split_instructions[i]

  if len(split_pattern) == 0 and len(split_instructions) == 0:
    return 1
  
  return 0