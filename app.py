from deap import base, creator, tools, algorithms
import random
import csv
import numpy
from Knapsack import Knapsack

#==========================[ Variables ]==========================#

items = []
# Get list of items from .csv file
with open('items.csv') as file:
    reader = csv.reader(file)
    for row in reader:
        # name, weight(kg), value
        items.append((row[0], float(row[1]), int(row[2])))

MAX_CAPACITY = 3  # in kg
knapsack = Knapsack(MAX_CAPACITY, items)

ITEMS_LENGTH = len(knapsack)    # Number of chromosomes
POPULATION_SIZE = 200
CROSSOVER_P = 0.9
MUTATION_P = 0.1
GEN_AMOUNT = 10
HALL_OF_FAME_SIZE = 10

BEST_RESULT = [1, 1, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 1, 1, 1]

#============================[ Setup ]============================#

toolbox = base.Toolbox()

toolbox.register('zeroOrOne', random.randint, 0, 1)
creator.create('FitnessMax', base.Fitness, weights=(1.0,)) # 1.0 means maximizing
creator.create('Individual', list, fitness=creator.FitnessMax)
toolbox.register('individualCreator', tools.initRepeat, creator.Individual, toolbox.zeroOrOne, ITEMS_LENGTH)
toolbox.register('populationCreator', tools.initRepeat, list, toolbox.individualCreator)

# Fitness
def evaluate(individual):
    return knapsack.get_total_value(individual),  # return a tuple

# Register the countOnes function
toolbox.register('evaluate', evaluate)

# Genetic operators
toolbox.register('select', tools.selTournament, tournsize=3)
toolbox.register('mate', tools.cxOnePoint)
toolbox.register('mutate', tools.mutFlipBit, indpb=1.0/ITEMS_LENGTH)

hall_of_fame = tools.HallOfFame(HALL_OF_FAME_SIZE)

stats = tools.Statistics(lambda ind: ind.fitness.values)

# Register the statistics object
stats.register('max', numpy.max)
stats.register('avg', numpy.mean)
stats.register("min", numpy.min)
stats.register("max", numpy.max)

#==========================[ Algorithm ]==========================#

population = algorithms.eaSimple(
    toolbox.populationCreator(n=POPULATION_SIZE),
    toolbox,
    cxpb=CROSSOVER_P,
    mutpb=MUTATION_P,
    ngen=GEN_AMOUNT,
    stats=stats,
    halloffame=hall_of_fame,
    verbose=True)

#===========================[ Results ]===========================#

print("\n============================[RESULT]===============================")
knapsack.print_items(hall_of_fame.items[0])
print(hall_of_fame.items[0])

print("\n=========================[BEST RESULT]=============================")
knapsack.print_items(BEST_RESULT)
print(BEST_RESULT)