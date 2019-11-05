class Time:
    '''
    Represents the time of day.

    attributes: hour, minute, second
    '''
    def __init__(self, hour=0, minute=0, second=0): # set default value if not defined
        self.hour = hour
        self.minute = minute
        self.second = second

    def __str__(self): # a way to print
        '''return a Time oject in a human-readable format
        text representation of this object'''
        return f'I like it this way: {self.hour:02d}:{self.minute:02d}:{self.second:02d}'

    def __add__(self, other):
        '''
        make "+" operator works to add time
        '''
        seconds = self.time_to_int() + other.time_to_int()
        return int_to_time(seconds)

    def print_time(self):
        print(f'I like it this way: {self.hour:02d}:{self.minute:02d}:{self.second:02d}')

    def time_to_int(self):  
        '''
        Computes the number of seconds since midnight.
        time: Time object.
        '''
        minutes = self.hour * 60 + self.minute
        seconds = minutes * 60 + self.second
        return seconds

    def is_after(self, other):
        return self.time_to_int() > other.time_to_int()

    def increment(self, seconds):
        """return a Time object after incrementing"""
        result = Time()
        result.hour = self.hour
        result.minute = self.minute
        result.second = self.second
        
        result.second += seconds

        if result.second >= 60:
            result.second -= 60
            result.minute += 1

        if result.minute >= 60:
            result.minute -= 60
            result.hour += 1

        return result


def int_to_time(seconds):
    """Makes a new Time object.

    seconds: int seconds since midnight.
    """
    time = Time()
    minutes, time.second = divmod(seconds, 60)
    time.hour, time.minute = divmod(minutes, 60)
    return time


start = Time(3, 0, 0)

# start.print_time()
print(start)

duration = Time(1, 35, 0)
end = start + duration
print(end)

print(start.time_to_int())

end = start.increment(100)
end.print_time()
print(end.is_after(start))

now = Time(3, 36, 0) # creating a Time object with flexibility
now.print_time()

time_2 = Time(second = 5)
time_2.print_time()

