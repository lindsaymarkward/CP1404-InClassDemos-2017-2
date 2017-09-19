from user import User
from team import Team

if __name__ == '__main__':
    # create and print a default Team
    team = Team()
    print(team)
    # add users
    team.add(User("Cam"))
    team.add(User("Pam"))
    # make one user different
    team.get("Pam").score += 1
    print(team)
    # test get with existing user
    print(team.get("Pam"))
    # test get with missing user
    print(team.get("Sam"))
    # test get_leader
    print(team.get_leader())
