class Octopus:

    count_animals = 0

    def __init__(self, name = "Octavio", age = 0):
        self._name = name
        self._age = 0
        Octopus.count_animals += 1

    def birthday(self):
        self._age += 1

    def get_age(self):
        return self._age

    def set_name(self, given_name):
        self._name = given_name

    def get_name(self):
        return self._name


def main():
    # Create octopus instances
    first_octopus = Octopus("Sharon")
    second_octopus = Octopus()

    # First octopus has birthday
    first_octopus.birthday()

    # Print octopuses ages
    print("Octopus ages:", first_octopus.get_age(), second_octopus.get_age())
    print("Octopus names:", first_octopus.get_name(), second_octopus.get_name())

    # Change second octopus name and print names
    second_octopus.set_name("Dana")
    print("Octopus names:", first_octopus.get_name(), second_octopus.get_name())

    # Print octopus count
    print("Octopus count animals", Octopus.count_animals)

if __name__ == "__main__":
    main()

