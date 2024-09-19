import pytest

from repository.Player_repository import get_all_players
from repository.database import create_tables, drop_tables
from repository.details_per_season_repository import get_all_details_per_season
from repository.load_to_db import load_players_from_api


@pytest.fixture(scope="module")
def setup_database():
    create_tables()
    #load_players_from_api()
    yield
    #drop_tables()


def test_all(setup_database):
    players = get_all_players()
    details = get_all_details_per_season()
    assert True

def test_get_all_players():
    players = get_all_players()
    assert len(players) == 20

