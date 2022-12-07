with open('input/01.txt') as f:
	data = f.read()
elves = [item.split('\n') for item in data.split('\n\n')]
elves_sum = [sum(int(x) for x in elf) for elf in elves]
print(max(elves_sum))
print(sum(sorted(elves_sum, reverse=True)[:3]))