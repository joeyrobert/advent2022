with open('input/04.txt') as f:
  sections = f.read().split('\n')

def get_pair(a):
  start, end = a.split('-')
  return [int(start), int(end)]

total_1 = 0
total_2 = 0
for section in sections:
  a, b = section.split(',')

  a = get_pair(a)
  b = get_pair(b)

  if (a[0] <= b[0] and a[1] >= b[1]) or (b[0] <= a[0] and b[1] >= a[1]):
    total_1 += 1

  set_a = set(list(range(a[0], a[1] + 1)))
  set_b = set(list(range(b[0], b[1] + 1)))
  print(a, b)
  print(set_a, set_b)
  if set_a.intersection(set_b):
    total_2 += 1

print('Part 1:', total_1)
print('Part 2:', total_2)