from util import *
import random
import copy
# Genetic Traveling Salesperson Problem 
# util.py
# cost(path, distances):
#   gives the cost of a path.
# valid_path(path):
#   Confirms that the path is a valid Hamiltonian circuit
# best_path(list_of_paths, distances):
#   Finds and returns the path with the lowest cost from a given list of paths. 


def ga_tsp(initial_population: list[tuple], distances: dict[int], generations: int):
    # input validation
    if initial_population is None or distances is None or generations is None:
        return None
    elif generations <= 0:
        return None
    
    # initial_population: list of paths
    # distances: dict of single edge distances between every city.
    # generations: number of generations
    best_cost_ever = float('inf')
    best_path_ever = best_path(initial_population, distances)

    # We will be using cost() to get the fitness score
    current_path_population = initial_population
    for gen in range(generations):
        population_by_fitness = {}

        # Calculating the costs for every path, aka calculating fitness
        for path in current_path_population:
            population_by_fitness[get_path_string(path)] = cost(path, distances)
        
        parent_pool = create_parent_pool(population_by_fitness)
        current_path_population = create_children_pool(len(current_path_population), parent_pool)

        current_generations_best = best_path(current_path_population, distances)
        if cost(current_generations_best, distances) < best_cost_ever:
            best_path_ever = current_generations_best  
    return best_path_ever


def get_path_string(path: tuple) -> str:
    result = ""
    for each in path:
        result += str(each)
    return result


def get_string_path(name: str) -> tuple:
    result = []
    for each in name:
        result.append(each)
    return tuple(result)


def create_parent_pool(population_by_fitness) -> list[tuple]:
    number_of_parents = len(population_by_fitness) * 2
    paths = list(population_by_fitness.keys())
    weights = list(population_by_fitness.values())
    parents = random.choices(paths, weights=weights, k=number_of_parents)
    for i, each in enumerate(parents):
        parents[i] = get_string_path(each)
    return parents


def create_children_pool(children_amount, parent_pool) -> list[tuple]:
    children_pool = []
    count = 0
    while len(children_pool) != children_amount:
        parent_one = parent_pool[count]
        count += 1
        if count >= len(parent_pool):
            count = 0
        parent_two = parent_pool[count]
        count += 1
        if count >= len(parent_pool):
            count = 0
        new_path = cross_over_paths(parent_one, parent_two)

        if valid_path(new_path):
            children_pool.append(new_path)
        else:
            mutated_path = mutate_path(new_path)
            if valid_path(mutated_path):
                children_pool.append(mutated_path)
            else:
                children_pool.append(random.choice(parent_pool))
    
    return children_pool


def cross_over_paths(parent_a: tuple, parent_b: tuple) -> tuple:
    # using a random ordered section from the first parent, this ensures a valid path
    # the second parent can add anything that isn't in the list already
    size = len(parent_a)
    child = [None] * size
    indices = random.sample(range(size), 2)
    start, end = sorted(indices)
    child[start:end] = parent_a[start:end]

    parent2_index = end
    child_index = end
    while None in child:
        city = parent_b[parent2_index % size]
        if city not in child:
            child[child_index % size] = city
            child_index += 1
        parent2_index += 1
    return tuple(child)


def mutate_path(path: tuple) -> tuple:
    path_list = list(path)
    random.shuffle(path_list)
    return tuple(path_list)
