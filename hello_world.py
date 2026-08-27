# Make genetic algorithm hello world!!!

#Turn string maximisation into hello world string bit!!!
# hello world

import random

# --- 1. PARAMETERS ---
GENOME_LENGTH = 11     # Length of the bitstring
POPULATION_SIZE = 300  # Number of individuals per generation
GENERATIONS = 50       # Maximum iterations
MUTATION_RATE = 0.1   # Chance for each bit to flip
ALPHABET = "abcdefghijklmnopqrstuvwxyz "

# --- 2. CORE FUNCTIONS ---

def create_genome():
    """Generates a random individual."""
    """In this instance, generates a random word"""
    return [random.choice(ALPHABET) for _ in range(GENOME_LENGTH)]
    # This randomly picks something from alphabet list

def fitness(genome):
    """Evaluates quality. Higher sum means closer to optimal."""
    """Scores based on how many words are correct"""
    solution = "hello world"
    score = 0
    num_chars = len(ALPHABET)
    # Go for gradients rather than large flat planes!!!
    # Big jumps are bad, smoothness is best
    # Smooth gradient here
    for i in range(len(genome)):
        score += 1 - abs(ord(genome[i])-ord(solution[i]))/num_chars
        # if str(genome[i]) == str(solution[i]):
        #     score += 1
        
    # We prefer exact matches so reward it more strongly
        if str(genome[i]) == str(solution[i]):
            score += 2

    return score

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
    split = random.randint(1, GENOME_LENGTH - 1)
    child_a = parent_a[:split] + parent_b[split:]
    child_b = parent_b[:split] + parent_a[split:]
    return child_a, child_b

def mutate(genome):
    """Randomly changes parameters based on the mutation rate."""

    for i in range(GENOME_LENGTH):
        if random.random() < MUTATION_RATE:
            genome[i] = random.choice(ALPHABET)  # Randomly changes a single character
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


# --- 3. THE EVOLUTIONARY LOOP ---


# --- Tracking stats ---
best_fitness_history = []
avg_fitness_history = []
worst_fitness_history = []


# Step 1: Initialize the population
population = [create_genome() for _ in range(POPULATION_SIZE)]

for generation in range(GENERATIONS):
    # Step 2: Sort the population by fitness (highest first)
    population = sorted(population, key=fitness, reverse=True)
    best_genome = population[0]
    best_fitness = fitness(best_genome)

    # Ways to represent population
    print(f"Generation {generation}: Best Fitness = {best_fitness}/{GENOME_LENGTH*3} -> {best_genome}")
    # for pop in population:
    #     print("".join(pop))
    # strng = "".join(best_genome)
    # print(strng)


    best_fitness_history.append(best_fitness)
    avg_fitness_history.append(sum(fitness(ind) for ind in population) / POPULATION_SIZE)
    worst_fitness_history.append(fitness(population[-1]))


    
    # Check for early termination if optimal solution is found
    if best_fitness == GENOME_LENGTH*3:
        print("Optimal solution reached!")
        break
        
    # Step 3: Breed a new generation
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










import matplotlib.pyplot as plt

plt.figure(figsize=(10,6))

plt.plot(best_fitness_history, label="Best Fitness", linewidth=2)
plt.plot(avg_fitness_history, label="Average Fitness", linestyle="--")
plt.plot(worst_fitness_history, label="Worst Fitness", linestyle=":")

plt.title("Genetic Algorithm Convergence Over Generations")
plt.xlabel("Generation")
plt.ylabel("Fitness")
plt.legend()
plt.grid(True)
plt.show()
