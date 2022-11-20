import requests

def teacher_data_comparator(teacher_constraints_data: dict) -> dict:
    """
    Take the user inputted data 
    """
    comparator_dict = {}

    for k,v in teacher_constraints_data.items():
        #initialize to 0 since this is the value to be updated 
        comparator_dict[k] = (0, v)
    return comparator_dict

def time_block_mapping() -> dict:
    """
    Generate and return a set of k,v pairs defined as:

        Chromosome_id: int -> day_startTime_endTime: string
    """ 
    result_dict = {}
    #7 hours in a day, 20 minutes per block, excluding 15 mins of recess + 45 of lunch break
    mins_per_day = 360
    blocks_per_day = 18
    block_size = 20
    days = ["Mon","Wed","Tue","Thu","Fri"]
    #TODO:
    #create the dictionary

    return result_dict


if __name__ == '__main__':
    d = time_block_mapping()
    for k,v in d.items():
        print(str(k)+ ': ' + str(v))
