"""Module."""


class User:
    """Class."""
    INITIAL_TACOS_TO_GIVE = 5

    def __init__(self, name=""):
        """Method."""
        self.name = name
        self.number_of_tacos = self.INITIAL_TACOS_TO_GIVE
        self.score = 0

    def __str__(self):
        return "{}, {} points, {} tacos remaining".format(self.name,
                                                          self.score,
                                                          self.number_of_tacos)

    def give_taco(self, number_given, other):
        if self.number_of_tacos >= number_given:
            self.number_of_tacos -= number_given
            other.score += number_given
            return True
        else:
            return False

    def __lt__(self, other):
        return self.score < other.score


class PowerUser(User):
    def __init__(self, name="", multiplier=2):
        super().__init__(name)
        self.multiplier = multiplier

    def __str__(self):
        return "*" + super().__str__()

    def give_taco(self, number_given, other):
        if self.number_of_tacos >= number_given:
            self.number_of_tacos -= number_given
            other.score += (self.multiplier * number_given)
            return True
        else:
            return False
