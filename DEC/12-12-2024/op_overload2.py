import datetime

class Time:
    def __init__(self):
        time_entry = input('Enter a time in hh:mm:ss format: ')
        self.__hours, self.__minutes, self.__seconds = map(int, time_entry.split(':'))
        # Store total seconds for easier calculations
        self.total_seconds = self.__hours * 3600 + self.__minutes * 60 + self.__seconds
    
    def __str__(self):
        return datetime.time(self.__hours, self.__minutes, self.__seconds).strftime("%H:%M:%S")
    
    def __add__(self, other):
        if not isinstance(other, Time):
            raise TypeError("unsupported operand type")
        
        total_seconds = self.total_seconds + other.total_seconds
        return self.convert(total_seconds)
    
    @staticmethod
    def convert(seconds):
        # Handle wraparound for 24-hour format
        seconds = seconds % (24 * 3600)
        hours = seconds // 3600
        seconds %= 3600
        minutes = seconds // 60
        seconds %= 60
        return f"{hours}:{minutes:02d}:{seconds:02d}"

# Example usage:
t1 = Time()
t2 = Time()
print(t1 + t2)