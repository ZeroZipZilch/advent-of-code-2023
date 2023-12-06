import importlib
import os
import sys

def main():
  day_number = sys.argv[1]
  task_number = sys.argv[2]
  input_user = sys.argv[3]
  
  input_file = 'tasks/day{day_number}/{input_user}-aoc-input.txt'.format(day_number=day_number, input_user=input_user)
  input_file = os.path.join(os.path.dirname(__file__), input_file)

  with open(input_file) as f:
    input_rows = [line.strip() for line in f.readlines()]
  
  task = importlib.import_module('tasks.day{day_number}.task{task_number}'.format(day_number=day_number, task_number=task_number)).run

  task(input_rows)

if __name__ == '__main__':
  main()