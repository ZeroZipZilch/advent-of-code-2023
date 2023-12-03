import re

def run(input_rows):
  total = 0

  for row in input_rows:
    row_numbers = find_all_worded_numbers(row)
    row_numbers = re.sub(r'\D', '', row_numbers)

    first_and_last_digit_of_row = int(row_numbers[0] + row_numbers[-1])
    print(first_and_last_digit_of_row)

    total += first_and_last_digit_of_row
  
  print(total)

def find_all_worded_numbers(row: str):
  numbers_as_words = {
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8, 
    'nine': 9
  }

  print('row before change:', row)

  worded_numbers = []
  for word in numbers_as_words:
    if word in row:
        for index in re.finditer(word, row):
          worded_numbers.append(dict(word=word, index=index.start()))
  
  worded_numbers.sort(key=lambda x: x['index'])
  
  for word in worded_numbers:
    if word['word'] in row:
      row = f"{row[:word['index']]}{numbers_as_words[word['word']]}{row[word['index'] + 1:]}"

  print(worded_numbers)
  print (row)

  return row