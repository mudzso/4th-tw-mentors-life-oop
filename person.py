class Person:

    def __init__(self, first_name=None, last_name=None, year_of_birth=None, gender=None):
        if gender == None or year_of_birth == None or last_name == None or first_name == None:
            raise TypeError("some data is missing")
        self.first_name = first_name
        self.last_name = last_name
        self.year_of_birth = year_of_birth
        self.gender = gender
