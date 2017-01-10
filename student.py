from person import Person


class Student(Person):

    def __init__(self, first_name=None, last_name=None, year_of_birth=None, gender=None, knowledge=None, energy=None):
        super().__init__(first_name, last_name, year_of_birth, gender)
        if knowledge == None or energy == None:
            raise TypeError("some data is missing")
        self.knowledge = knowledge
        self.energy = energy

    @classmethod
    def create_by_csv(cls, path="./data/students.csv"):
        csv_list = []
        student_list = []

        with open(path) as csv_file:
            students = csv_file.readlines()

        for student in students:
            csv_list.append(student.strip("\n").split(","))

        for student in csv_list:
            if len(student) < 6:
                raise TypeError("some data is missing")
            student_first_name = student[0]
            student_last_name = student[1]
            student_year_of_birth = int(student[2])
            student_gender = student[3]
            student_knowledge = int(student[4])
            student_energy = int(student[5])
            student_list.append(Student(student_first_name, student_last_name,
                                        student_year_of_birth, student_gender, student_knowledge, student_energy))

        return student_list
