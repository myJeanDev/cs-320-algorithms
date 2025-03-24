# Generates a plausible initial population
# Also a variant version that generates a lousy initial population

import random
import math
from util import valid_path, cost
from functools import partial

MIN_INIT_POPULATION = 20
MIN_POPULATION = 6


# This is a guess - there are no good guidelines for initial populations.
def _initial_size(population_size):
    psf = math.factorial(population_size)
    log_psf = int(math.log(psf, 2))
    if (log_psf < MIN_INIT_POPULATION):
        return MIN_INIT_POPULATION
    return int(log_psf)


# We don't actually use distances though might in the future.
def init_pop(list, dist):
    pop_size = len(list)
    if (pop_size < MIN_POPULATION) or (not valid_path(list)):
        return []

    num_initial = _initial_size(pop_size)

    result = []
    while (len(result) < num_initial):
        random.shuffle(list)
        t = tuple(list)
        if (t not in result):
            result += [t]

    return result


# For debugging!
# Invoke by "from init_pop import init_lousy as init_pop"
def init_lousy(list, dist):
    pop_size = len(list)
    if (pop_size < MIN_POPULATION) or (not valid_path(list)):
        return []

    num_initial = _initial_size(pop_size)

    result = []
    while (len(result) < (num_initial * 2)):
        random.shuffle(list)
        t = tuple(list)
        if (t not in result):
            result += [t]

    # functools partial allows us to provide default arguments to cost
    # reverse=True sorts in reverse, so the front of the list is the highest
    # cost
    result = sorted(result, key=partial(cost, distances=dist), reverse=True)

    return result[0:num_initial]
