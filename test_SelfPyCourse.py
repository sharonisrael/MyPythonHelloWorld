import pytest

import SelfPyCourse

# check as well test_students_db which has global object

# run before any test with prep as parameter
@pytest.fixture()
def prep():
    print("Preparing test")

# before module tests
def setup_module(module):
    print("----setup_module----")

# aftrer all module tests
def teardown_module(module):
    print("----teardown_module----")


# Change in the configuration Additional argument: -x to stop after first failure
# Change in the configuration Additional argument: --maxfail=2 to stop after 2 failures

def test_prep(prep):
    assert True

def test_prep2(prep):
    assert True


def test_simple_increment():
    assert SelfPyCourse.simple_increment(1) != 2


def test_simple_increment2():
    str_add = "Hello " + "World"
    assert str_add == "Hello World"
    assert "Good" in str_add


# Change in the configuration Additional argument: -k "giga"
def test_giga():
    assert False


# Change in the configuration Additional argument: -m "givenumber"
@pytest.mark.givenumber
def test_number_test():
    assert False


# skip test
@pytest.mark.skip(reason="I skipped this test")
def test_skipped_number_test():
    assert False

# Prints also the print. In Youtube saw Change in the configuration Additional argument: -s to show the print
def test_print_number_test():
    my_list = [1,2,3,4]
    print(my_list, "---------------------------")
    assert 7 in my_list

speed_data = {45, 50, 55, 100}
@pytest.mark.parametrize("speed_brake", speed_data)
def test_car_brake(speed_brake):
    car = Car(50)
    car.brake()
    assert car.speed == speed_brake
s