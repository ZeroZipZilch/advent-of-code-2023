import re
from tasks.day3.NumberCoordinates import NumberCoordinates

from tasks.day3.Cell import Cell

def run(input_rows: list[str]):
  grid = list()

  for (row_number, row) in enumerate(input_rows):
    (numbers, cells) = parse_grid(row_number, input_rows.__len__, row)

    grid.append(cells)

    for number in numbers:
      print(number.row_number, number.start_x, number.end_x, number.value)

    for cell in cells:
      if check_adjencent_for_symbols(grid, cell):
        print(cell.coordinates.value)


def check_adjencent_for_symbols(grid, cell):
  pass

def parse_grid(row_number, max_rows, row):
  row_numbers = []
  number_sequence = ''
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

    if character == '.':
      assign_coordinates_to_adjecent_number_cells(number_sequence, row_number, column_number, row_cells, row_numbers)

      number_sequence = ''
    else:
      number_sequence = number_sequence + character

      if re.match('[\d]', character):
        cell.is_number = True
      elif re.match('[\W]', character):
        cell.is_symbol = True

    row_cells.append(cell)
  
  return row_numbers, row_cells

def assign_coordinates_to_adjecent_number_cells(number_sequence, row_number, column_number, row_cells: list[Cell], row_numbers: list[NumberCoordinates]):
  if number_sequence == '':
    return
  
  number_coordinates = NumberCoordinates()

  number_coordinates.value = int(number_sequence)
  number_coordinates.row_number = row_number
  number_coordinates.start_x = column_number - len(number_sequence)
  number_coordinates.end_x = column_number - 1

  row_numbers.append(number_coordinates)

  for i in range(1, len(number_sequence)):
    row_cells[column_number - i].coordinates.start_x = column_number - len(number_sequence)
    row_cells[column_number - i].coordinates.end_x = column_number - 1
    row_cells[column_number - i].coordinates.value = number_sequence