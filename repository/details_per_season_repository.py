from models.DetailsPerSeason import DetailsPerSeason
from repository.database import get_db_connection


def get_all_details_per_season():
    with get_db_connection() as connection, connection.cursor() as cursor:
        cursor.execute("SELECT * FROM details_per_season")
        res = cursor.fetchall()
        details = [DetailsPerSeason(**d) for d in res]
        connection.commit()
        return details

def get_details_per_season_by_id(id):
    with get_db_connection() as connection, connection.cursor() as cursor:
        cursor.execute("SELECT * FROM details_per_season WHERE id = %s", (id,))
        res = cursor.fetchone()
        details_per_season = DetailsPerSeason(**res)
        connection.commit()
        return details_per_season

def create_details_per_season(details: DetailsPerSeason) -> int:
    with get_db_connection() as connection, connection.cursor() as cursor:
        cursor.execute("""
            INSERT INTO details_per_season (
                player_id, player_name, position, age, games, field_goals, field_attempts, field_percent, 
                three_percent, two_percent, assists, turnovers, points, team, season
            ) 
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            RETURNING id
        """, (
            details.player_id, details.player_name, details.position, details.age, details.games, details.field_goals,
            details.field_attempts, details.field_percent, details.three_percent, details.two_percent,
            details.assists, details.turnovers, details.points, details.team, details.season
        ))

        new_id = cursor.fetchone()["id"]
        connection.commit()
        return new_id