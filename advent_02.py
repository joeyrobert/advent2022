with open('input/02.txt') as f:
	data = f.read()

# A = opponent rock
# B = opponent paper
# C = opponent scissors

# X = my rock
# Y = my paper
# Z = my scissors

player_scores = {
	'X': 1,
	'Y': 2,
	'Z': 3,
	'A': 1,
	'B': 2,
	'C': 3,
}

outcome_scores = {
	'win': 6,
	'draw': 3,
	'loss': 0,
	'X': 0,
	'Y': 3,
	'Z': 6,
}

# First question
winners = {
	'X': 'C',
	'Y': 'A',
	'Z': 'B',
}

draws = {
	'X': 'A',
	'Y': 'B',
	'Z': 'C',
}

strat = data.split('\n')
points_one = 0
for row in strat:
	opp, you = row.split(' ')

	if winners[you] == opp:
		outcome = 'win'
	elif draws[you] == opp:
		outcome = 'draw'
	else:
		outcome = 'loss'

	score = player_scores[you] +  outcome_scores[outcome]
	points_one += score

print(points_one)

# Second question
winners = {
	'A': 'B',
	'B': 'C',
	'C': 'A',
}
losers = {v: k for k, v in winners.items()}
points_two = 0
for row in strat:
	opp, outcome = row.split(' ')

	if outcome == 'X':
		# Lose
		you = losers[opp]
	elif outcome == 'Y':
		# Draw	
		you = opp
	else:
		# Win
		you = winners[opp]

	score = player_scores[you] +  outcome_scores[outcome]
	points_two += score

print(points_two)