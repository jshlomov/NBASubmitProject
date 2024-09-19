from typing import List

from models.PlayerToTeam import PlayerToTeam
from repository.database import get_db_connection


def create_player_to_team(player: PlayerToTeam) -> int:
    with get_db_connection() as connection, connection.cursor() as cursor:
        cursor.execute("""
            INSERT INTO player_to_team (team_id, player_id)
            VALUES (%s, %s)
            RETURNING id;
        """, (player.team_id, player.player_id))

        new_id = cursor.fetchone()
        connection.commit()
        return new_id["id"] if new_id else 0


def get_players_by_team(team_id: int) -> List[PlayerToTeam]:
    with get_db_connection() as connection, connection.cursor() as cursor:
        cursor.execute("""
            SELECT id, team_id, player_id
            FROM player_to_team
            WHERE team_id = %s;
        """, (team_id,))

        res = cursor.fetchall()
        return [PlayerToTeam(id=r["id"], team_id=r["team_id"], player_id=r["player_id"]) for r in res]

def update_player_to_team(player: PlayerToTeam) -> None:
    with get_db_connection() as connection, connection.cursor() as cursor:
        cursor.execute("""
            UPDATE player_to_team
            SET team_id = %s, player_id = %s
            WHERE id = %s;
        """, (player.team_id, player.player_id, player.id))
        connection.commit()

def delete_player_from_team(player_id: int) -> None:
    with get_db_connection() as connection, connection.cursor() as cursor:
        cursor.execute("""
            DELETE FROM player_to_team
            WHERE id = %s;
        """, (player_id,))
        connection.commit()

