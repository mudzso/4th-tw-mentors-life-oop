from codecool_class import CodecoolClass
from mentor import Mentor
from student import Student
from team import *
import random
from cc_building import Building
# init csvből tanulók generálodnak,mentorok meg maga a suli is. reggeli assignment, csapat generálás input
# print csapatok assignment pontjai, ha üres
# random esemény, input, BFA, input ha empty no adat,egyébként stats, aljasodás.


def choose_random_event(times):
    for i in range(times):
        chooser = random.randint(1, 99)
        if chooser < 20:
            kitchen.drink_tea_and_chat(cc_tokyo)
        elif chooser < 40:
            kitchen.private_mentoring(cc_tokyo)
        elif chooser < 60:
            kitchen.student_has_coffee(cc_tokyo)
        elif chooser < 80:
            lounge.play_a_game_of_darts(cc_tokyo)
        elif chooser < 100:
            lounge.private_mentoring(cc_tokyo)


def main():

    cc_tokyo = CodecoolClass.generate_local()
    cc_tokyo.location = "Tokyo"
    print("Generating codecool class in the year of {} in the city of {} with {} mentors and {} students in class.".format(
        str(cc_tokyo.year), cc_tokyo.location, str(len(cc_tokyo.mentors)), str(len(cc_tokyo.students))))
    teams = Team.make_teams(4, cc_tokyo)
    Team.do_assigment_with_random_teams(teams)
    kitchen = Building("kitchen")
    lounge = Building("lounge")

    times = int(input("How many hours untill BFA?"))
    choose_random_event(times)

if __name__ == "__main__":
    main()
