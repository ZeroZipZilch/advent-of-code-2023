import re
from tasks.day3.NumberCoordinates import NumberCoordinates

from tasks.day3.Cell import Cell

def run(input_rows: list[str]):
  grid = list()

  row_numbers: list[NumberCoordinates] = []
  row_symbols: list[NumberCoordinates] = []
  adjecent_numbers: list[NumberCoordinates] = []

  for (row_number, row) in enumerate(input_rows):
    cells = parse_grid(row_number, input_rows.__len__, row, row_numbers, row_symbols)

    grid.append(cells)

    for symbol in row_symbols:
      check_adjencent_for_numbers(symbol, row_numbers, adjecent_numbers)
    
  total = 0

  for adjecent_number in adjecent_numbers:
    total = total + adjecent_number.value
    # print(adjecent_number.row_number, adjecent_number.start_x, adjecent_number.end_x, adjecent_number.value)
  
  print("total", total)
  # for number in row_numbers:
  #     print(number.row_number, number.start_x, number.end_x, number.value)
    
  # for symbol in row_symbols:
  #   print(symbol.row_number, symbol.start_x, symbol.end_x, symbol.value)

  print("done")


def check_adjencent_for_numbers(symbol: NumberCoordinates, numbers: list[NumberCoordinates], adjecent_numbers: list[NumberCoordinates]):
    for number in numbers:
      adjecent_start = number.start_x - 1
      adjecent_end = number.end_x + 1

      adjecent_horizontal = symbol.start_x >= adjecent_start and symbol.end_x <= adjecent_end
      adjecent_vertical = symbol.row_number >= number.row_number - 1 and symbol.row_number <= number.row_number + 1

      if adjecent_horizontal and adjecent_vertical:
        adjecent_number = NumberCoordinates()

        adjecent_number.value = number.value
        adjecent_number.start_x = number.start_x
        adjecent_number.end_x = number.end_x
        adjecent_number.row_number = number.row_number

        if not object_exists_in_list(adjecent_number, adjecent_numbers):
          adjecent_numbers.append(adjecent_number)
          return True


def parse_grid(row_number, max_rows, row, row_numbers: list[NumberCoordinates], row_symbols: list[NumberCoordinates]):
  current_sequence = ''
  row_cells = list()

  character: str

  for (column_number, character) in enumerate(row):
    cell: Cell = Cell()

    cell.row_number: int = row_number
    cell.coordinates = NumberCoordinates()

    if row_number == 0:
      cell.is_top_row = True

    if row_number == max_rows:
      cell.is_bottom_row = True

    cell.column_number = column_number
    cell.character = character

    if character == '.' or re.match('[\W]', character) or (re.match('[\d]', character) and re.match('[\W]', current_sequence)):
      assign_coordinates_to_adjecent_number_cells(current_sequence, row_number, column_number, row_cells, row_numbers, row_symbols)

      if character != '.':
        current_sequence = character
      else:
        current_sequence = ''
    else:
      current_sequence = current_sequence + character

      if re.match('[\d]', current_sequence) and column_number == len(row) - 1:
        assign_coordinates_to_adjecent_number_cells(current_sequence, row_number, column_number, row_cells, row_numbers, row_symbols)
        current_sequence = ''

      if re.match('[\d]', character):
        cell.is_number = True
      elif re.match('[\W]', character):
        cell.is_symbol = True

    row_cells.append(cell)
  
  return row_cells

def assign_coordinates_to_adjecent_number_cells(current_sequence, row_number, column_number, row_cells: list[Cell], row_numbers: list[NumberCoordinates], row_symbols: list[NumberCoordinates]):
  if current_sequence == '':
    return
  
  if re.match('[\d]', current_sequence):
    number_coordinates = NumberCoordinates()

    number_coordinates.value = int(current_sequence)
    number_coordinates.row_number = row_number
    number_coordinates.start_x = column_number - len(current_sequence)
    number_coordinates.end_x = column_number - 1

    row_numbers.append(number_coordinates)
  elif re.match('[\W]', current_sequence):
    symbol_coordinates = NumberCoordinates()

    symbol_coordinates.value = current_sequence
    symbol_coordinates.row_number = row_number
    symbol_coordinates.start_x = column_number - len(current_sequence)
    symbol_coordinates.end_x = column_number - 1

    # If row_symbols doesn't contain symbol_coordinates, add it
    if not object_exists_in_list(symbol_coordinates, row_symbols):
      row_symbols.append(symbol_coordinates)

  for i in range(1, len(current_sequence)):
    row_cells[column_number - i].coordinates.start_x = column_number - len(current_sequence)
    row_cells[column_number - i].coordinates.end_x = column_number - 1
    row_cells[column_number - i].coordinates.value = current_sequence

def object_exists_in_list(object, list):
  for item in list:
    if object.end_x == item.end_x and object.start_x == item.start_x and object.row_number == item.row_number and object.value == item.value:
      return True
  
  return False