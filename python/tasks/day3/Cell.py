from tasks.day3.NumberCoordinates import NumberCoordinates

class Cell:
  is_top_row: bool = False
  is_bottom_row: bool = False
  is_number: bool = False
  is_symbol: bool = False
  row_number: int = 0
  column_number: int = 0
  character: str = ''
  coordinates: NumberCoordinates