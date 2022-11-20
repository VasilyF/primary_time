"""
Schedule Building Algorithm for PrimaryTime.org

Authors: Ben Hepditch, Steven Squire

Creates the most optimal weekly school schedule 
(ie, that which satisfies the teacher's constraints and has no conflicts )
"""

import pygad as pg
import numpy as np
from server.src.teacher_constraints import Comparator
import teacher_constraints as tc
#where ga standas for genetic algorithm
#see https://pygad.readthedocs.io/en/latest/README_pygad_ReadTheDocs.html for more details

#should be the number of blocks with no conflict * number of teachers in the box
def init_comparators():
    url = "API-ENDPOINT"
    data = tc.transform_requests_data(url)
    return tc.Comparator(data)
    

def fitness_function(solution, solution_index):

    """
    Assess the fitness of the population (set of schedules).
    Compare the schedules of each teacher 
    """
    comparator = init_comparators()

    #solution = schedule
    #first pass: is there more than 1 teacher prepping in any of the time blocks?
    if np.sum(solution) != 90:
        #return 1/sum of all solutions if this is bad
        return 0
    score = 0
    for block_num in range(len(solution)-1):
        #for each block in the schedule
        
        for teacher_id in range(len(block_num)-1):
            score+=1
            #check constraints of the teachers
            if block_num[teacher_id] == 1:
                #teacher is prepping
                comparator.compare_prep_times[teacher_id][0] += 20
                if comparator.compare_prep_times[teacher_id][0] > comparator.compare_prep_times[teacher_id][1]:
                    #too many hours prepping
                    return score
            else:
                #teacher is with class
                comparator.compare_class_times[teacher_id][0] += 20
                if comparator.compare_class_times[teacher_id][0] > comparator.compare_class_times[teacher_id][1]:
                    #too many hours teaching 
                    return score
            
            """At this point we want to check the constraints on days worked"""
            if tc.time_block_mapping[block_num][0:2] not in comparator.compare_days_worked[teacher_id][1]:
                #check if a teacher is working a day they're not supposed to
                return score
        
        score+=5

    return 0


ga_instance = pg.GA(num_generations=10,
                       num_parents_mating=2,
                       sol_per_pop=90,
                       num_genes=20,
                       fitness_func=fitness_function,
                       gene_space=[0, 1])
ga_instance.run()

#print(ga_instance.initial_population)
print(ga_instance.population)
