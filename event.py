from codecool_class import CodecoolClass
import random


class Event():

    def __init__(self):
        self.event_name = None
        self.CClass = None
        self.drink_alcohol = False
        self.location = None
        self.date = None

    @classmethod
    def organize_event(cls, CClass):
        event = Event()
        event.event_name = input("Event name:")
        event.CClass = CClass
        event.drink_alcohol = True if input("alkohol is allowed(y or n): ") == "y" else False
        event.location = input("event location: ")
        event.date = input("event of date(yyyy.mm.dd): ")
        return event

    def get_drunk(self):
        if self.drink_alcohol:
            alcohols = ["Pálinka", "Sör", "Whisky", "Szaké"]
            palinka_counter = 0
            sor_counter = 0
            whisky_counter = 0
            szake_counter = 0
            drunk = False
            overall_knowledge = self.CClass.get_student_all_knowledge()
            print("Baszunk beljebb")
            overall_energy_level = self.CClass.get_student_all_energy()
            print("base energy level is: {}".format(overall_energy_level))
            while not drunk:
                alcohol = random.choice(alcohols)

                if overall_energy_level < 0:
                    students = len(self.CClass.students)
                    print("Megérkeztünk gyöngyöspatára!")
                    print("{} feles pálinka,{} liter sör, {} whisky kóla,{} feles szaké fogyot el".format(palinka_counter * students,
                                                                                                          sor_counter * students, whisky_counter * students, szake_counter * students))
                    drunk = True

                elif alcohol == "Pálinka":
                    print("Kanpai! donburibachi ha-dodorinku")
                    overall_energy_level -= 300
                    palinka_counter += 1
                elif alcohol == "Sör":
                    print("Kanpai! nomimono bakushu ")
                    overall_energy_level -= 100
                    sor_counter += 1
                elif alcohol == "Whisky":
                    print("Kanpai pota-ju ba-bon")
                    overall_energy_level -= 200
                    whisky_counter += 1
                elif alcohol == "Szaké":
                    print("Kanpai! utsuwa hyakuyakunochou")
                    overall_energy_level -= 180
                    szake_counter += 1

miskolc = CodecoolClass.generate_local()
beba = Event.organize_event(miskolc)
beba.get_drunk()
