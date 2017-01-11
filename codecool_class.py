from mentor import Mentor
from student import Student


class CodecoolClass:

    def __init__(self):
        self.location = None
        self.year = 2017
        self.mentors = []
        self.students = []

    @classmethod
    def generate_local(cls):

        result = CodecoolClass()
        result.mentors = Mentor.create_by_csv()
        result.students = Student.create_by_csv()
        return result

    def get_student_gender_for_print(self, student, form):

        pronouns = [["he", "she", "it"], ["him", "her", "it"], ["his", "her", "its"]]

        if student == "male":
            return pronouns[form - 1][0]
        if student == "female":
            return pronouns[form - 1][1]
        if student == "notsure":
            return pronouns[form - 1][2]

    def find_student_by_full_name(self, full_name):
        for i in range(len(self.students)):
            if full_name == self.students[i].first_name + " " + self.students[i].last_name:
                return self.students[i]
        return "Student is not found"

    def find_mentor_by_full_name(self, full_name):

        for i in range(len(self.mentors)):
            if full_name == self.mentors[i].first_name + " " + self.mentors[i].last_name:
                return self.mentors[i]
        return "Mentor is not found"

    def get_student_all_knowledge(self):
        overall_knowledge = 0
        for i in range(len(self.students)):

            over_all_knowledge += self.students[i].knowledge
        return over_all_knowledge if over_all_knowledge < 9000 else "Its OVER 9000"

    def get_student_all_energy(self):
        over_all_energy = 0
        for i in range(len(self.students)):
            over_all_energy += self.students[i].energy
        return over_all_energy
