from user import User
from user import PowerUser


def run_tests():
    user1 = User("Bob")
    user2 = User("Jane")
    power_user = PowerUser("Power", 500)

    print(user1)
    print(user2)
    print(power_user)

    # Test give_taco method
    user1.give_taco(3, user2)
    power_user.give_taco(1, user1)
    power_user.give_taco(4, user1)

    # print(user1)
    # print(user2)
    # print(power_user)

    users = [user1, user2, power_user]
    for user in users:
        print(user)

    print(user1 < power_user)
    print(user1 < user2)


if __name__ == '__main__':
    run_tests()
