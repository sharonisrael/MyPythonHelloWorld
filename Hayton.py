class Animal:

    zoo_name = "Hayaton"

    def __init__(self, given_name, given_hunger=0):
        self._name = given_name
        self._hunger = given_hunger

    def get_name(self):
        return self._name

    def is_hungry(self):
        return self._hunger > 0

    def feed(self):
        self._hunger -= 1

    def talk(self):
        print("Animal sound")

    def __str__(self):
        return __name__ + " " + self._name


class Dog(Animal):

    def talk(self):
        print("woof woof")

    def fetch_stick(self):
        print("There you go, sir!")


class Cat(Animal):

    def talk(self):
        print("meow")

    def chase_laser(self):
        print("Meeeeow")


class Skunk(Animal):

    def __init__(self, given_name, given_hunger=0, given_stink_count=6):
        super().__init__(given_name, given_hunger)
        _stink_count = given_stink_count

    def talk(self):
        print("tsssss")

    def stink(self):
        print("Dear lord!")


class Unicorn(Animal):

    def talk(self):
        print("Good day, darling")

    def sing(self):
        print("I’m not your toy...")


class Dragon(Animal):

    def __init__(self, given_name, given_hunger=0, given_color="Green"):
        super().__init__(given_name, given_hunger)
        _color = given_color

    def talk(self):
        print("Raaaawr")

    def breath_fire(self):
        print("$@#$#@$")


def main():
    zoo_lst = create_first_phase_animals()
    new_zoo_lst = create_second_phase_animals()
    zoo_lst += new_zoo_lst
    perform_animals_actions(zoo_lst)
    print(Animal.zoo_name)


def create_first_phase_animals():
    brownie = Dog("Brownie", 10)
    zelda = Cat("Zelda", 3)
    stinky = Skunk("Stinky", 0)
    keith = Unicorn("Keith", 7)
    lizzy = Dragon("Lizzy", 1450)
    return [brownie, zelda, stinky, keith, lizzy]


def perform_animals_actions(zoo_lst):
    # loop over all animals
    for animal in zoo_lst:
        print(str(type(animal))[17:-2] + " " + animal.get_name())
        feed_animal_until_full(animal)
        animal.talk()
        run_animal_unique_action(animal)


def feed_animal_until_full(animal):
    while animal.is_hungry():
        animal.feed()


def run_animal_unique_action(animal):
    if isinstance(animal, Dog):
        animal.fetch_stick()
    elif isinstance(animal, Cat):
        animal.chase_laser()
    elif isinstance(animal, Skunk):
        animal.stink()
    elif isinstance(animal, Unicorn):
        animal.sing()
    elif isinstance(animal, Dragon):
        animal.breath_fire()
    else:
        print("Unknown animal")


def create_second_phase_animals():
    doggo = Dog("Doggo", 80)
    kitty = Cat("Kitty", 80)
    stinky_jr = Skunk("Stinky Jr.", 80)
    clair = Unicorn("Clair", 80)
    mcfly = Dragon("McFly", 80)
    return [doggo, kitty, stinky_jr, clair, mcfly]


if __name__ == "__main__":
    main()
