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
            if  self.day > 29:
                return False
            return True
        elif self.month == 4 or 6 or 9 or 11:
            if  self.day > 30:
                return False
            return True
        elif self.month == 1 or 3 or 5 or 7 or 8 or 10 or 12:
            if self.day > 31:
                return False
            return True

    def __str__(self):
        return f'{self.year}.{self.month}.{self.day}'


class DateStamp(Date):
    def __init__(self, year, month, day):
        super().__init__(year, month, day)

d = Date(2020, 2, 22)
d.date_ent()
print(d)
print(d.validate())

now = datetime.now()
ds = DateStamp(now.year, now.month, now.day)
print(ds)
print(ds.validate())
