class Date:
    def __init__(self):
        self.year = None
        self.month = None
        self.day = None

    def date_ent(self):
        self.year = input('Year: ')
        self.month = input('Month: ')
        self.day = input('Day: ')

    def date_print(self):
        print(self.year, self.month, self.day, sep='.')

d = Date()
d.date_ent()
d.date_print()
