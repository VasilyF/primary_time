import requests
class Comparator:
    def __init__(self,data:list) -> None:
        """
        data : [
            prep = {teacher_id : max_prep_time},
            class = {teacher_id : max_class_time},
            minutes = {teacher_id : max_minutes_per_week}
            days = {teacher_id : [days_worked]}   
        ]
        
        """
        self.data=data
        self.prep_times={}
        self.class_times={}
        self.minutes_worked={}
        self.days_worked={}

    def compare_prep_times(self) -> dict:
        """
        Take the user inputted data 
        """
        comparator_dict = {}

        for k,v in self.data[0].items():
            #initialize to 0 since this is the value to be updated 
            comparator_dict[k] = (0, v)

        self.prep_times = comparator_dict

    def compare_class_times(self) -> dict:
        """
        Take the user inputted data 
        """
        comparator_dict = {}

        for k,v in self.data[1].items():
            #initialize to 0 since this is the value to be updated 
            comparator_dict[k] = (0, v)

        self.class_times = comparator_dict

    def compare_minutes_worked(self) -> dict:
        """
        Take the user inputted data 
        """
        comparator_dict = {}

        for k,v in self.data[2].items():
            #initialize to 0 since this is the value to be updated 
            comparator_dict[k] = (0, v)

        self.minutes_worked = comparator_dict

    def compare_days_worked(self) -> dict:
        """
        Take the user inputted data 
        """
        comparator_dict = {}

        for k,v in self.data[3].items():
            #initialize to 0 since this is the value to be updated 
            comparator_dict[k] = (0, v)

        self.days_worked = comparator_dict

class ScheduleData:
    def __init__(self,url:str) -> None:
        self.data = self.transform_requests_data()
        self.url = url
        self.time_blocks = {}
        self.teacher_ids = {}

    def time_block_mapping(self) -> dict:
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

        self.time_blocks = result_dict

    def transform_requests_data(self) -> list:
        """
        Take json data and reformat for schedule_builder

        """
        url = self.url
        dummy_inputs = []
        prep_times = {}
        class_times = {}
        minutes_worked = {}
        days_worked = {}
        result_data = [prep_times,class_times,minutes_worked,days_worked]

        for i in range(len(dummy_inputs)-1):
            total_mins_worked = len(dummy_inputs[3])*420
            result_data[0][i] = dummy_inputs[1] #amount of prep time
            result_data[1][i] = total_mins_worked-dummy_inputs[1] #amount of class time
            result_data[2][i] = total_mins_worked
            result_data[3][i] = dummy_inputs[3] #list of weeks worked

        return result_data

    def store_teacher_id_mappings(self):
        """
        Ensure that the ordering of teacher_constraints/teacher_ids can be reversed
        """
        dummy_teacher_ids = []
        id_mappings = {}
        
        for i in range():

            id_mappings[i] = i
        
        return dummy_teacher_ids



if __name__ == '__main__':
    """d = time_block_mapping()
    for k,v in d.items():
        print(str(k)+ ': ' + str(v))"""
