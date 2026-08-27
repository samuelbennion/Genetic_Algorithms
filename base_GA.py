# import matplotlib.pyplot as plt
import random

GENOME_LEN = 20     # Length of the bitstring
POPULATION_SIZE = 100  # Number of individuals per generation
GENERATIONS = 50       # Maximum iterations
MUTATION_RATE = 0.05   # Chance for each bit to flip

def create_genome():
    """Generates a random individual."""

    return [random.randint(0,1) for _ in range(GENOME_LEN)]

def fitness(genome):
    """Tests quality of the individual"""
    return sum(genome)
    

def tournament_selection(population, k=10):
    """Selects the best individual out of k randomly chosen members."""
    selected = random.sample(population, k)
    return max(selected, key=fitness)

# Alternatively use roulette wheel selection, use numpy graphs to deem which one is better

# def roulette_wheel_select(population, fitness, r):

#     T = r*sum(fitness(individual) for individual in population)

#     # print(T)
#     selected_indiviual = 0
#     running_total = 0

#     for individual in population:
#         running_total += fitness(individual)
#         if running_total >= T:
#             return individual

def crossover(parent_a, parent_b):
    """Combines two parents at a random split point."""
    split = random.randint(1, GENOME_LEN - 1)
    child_a = parent_a[:split] + parent_b[split:]
    child_b = parent_b[:split] + parent_a[split:]
    return child_a, child_b

def mutate(genome):
    """Randomly changes parameters based on the mutation rate."""

    for i in range(GENOME_LEN):
        if random.random() < MUTATION_RATE:
            genome[i] = random.randint(0,1)  # Randomly changes a single character
    return genome



# TESTING THINGS BELOW

# population = []
# for i in range(10):
#     geno = create_genome()

#     print(geno, fitness(geno))
#     population.append(geno)

# print(tournament_selection(population, k=10))

# genome1 = create_genome()
# print("Original genome", genome1)

# for i in range(10):
#     mutate(genome1)
#     print(genome1)

# genome1 = create_genome()
# genome2 = create_genome()
# print(genome1, genome2)

# print(crossover(genome1, genome2))


best_fitness_plot = []
avg_fitness_plot = []

# We create a population and then evolve it over generations
population = [create_genome() for _ in range(POPULATION_SIZE)]

for generation in range(GENERATIONS):

    population = sorted(population, key=fitness, reverse=True)
    best_genome = population[0]
    best_fitness = fitness(best_genome)

    # Ways to represent population
    # print(f"Generation {generation}: Best Fitness = {best_fitness}/{GENOME_LENGTH*3} -> {best_genome}")
    # for pop in population:
    #     print("".join(pop))
    # strng = "".join(best_genome)
    # print(strng)
    for pop in population:
        print("".join(map(str, pop)))
    print("".join(map(str, best_genome)))

    best_fitness_plot.append(best_fitness)
    avg_fitness_plot.append(sum(fitness(genome) for genome in population) / POPULATION_SIZE)


    
    # Stop early if we found solution already
    if best_fitness == GENOME_LEN:
        print("Best Answer!")
        break
        
    new_generation = [best_genome]  # Elitism: Keep the best individual intact
    
    while len(new_generation) < POPULATION_SIZE:
        # Selection
        parent_a = tournament_selection(population)
        parent_b = tournament_selection(population)
        
        # Crossover
        child_a, child_b = crossover(parent_a, parent_b)
        
        # Mutation
        child_a = mutate(child_a)
        child_b = mutate(child_b)
        
        new_generation.extend([child_a, child_b]) #Extend like append but more efficent
        
    # Truncate population to the correct size and advance generation
    population = new_generation[:POPULATION_SIZE]










# # plt.figure(figsize=(10,6))

# plt.plot(best_fitness_plot, label="Best Fitness", linewidth=2)
# plt.plot(avg_fitness_plot, label="Average Fitness", linestyle="--")

# plt.title("Genetic Algorithm Convergence Over Generations")
# plt.xlabel("Generation")
# plt.ylabel("Fitness")
# plt.legend()
# plt.grid(True)
# plt.show()
