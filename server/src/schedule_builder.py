"""
Schedule Building Algorithm for PrimaryTime.org

Authors: Ben Hepditch, Steven Squire

Creates the most optimal weekly school schedule 
(ie, that which satisfies the teacher's constraints and has no conflicts )
"""

import pygad as pg
import numpy as np
from teacher_constraints import teacher_data_comparator as comparator
#where ga standas for genetic algorithm
#see https://pygad.readthedocs.io/en/latest/README_pygad_ReadTheDocs.html for more details
empty_comparator = comparator
#should be the number of blocks with no conflict * number of teachers in the box
solution =  20*10

def fitness_function(solution: int, schedule_list: list) -> int:

    """
    Assess the fitness of the population (set of schedules).
    Compare the schedules of each teacher 
    """
    new_comparator = empty_comparator

    for schedule in schedule_list:
        #each schedule 'chromosome' corresponds to a labeled timeslot
        for i in range(20):
            #where i is the 'teacher id' 
            #20 is just a palceholder for the number of teachers 
            print(i)
            

    return 0


ga_instance = pg.GA(num_generations=10,
                       num_parents_mating=2,
                       sol_per_pop=3,
                       num_genes=4,
                       fitness_func=fitness_function,
                       gene_space=[0, 1])
ga_instance.run()

print(ga_instance.initial_population)
print(ga_instance.population)
