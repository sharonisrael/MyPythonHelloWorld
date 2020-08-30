class BigThing:

    def __init__(self, given_object):
        self._my_object = given_object

    def size(self):
        #    אם המשתנה הוא מספר - המתודה מחזירה את המספר
        # אם המשתנה הוא רשימה/מילון/מחרוזת - המתודה מחזירה את אורך המשתנה (len).
        if(isinstance(self._my_object, int)):
            return self._my_object
        elif(isinstance(self._my_object, (list, dict, str))):
            return len(self._my_object)
        else:
            return -1


class BigCat(BigThing):

    def __init__(self, given_object, given_weight):
        # Using super
        super().__init__(given_object)
        # Alternative option
        # BigThing.__init__(self, given_object)
        self._my_weight = given_weight

    def size(self):
        if (self._my_weight > 20):
            return "Very fat"
        elif (self._my_weight > 15):
            return "Fat"
        else:
            return "OK"


def main():
    # my_thing = BigThing("balloon")
    # print(my_thing.size())
    # 7
    cutie = BigCat("mitzy", 22)
    print(cutie.size())
    # Very Fat


if __name__ == "__main__":
    main()
