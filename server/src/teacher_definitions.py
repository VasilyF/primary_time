"""
Teacher Objects
"""
class Teacher:

    def __init__(self,teacher_id) -> None:
        self.teacher_id = teacher_id
        self.prep_schedule = {
            "mon" : [],
            "tue" : [],
            "wed" : [],
            "thu" : [],
            "fri" : [],
        }
        self.class_schedule = {
            "mon" : [],
            "tue" : [],
            "wed" : [],
            "thu" : [],
            "fri" : [],
        }

    def add_prep_block(self,block_id):
        #where block id has format: day_startTime_endTime
        block_info = block_id.split("_")
        block_day, block_start, block_end = block_info
        self.prep_schedule[self.prep_schedule.index(block_day)].append([block_start, block_end])

    def add_class_block(self,block_id):
        #where block id has format: day_startTime_endTime
        block_info = block_id.split("_")
        block_day, block_start, block_end = block_info
        self.prep_schedule[self.class_schedule.index(block_day)].append([block_start, block_end])

    