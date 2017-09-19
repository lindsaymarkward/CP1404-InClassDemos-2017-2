from user import User


def run_tests():
    user1 = User("Bob")
    user2 = User("Jane")

    print(user1)
    print(user2)

# Test give_taco method
    user1.give_taco(3, user2)

    print(user1)
    print(user2)

if __name__ == '__main__':
    run_tests()
