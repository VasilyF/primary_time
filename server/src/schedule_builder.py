"""
Schedule Building Algorithm for PrimaryTime.org

Authors: Ben Hepditch, Steven Squire

Creates the most optimal weekly school schedule 
(ie, that which satisfies the teacher's constraints and has no conflicts )
"""

import pygad as pg
import numpy as np
import teacher_constraints as tc
import teacher_definitions as td
#where ga standas for genetic algorithm
#see https://pygad.readthedocs.io/en/latest/README_pygad_ReadTheDocs.html for more details

#should be the number of blocks with no conflict * number of teachers in the box
def init_comparators():
    url = "API-ENDPOINT"
    
    return tc.Comparator(url)
    
def init_data():
    url = "API-ENDPOINT"
    return tc.ScheduleData(url)

def fitness_function(solution, solution_index):

    """
    Assigns a score to each proposed schedule. Highest score = total blocks * number of teachers

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
        
        score+=1

    return 0

def main():
    
    ga_instance = pg.GA(num_generations=10,
                        num_parents_mating=2,
                        sol_per_pop=90,
                        num_genes=20,
                        fitness_func=fitness_function,
                        gene_space=[0, 1],
                        save_solutions = True
                        )
    return ga_instance

def output_best_schedule(schedule):
    """
    Translate the binary lists back into blocks for json format
    """
    schedule_data = init_data()
    prescribed_schedule = {}
    teacher_schedules = [td.Teacher(schedule_data.teacher_ids(i)) for i in range(len(schedule)-1)]
        
    for block_num in range(len(schedule)-1):
        #use saved teacher id and block time mappings 
        for teacher_id in range(len(schedule[block_num])-1):
            if schedule[block_num][teacher_id] == 1: 
                #if prep block
                teacher_schedules[teacher_id].add_prep_block(schedule_data.time_blocks)
            else:
                teacher_schedules[teacher_id].add_class_block(schedule_data.time_blocks)

    return prescribed_schedule
if __name__ == '__main__':
    
    schedule_builder = main()
    schedule_builder.run()
    #print(ga_instance.initial_population)
    print(schedule_builder.population)
    schedule_builder.plot_fitness()
