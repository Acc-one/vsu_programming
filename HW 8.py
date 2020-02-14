class Date:
    def __init__(self):
        self.year = None
        self.month = None
        self.day = None

     def date_ent(self):
        self.year = input('Year: ')
        self.month = input('Month: ')
        self.day = input('Day: ')

     def __str__(self):
        return self.year, self.month, self.day, sep='.' 

 d = Date()
d.date_ent()
d.__str__()
