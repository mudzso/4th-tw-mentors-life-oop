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


# cc_b = CodecoolClass.generate_local()
# print(cc_b.find_student_by_full_name("Eizaburô Atuti"))
# print(cc_b.find_mentor_by_full_name("Józsi"))
