import re
import math

def run(input_rows: list[str]):
  row_length = len(input_rows[0])

  grid = [[None for i in range(row_length)] for j in range(len(input_rows))]

  symbol_positions = [get_x_y(m.start(), row_length, input_rows) for m in re.finditer(r"[^A-Z\d.]", ''.join(input_rows))]
  number_indexes = []

  for i, row in enumerate(input_rows):
    number_indexes += [get_x_y_span(m.span(), i, input_rows) for m in re.finditer(r"\d+", row)]
  
  for number_index in number_indexes:
      y, start_x, end_x, value = number_index

      for x in range(start_x, end_x + 1):
        grid[y][x] = value

  total = 0
  
  for position in symbol_positions:
    y, x, _, v = position
    nearby_numbers = []

    for y_offset in range(-1, 2):
      last_row_value = None

      for x_offset in range(-1, 2):
        if y_offset == 0 and x_offset == 0:
          last_row_value = None
          continue

        is_edge = (y + y_offset) < 0 or (y + y_offset) >= len(input_rows) or (x + x_offset) < 0 or (x + x_offset) >= row_length
        if is_edge:
          continue

        cell_value = grid[y + y_offset][x + x_offset]
        if cell_value is None:
          last_row_value = None
          continue

        if last_row_value is None:
          last_row_value = int(cell_value)
          nearby_numbers.append(int(cell_value))

    total += sum(nearby_numbers)
      
  print(total)


def get_x_y(index, row_length: int, input_rows: list[str]):
  y = index // row_length
  x = index % row_length

  value = input_rows[y][x]

  return (y, x, x, value)


def get_x_y_span(span: tuple[int, int], row_index: int, input_rows: list[str]):
  start, end = span

  start_x = start
  end_x = (end - 1)
  y = row_index

  value = input_rows[y][start_x:end_x + 1]

  return (y, start_x, end_x, value)


def get_index_value(number_info: tuple[int, int, int], input_rows: list[str]):
  y, start_x, end_x = number_info

  return input_rows[y][start_x:end_x + 1]