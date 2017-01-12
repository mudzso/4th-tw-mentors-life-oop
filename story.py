from codecool_class import CodecoolClass
from mentor import Mentor
from student import Student
from team import Team
import random
from cc_building import Building
from test import Test
from copy import deepcopy
import time
from event import Event
# init csvből tanulók generálodnak,mentorok meg maga a suli is. reggeli assignment, csapat generálás input
# print csapatok assignment pontjai, ha üres
# random esemény, input, BFA, input ha empty no adat,egyébként stats, aljasodás.


def main():

    cc_tokyo = CodecoolClass.generate_local()
    students_copy = deepcopy(cc_tokyo)
    cc_tokyo.location = "Tokyo"
    print("Generating codecool class in the year of {} in the city of {} with {} mentors and {} students in class.".format(
        str(cc_tokyo.year), cc_tokyo.location, str(len(cc_tokyo.mentors)), str(len(cc_tokyo.students))))
    time.sleep(3)
    teams = Team.make_teams(4, students_copy)
    Team.do_assigment_with_random_teams(teams)
    kitchen = Building("kitchen")
    lounge = Building("lounge")

    times = int(input("How many hours untill BFA?"))
    for i in range(times):
        chooser = random.randint(1, 99)
        if chooser < 20:
            kitchen.drink_tea_and_chat(cc_tokyo)
            time.sleep(3)
        elif chooser < 40:
            kitchen.private_mentoring(cc_tokyo)
            time.sleep(3)
        elif chooser < 60:
            kitchen.student_has_coffee(cc_tokyo)
            time.sleep(3)
        elif chooser < 80:
            lounge.play_a_game_of_darts(cc_tokyo)
            time.sleep(3)
        elif chooser < 100:
            lounge.private_mentoring(cc_tokyo)
            time.sleep(3)

    print("\n\nWARNING!!! BFA IMMINENT!!! EVERYONE GET TO SAFETY!!! WARNING!!!\n\n")
    time.sleep(3)
    bfa = Test.organize_test("BFA", cc_tokyo)
    bfa.grade_test(random.randint(25, 60), cc_tokyo.students)
    time.sleep(3)
    bfa.check_admin_satisfaction()
    time.sleep(3)
    bfa.failers_get_private_mentoring(bfa.failed_students, cc_tokyo)
    time.sleep(3)
    print("After the private mentorings the classes overall knowledge increase to:", end="")
    print(cc_tokyo.get_student_all_knowledge())
    time.sleep(3)
    bfa.failers_repeat()
    print("Failers retake the BFA the samurai way!!!")
    time.sleep(3)
    bfa.check_admin_satisfaction()
    print("The day is over, lets go drinking!")
    beba = Event.organize_event(cc_tokyo)
    beba.get_drunk()

    print("And thats how a day goes in Codecool.")


if __name__ == "__main__":
    main()
