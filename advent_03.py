from collections import defaultdict

def get_common_item(rucksack):
    first = rucksack[:len(rucksack) // 2]
    second = rucksack[len(rucksack) // 2:]
    return list(set(first).intersection(second))

def get_priority(item):
  priority = 0
  if item.isupper():
    priority += 26
  priority += ord(item.lower()) - ord('a') + 1
  return priority

with open('input/03.txt') as f:
  rucksacks = f.read().split('\n')

total = 0
for rucksack in rucksacks:
  item_set = get_common_item(rucksack)
  total += get_priority(item_set[0])

print('Part 1:', total)

groups = defaultdict(list)
for i, rucksack in enumerate(rucksacks):
  group = i // 3
  groups[group].append(rucksack)

total = 0
for groupsacks in groups.values():
  common = list(set(groupsacks[0]).intersection(groupsacks[1]).intersection(groupsacks[2]))
  total += get_priority(common[0])

print('Part 2:', total)