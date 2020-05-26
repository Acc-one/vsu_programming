from datetime import datetime

class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def date_ent(self):
        self.year = int(input('Year: '))
        self.month = int(input('Month: '))
        self.day = int(input('Day: '))

    def validate(self):
        if self.month > 12:
            return False
        elif self.month == 2:
            return self.day <= 29
        elif self.month in [4, 6, 9, 11]:
            return self.day <= 30
        elif self.month in [1, 3, 5, 7, 8, 10, 12]:
            return self.day <= 31

    def __str__(self):
        return f'{self.year}.{self.month}.{self.day}'

    def set_date(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day
        if not self.__validate():
            raise ValueError('Date incorrect')

    
class DateStamp(Date):
    def __init__(self):
        now = datetime.now()
        super().__init__(now.year, now.month, now.day)
        
d = Date(2020, 2, 20)
print(d)
print(d.validate())

ds = DateStamp()
print(ds)
