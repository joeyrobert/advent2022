from collections import defaultdict
import copy
import re

with open('input/05.txt') as f:
  lines = f.read()

stacks, inst = lines.split('\n\n')
stack_lines = stacks.split('\n')
inst_lines = inst.split('\n')
stack_dict = defaultdict(list)

for i in range(-2, -1*len(stack_lines) - 1, -1):
  for j in range(len(stack_lines[i]) // 4 + 1):
    item = stack_lines[i][j*4:j*4 + 4]

    if item[1] != ' ':
      stack_dict[j + 1].append(item[1])

stack_dict_2 = copy.deepcopy(stack_dict)

for line in inst_lines:
  matches = re.findall('move (\\d+) from (\\d+) to (\\d+)', line)
  quantity, start, end = list(map(int, matches[0]))

  # Part 1
  for i in range(quantity):
    stack_dict[end].append(stack_dict[start].pop())

  # Part 2
  tmp = []
  for i in range(quantity): # 3
    stack_dict_2[end].append(stack_dict_2[start][-quantity + i])

  for i in range(quantity):
    stack_dict_2[start].pop()

def get_top(stack_dict):
  msg = []
  for key in sorted(stack_dict.keys()):
    msg.append(stack_dict[key][-1])
  return ''.join(msg)

print('Part 1:', get_top(stack_dict))
print('Part 2:', get_top(stack_dict_2))