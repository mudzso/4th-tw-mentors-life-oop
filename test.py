import random
from codecool_class import CodecoolClass
from mentor import Mentor
from student import Student


class Test:

    def __init__(self):
        self.name = None
        self.admin = None
        self.participants = None
        self.passing_percent = 50
        self.result = {'Pass': None, 'Fail': None}

    @classmethod
    def organize_test(cls, name):
        test = Test()
        test.name = name
        test.admin = random.choice(CodecoolClass.generate_local().mentors)
        test.participants = CodecoolClass.generate_local().students
        test.result = Test.grade_test(test.passing_percent, test.participants)

        return test

    def grade_test(passing_percent, participants):
        result = {'Pass': 0, 'Fail': 0}
        for student in participants:
            if student.knowledge > passing_percent:
                result['Pass'] += 1
            else:
                result['Fail'] += 1

        return result


test_1 = Test.organize_test("asd")
print(test_1.result)
print(test_1.participants[0].first_name)
print(test_1.admin.first_name)