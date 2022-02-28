import random
random.seed()

popSize = 1000
chromosomeLength = 1000

def generateChromosome():
	return [random.randint(0, 1) for x in range(chromosomeLength)]

def generatePopulation():
	return [generateChromosome() for x in range(popSize)]

population = generatePopulation()

tournamentSize = 4
noOfTournaments = 20

def getFitness(c):
	fitness = chromosomeLength
	for a in c:
		if a == 1:
			fitness -= 1
	return fitness

def getFittest(cs):
	bestFitness = chromosomeLength
	fittest = []
	for c in cs:
		fitness = getFitness(c)
		if fitness < bestFitness:
			bestFitness = fitness
			fittest = c
	return fittest

def randomSelection(list, count):
	upper = len(list) - 1
	selection = []
	selected = []
	for i in range(count):
		index = random.randint(0, upper)
		while index in selected:
			index = random.randint(0, upper)
		selection.append(list[index])
		selected.append(index)
	return selection

def getParents(pop):
	parents = []
	for i in range(noOfTournaments):
		parent = getFittest(randomSelection(pop, tournamentSize))
		pop.remove(parent)
		parents.append(parent)
	return parents

mutationRate = 0.3
alleleMutateRate = 1 / chromosomeLength

def mutate(c):
	for i, a in enumerate(c):
		if random.random() <= alleleMutateRate:
			if a == 0:
				c[i] = 1
			else:
				c[i] = 0

def crossover(p1, p2):
	child = []
	for i in range(chromosomeLength):
		p1i = p1[i]
		if p1i == p2[i]:
			child.append(p1i)
		else:
			child.append(random.randint(0, 1))
	if random.random() <= mutationRate:
		mutate(child)
	return child

def generateOffspring(parents):
	offspring = []
	upper = len(parents) - 1
	for i in range(popSize - len(parents)):
		rand1 = random.randint(0, upper)
		rand2 = random.randint(0, upper)
		while rand1 == rand2:
			rand2 = random.randint(0, upper)
		p1 = parents[rand1]
		p2 = parents[rand2]
		offspring.append(crossover(p1, p2))
	return offspring

def simulateGeneration():
	global population
	parents = getParents(population)
	offspring = generateOffspring(parents)
	population = parents
	population.extend(offspring)

def getAvgFitness(pop):
	total = 0
	for c in pop:
		total += getFitness(c)
	return total / popSize

averageFitness = chromosomeLength
cycle = 0
while averageFitness != 0.0:
	simulateGeneration()
	averageFitness = getAvgFitness(population)
	print("Cycle", cycle, ": " + str(averageFitness), end='\r')
	cycle += 1
print("Optimum fitness reached in", cycle - 1, "cycles")