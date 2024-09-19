from venv import create

from config.config_sql import SQL_URI
from psycopg2.extras import RealDictCursor


def get_db_connection(psycopg2=None):
    return psycopg2.connect(SQL_URI, cursor_factory=RealDictCursor)

def create_tables():
    create_players_table()
    create_details_per_season_table()
    create_fantasy_team_table()

def drop_tables():
    drop_players_table()
    drop_details_per_season_table()
    drop_fantasy_team_table()


def create_players_table():
    with get_db_connection() as connection:
        with connection.cursor() as cursor:
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS players (
                id SERIAL PRIMARY KEY,
                player_name VARCHAR(100),
                player_id VARCHAR(50) UNIQUE
                )
            ''')
            connection.commit()

def create_details_per_season_table():
    with get_db_connection() as connection:
        with connection.cursor() as cursor:
            cursor.execute('''
                CREATE TABLE details_per_season (
                id SERIAL PRIMARY KEY,
                player_id INT REFERENCES players(id) ON DELETE CASCADE,
                position VARCHAR(50),
                age INT,
                games INT,
                field_goals INT,
                field_attempts INT,
                field_percent FLOAT,
                three_percent FLOAT,
                two_percent FLOAT,
                assists INT,
                turnovers INT,
                points INT,
                team VARCHAR(50),
                season INT
                )
            ''')
            connection.commit()

def create_fantasy_team_table():
    with get_db_connection() as connection:
        with connection.cursor() as cursor:
            cursor.execute('''
                CREATE TABLE fantasy_team (
                id SERIAL PRIMARY KEY,
                C INT REFERENCES players(id) ON DELETE CASCADE,
                PF INT REFERENCES players(id) ON DELETE CASCADE,
                SF INT REFERENCES players(id) ON DELETE CASCADE,
                SG INT REFERENCES players(id) ON DELETE CASCADE,
                P INT REFERENCES players(id) ON DELETE CASCADE
                )
            ''')
            connection.commit()

def drop_players_table():
    with get_db_connection() as connection, connection.cursor() as cursor:
        cursor.execute("DROP TABLE players CASCADE")
        connection.commit()

def drop_details_per_season_table():
    with get_db_connection() as connection, connection.cursor() as cursor:
        cursor.execute("DROP TABLE details_per_season CASCADE")
        connection.commit()

def drop_fantasy_team_table():
    with get_db_connection() as connection, connection.cursor() as cursor:
        cursor.execute("DROP TABLE fantasy_team CASCADE")
        connection.commit()