from config.config_sql import SQL_URI
from psycopg2.extras import RealDictCursor


def get_db_connection(psycopg2=None):
    return psycopg2.connect(SQL_URI, cursor_factory=RealDictCursor)

def create_players_table():
    with get_db_connection() as connection:
        with connection.cursor() as cursor:
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS players (
                    id SERIAL PRIMARY KEY,
                    question_text VARCHAR(255) NOT NULL,
                    correct_answer VARCHAR(255) NOT NULL
                )
            ''')
            connection.commit()