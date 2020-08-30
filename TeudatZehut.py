def check_id_valid(id_number):
    """
    This function gets id number of 9 digits and returns if id number is valid
    :param int id_number: Id number
    :return: is Id valid
    :rtype: bool
    """
    min_id = 100000000  # 9 digits
    max_id = 999999999  # 9 digits
    # Verify it's a 9 digit number
    if not isinstance(id_number, int):
        raise TypeError("Id must be integer with only digits")
    if id_number < min_id or id_number > max_id:
        raise ValueError("Id must be 9 digits int number")

    # Double every number in 1 (odd index) or 2 (even index) depending position
    multiplied_odd_id = list(map(lambda value: int(value) * 1, str(id_number)[::2]))
    # Check every multiplication. If it's above 9 then sum the digits. For example 8 * 2 = 16 => 7
    multiplied_even_id = list(map(lambda value: (int(value) * 2) // 10 + (int(value) * 2) % 10, str(id_number)[1::2]))
    #  sum all the values in the outcomes
    sum_all_multiplied = sum(multiplied_odd_id) + sum(multiplied_even_id)
    # check if sum divides by 10 without remaining
    valid_id = (sum_all_multiplied % 10) == 0
    # return
    return valid_id


def run_check_id_valid(id_number):
    print(check_id_valid(id_number))


class IDIterator:
    min_id = 100000000  # 9 digits
    max_id = 999999999  # 9 digits

    def __init__(self, given_id):
        # id is integer number with 9 digits
        if not isinstance(given_id, int):
            raise TypeError("Id must be integer with only digits")
        if given_id < IDIterator.min_id or given_id > IDIterator.max_id:
            raise ValueError("Id must be 9 digits number")
        # set member
        self._id = given_id

    def __iter__(self):
        return self

    def __next__(self):
        new_id = self._id
        while True:
            # progress to next id candidate
            new_id += 1
            # stop after all id digits complete
            if new_id >= IDIterator.max_id:
                raise StopIteration()
            if check_id_valid(new_id):
                break
        self._id = new_id
        return new_id


def run_id_iterator(id_number):
    id_iterator = IDIterator(id_number)
    for i in range(10):
        try:
            print(next(id_iterator))
        except StopIteration:
            print("No more possible valid ids")
            break


def id_generator(id_number):
    """
    A generator to create consecutive valid id numbers
    In rtype can put Generator[int, Any, None] or Iterator[int]
    :param int id_number: id number to start from
    :return: yield new valid id
    :rtype: Generator[int, Any, None]
    """
    min_id = 100000000  # 9 digits
    max_id = 999999999  # 9 digits
    # id is integer number with 9 digits
    if not isinstance(id_number, int):
        raise TypeError("Id must be integer with only digits")
    if id_number < min_id or id_number > max_id:
        raise ValueError("Id must be 9 digits number")
    # generate and yield id
    new_id = id_number
    while new_id <= max_id:  # Go over all next ids with 9 digits
        # progress to next id candidate
        new_id += 1
        # of valid id then yield new id
        if check_id_valid(new_id):
            yield new_id


def run_id_generator(id_number):
    my_id_generator = id_generator(id_number)
    for i in range(10):
        try:
            print(next(my_id_generator))
        except StopIteration:
            print("No more possible valid ids")
            break


def main():
    # For example 123456780, 123456782
    id_number_input = input("Please enter Id: ")
    # check input has digits only
    if not id_number_input.isdigit():
        print("Id must contain digits only:", id_number_input)
        exit()

    # Convert to int
    id_number = int(id_number_input)
    # check input has 9 digits
    min_id = 100000000  # 9 digits
    max_id = 999999999  # 9 digits
    if id_number < min_id or id_number > max_id:
        print("Id must be 9 digits number:", id_number_input)
        exit()

    # run id operations
    print("Id number")
    print(id_number)
    print("Check id is valid")
    run_check_id_valid(id_number)
    print("Create 10 next ids using iterator")
    run_id_iterator(id_number)
    print("Create 10 next ids using generator")
    run_id_generator(id_number)


if __name__ == "__main__":
    main()
