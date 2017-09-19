from operator import attrgetter
from user import User


class Team:
    def __init__(self):
        self.users = []

    def __str__(self):
        return str([str(user) for user in self.users])

    def add(self, user):
        self.users.append(user)

    def get(self, name):
        for user in self.users:
            if user.name == name:
                return user
        return None

    def get_leader(self):
        self.users.sort(key=attrgetter("score"), reverse=True)
        return self.users[0]
