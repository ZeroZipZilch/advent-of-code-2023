import re

def run(input_rows):
  total = 0

  for row in input_rows:
    row_numbers = re.sub(r'\D', '', row)
    first_and_last_digit_of_row = int(row_numbers[0] + row_numbers[-1])

    total += first_and_last_digit_of_row
  
  print(total)

