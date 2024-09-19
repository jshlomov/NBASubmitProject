import pytest

from repository.database import create_tables, drop_tables


@pytest.fixture(scope="module")
def setup_database():
    create_tables()

    yield
    drop_tables()


def test_users_from_api(setup_database):
    users = get_all_users()
    assert len(users) == 4