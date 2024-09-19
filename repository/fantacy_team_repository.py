from models.FantasyTeam import FantasyTeam
from repository.database import get_db_connection


def create_fantasy_team(team: FantasyTeam) -> int:
    with get_db_connection() as connection, connection.cursor() as cursor:
        cursor.execute("""
            INSERT INTO fantasy_team (name)
            VALUES (%s)
            RETURNING id;
        """, (team.name,))

        new_id = cursor.fetchone()
        connection.commit()
        return new_id["id"] if new_id else 0


def get_fantasy_team_by_id(team_id: int) -> FantasyTeam:
    with get_db_connection() as connection, connection.cursor() as cursor:
        cursor.execute("""
            SELECT id, name
            FROM fantasy_team
            WHERE id = %s;
        """, (team_id,))

        row = cursor.fetchone()
        return FantasyTeam(id=row["id"], name=row["name"]) if row else None

def update_fantasy_team(team: FantasyTeam) -> None:
    with get_db_connection() as connection, connection.cursor() as cursor:
        cursor.execute("""
            UPDATE fantasy_team
            SET name = %s
            WHERE id = %s;
        """, (team.name, team.id))
        connection.commit()

def delete_fantasy_team(team_id: int) -> None:
    with get_db_connection() as connection, connection.cursor() as cursor:
        cursor.execute("""
            DELETE FROM fantasy_team
            WHERE id = %s;
        """, (team_id,))
        connection.commit()
