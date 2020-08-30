from students_db import StudentDB
import pytest

# Makes it run only once in the 'module' and not before all tests
# Can be @pytest.fixture(scope="session") --> @pytest.fixture(scope="module") --> @pytest.fixture
@pytest.fixture(scope='module')
def db():
    print('----------setup----------------')
    db = StudentDB()
    db.connect('data.json')
    yield db
    # After all completed all tests
    print('----------teardown----------------')
    db.close()


def test_scott_data(db):
    scott_data = db.get_data('Scott')
    assert scott_data['id'] == 1
    assert scott_data['name'] == 'Scott'
    assert scott_data['result'] == 'pass'


def test_mark_data(db):
    mark_data = db.get_data('Mark')
    assert mark_data['id'] == 2
    assert mark_data['name'] == 'Mark'
    assert mark_data['result'] == 'fail'

