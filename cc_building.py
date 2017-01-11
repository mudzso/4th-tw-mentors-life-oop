from codecool_class import CodeCoolClass
import random


class Building():

    def __init__(self, room_type):
        self.is_kitchen = False
        self.is_lounge = False
        self.is_main_room = False
        if room_type == "kitchen":
            self.iskitchen = True
        elif room_type == "lounge":
            self.is_lounge = True
        elif room_type == "main_room":
            self.is_main_room = True

    # Kitchen specific methods

    def student_has_coffee(self, cc_class):
        if self.is_kitchen:
            energy = 100
            while energy >= 90:
                student = random.choice(cc_class.students)
                gender_str = cc_class.get_student_gender_for_print(student, 2)
                energy = student.energy
            print("{} drank some coffe and {} energy increased by 10".format(student.name, gender_str))
        else:
            pass
