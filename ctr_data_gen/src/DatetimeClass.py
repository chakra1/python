from enum import Enum
from random import randrange, seed, randint
from datetime import datetime, timedelta

# def generate_random_datetime(start, end):
#     
#     def get_date(x):
#         return start + timedelta(seconds=x)  
#          
#     delta = end - start
#     delta_in_seconds = (delta.days * 24 * 3600) + delta.seconds
#     random_second = randrange(delta_in_seconds)
#     return get_date(random_second)


class DatetimeClass():
    
    class DatetimeFormat(Enum):
        format_1 = '%Y-%m-%d %H:%M:%S'
        format_2 = '%Y-%m-%d'
        format_3 = '%m/%d/%Y %I:%M %p'
        format_4 = '%c'
        format_5 = '%d-%b-%Y %H:%M:%S'
        format_6 = '%d-%b-%Y %H:%M:%S %Z'
        format_7 = '%m/%d/%Y %I:%M %p %Z'
        format_8 = '%Y-%m-%d %H:%M:%S %Z'
        
        @classmethod
        def has_value(cls, value):
            return any(value == item.value for item in cls)
    
    def __init__(self, start, end, format):
        self.start = datetime.strptime(start,format)
        self.end = datetime.strptime(end,format)
        if not self.DatetimeFormat.has_value(format): #error!
            raise ValueError("Invalid format argument!")
    
    def generate_random_datetime(self, x): 
        delta = self.end - self.start
        delta_in_seconds = (delta.days * 24 * 3600) + delta.seconds
        seed(x)
        random_second = randrange(delta_in_seconds)
        return self.start + timedelta(seconds=random_second)
            
    def generate_N_datetimes(self, n):
        i=0
        datetimes = list()
        while (i < n):
            x = randint(0,100)
            datetimes.append(self.generate_random_datetime(x))
            i = i + 1 
        return datetimes

        
