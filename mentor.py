from person import Person


class Mentor(Person):

    def __init__(self, first_name=None, last_name=None, year_of_birth=None, gender=None, nickname=None):
        super().__init__(first_name, last_name, year_of_birth, gender)
        if nickname == None:
            raise TypeError("some data is missing")
        self.nickname = nickname

    @classmethod
    def create_by_csv(cls, path="./data/mentors.csv"):
        csv_list = []
        mentor_list = []

        with open(path) as csv_file:
            mentors = csv_file.readlines()

        for mentor in mentors:
            csv_list.append(mentor.strip("\n").split(","))

        for mentor in csv_list:
            mentor_first_name = mentor[0]
            mentor_last_name = mentor[1]
            mentor_year_of_birth = int(mentor[2])
            mentor_gender = [3]
            mentor_nickname = [4]
            mentor_list.append(Mentor(mentor_first_name, mentor_last_name,
                                      mentor_year_of_birth, mentor_gender, mentor_nickname))

        return mentor_list
