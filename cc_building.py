from codecool_class import CodecoolClass
from student import Student
import random


class Building():

    def __init__(self, room_type):
        self.is_kitchen = False
        self.is_lounge = False
        if room_type == "kitchen":
            self.is_kitchen = True
        elif room_type == "lounge":
            self.is_lounge = True

    # Kitchen specific methods

    def student_has_coffee(self, cc_class):
        if self.is_kitchen:
            energy = 100
            while energy >= 90:
                student = random.choice(cc_class.students)
                gender_str = cc_class.get_student_gender_for_print(student, 3)
                energy = student.energy
            print("{} drank some coffe and {} energy increased by 10".format(student.last_name, gender_str))
        else:
            pass

    def drink_tea_and_chat(self, cc_class):
        if self.is_kitchen:
            people_in_kitchen = []
            people = []
            people = cc_class.students
            number_of_people = random.randint(2, 6)
            string_to_print = ""
            for i in range(number_of_people):
                people_in_kitchen.append(random.choice(people))
            for person in people_in_kitchen:
                person.energy += 5
                string_to_print += person.first_name + ", "
            print("{} had a cup of tea and chat together. They also gained 5 energy".format(string_to_print.strip(", ")))
        else:
            pass

    # Lounge specific methods

    def play_a_game_of_darts(self, cc_class):
        if self.is_lounge:
            people_in_lounge = []
            people = []
            people = cc_class.students
            number_of_people = random.randint(2, 6)
            string_to_print = ""
            for i in range(number_of_people):
                people_in_lounge.append(random.choice(people))
            for person in people_in_lounge:
                person.energy += 10
                string_to_print += person.first_name + ", "
            print("{} played a good game of darts. They also gained 10 energy.".format(string_to_print.strip(", ")))
        else:
            pass

    # Mixed methods

    def private_mentoring(self, cc_class):
        if self.is_kitchen or self.is_lounge:
            mentor = random.choice(cc_class.mentors)
            student_knowledge = 200
            while student_knowledge > 65:
                student = random.choice(cc_class.students)
                student_knowledge = student.knowledge
                if student_knowledge > 65:
                    student_knowledge = 200
                else:
                    print("{} mentor helps {} practice, {} gained 20 knowledge".format(
                        mentor.nickname, student.last_name, cc_class.get_student_gender_for_print(student, 1)))

        else:
            pass
