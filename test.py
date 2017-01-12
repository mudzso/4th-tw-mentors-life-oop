import random
import story


class Test:

    def __init__(self):
        self.name = None
        self.admin = None
        self.participants = None
        self.knowledge_to_pass = 40
        self.result = None
        self.passed_students = []
        self.failed_students = []

    @classmethod
    def organize_test(cls, name, cc_class):
        test = Test()
        test.name = name
        test.admin = random.choice(cc_class.mentors)
        test.participants = cc_class.students

        return test

    def grade_test(self, knowledge_to_pass, participants):
        result = {'Pass': 0, 'Fail': 0}
        passed_students = []
        failed_students = []
        for student in participants:
            if student.knowledge >= knowledge_to_pass:
                result['Pass'] += 1
                passed_students.append(student)
            else:
                result['Fail'] += 1
                failed_students.append(student)
        print('{} students passed and {} students failed {}.'.format(result['Pass'], result['Fail'], self.name))
        self.result = result
        self.passed_students = passed_students
        self.failed_students = failed_students

    def check_admin_satisfaction(self):
        if len(self.failed_students) >= len(self.participants) * 0.1:
            print('You are a disgrace to Codecool Tokyo! {} is ashamed!'.format(self.admin.nickname))
        else:
            print('{} is pleased with the results.'.format(self.admin.nickname))

    def failers_repeat(self):
        temp_list_for_failed = []
        for student in self.failed_students:
            if student.knowledge >= self.knowledge_to_pass:
                self.result['Fail'] -= 1
                self.result['Pass'] += 1
                self.passed_students.append(student)
            else:
                temp_list_for_failed.append(student)
        self.failed_students = temp_list_for_failed
