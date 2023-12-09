import re

def run(input_rows: list[str]):
  history_book = dict()
  total_values = 0

  for history_page in input_rows:
    history_values = list(map(int, history_page.split(' ')))
    history_book[history_page] = list()
    
    history_book[history_page].append(list(history_values))

    while min(history_values) != max(history_values):
      current_history_values = []

      for (i, value) in enumerate(history_values):
        if i + 1 < len(history_values):
          current_history_values.append(history_values[i + 1] - value)
      
      history_book[history_page].append(current_history_values)
      history_values = current_history_values

    next_value = 0

    for i in range(len(history_book[history_page]) - 1, -1, -1):
      history_page_values = history_book[history_page][i]
      next_history_page_values = history_book[history_page][i - 1] if i - 1 >= 0 else [0]

      next_value = next_history_page_values[0] - history_page_values[0]

      print(f"{i}: {next_value} - {history_page_values}")
      next_history_page_values.insert(0, next_value)
    
    total_values += history_page_values[0]

  print(total_values)