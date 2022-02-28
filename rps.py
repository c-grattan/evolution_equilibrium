import random
random.seed()

#For simplicity's sake, 0=rock, 1=paper, 2=scissors

def generatePop(size):
	return [random.randint(0, 2) for x in range(0, size)]

def getFitnessAgainst(c, p):
	fitness = 0
	for ec in p:
		if ec != c + 1 % 3:
			fitness += 1
	return fitness