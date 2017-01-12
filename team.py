from codecool_class import CodecoolClass
import random
import story

class Team():

    def __init__(self):
        self.team_name = ""
        self.team = []

    @classmethod
    def make_teams(cls, n_of_members, cc_class):
        teams_list = []
        whole_class = cc_class.students
        while len(whole_class) > n_of_members:
            team = []
            for _ in range(n_of_members):
                member = random.choice(whole_class)
                team.append(member)
                whole_class.remove(member)

            temp = Team()
            temp.team_name = team[0].first_name + "-team"
            temp.team = team
            teams_list.append(temp)
        temp = Team()
        temp.team_name = whole_class[0].first_name + "-team"
        temp.team = whole_class
        teams_list.append(temp)

        return teams_list

    @classmethod
    def team_knowledge_levels(cls, Teams, team_name):
        knowledge_level = 0
        for team in Teams:
            if team.team_name == team_name:
                for member in team.team:
                    knowledge_level += member.knowledge
                return "{}:{}".format(team.team_name, knowledge_level)
        return "Not found team"

    @classmethod
    def do_assigment_with_random_teams(cls, teams):
        print("The teams were given an assignment")
        for team in teams:
            score = Team.team_knowledge_levels(teams, team.team_name)
            score = score.split(":")
            score_dict = {score[0]: score[1]}
            for k, v in score_dict.items():
                print("{} achieved {} points based on their average knowledge".format(k, int(v) // len(team.team)))
