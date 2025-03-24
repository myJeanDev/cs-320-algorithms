# Program to run ga_tsp with various inputs

import sys
from util import cost, best_path
# from init_pop import init_lousy as init_pop
from init_pop import init_pop
from load_dist import load_dist
from main import ga_tsp


GENERATIONS = 500


if (len(sys.argv) < 2):
    print("missing filename argument")
    sys.exit(1)


cities, distances = load_dist(sys.argv[1])
print(f"cities={cities}")
# print(f"distances = {distances}")
if (distances is None) or (cities is None):
    sys.exit(1)  # load_dist should have printed a message

initial_population = init_pop(cities, distances)
if (len(initial_population) == 0):
    print("population did not initialize")
    sys.exit(1)

path = best_path(initial_population, distances)

print(f"initial population size is {len(initial_population)}")
print(f"start: best path={path} with cost={cost(path,distances)}")

path = ga_tsp(initial_population, distances, GENERATIONS)

print(f"end:   best path={path} with cost={cost(path,distances)}")
