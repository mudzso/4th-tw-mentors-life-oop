from codecool_class import CodecoolClass
import random


class Teams():

    def __init__(self):
        self.team_name = ""
        self.team = []

    @classmethod
    def make_teams(cls, n_of_members):
        teams_list = []
        whole_class = cc_b.students
        while len(whole_class) > n_of_members:
            team = []
            for _ in range(n_of_members):
                member = random.choice(whole_class)
                team.append(member)
                whole_class.remove(member)

            temp = Teams()
            temp.team_name = team[0].first_name + "-team"
            temp.team = team
            teams_list.append(temp)
        temp = Teams()
        temp.team_name = whole_class[0].first_name + "-team"
        temp.team = whole_class
        teams_list.append(temp)
        return teams_list
