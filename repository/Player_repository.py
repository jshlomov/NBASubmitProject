from models.Player import Player
from repository.database import get_db_connection


def get_all_players():
    with get_db_connection() as connection, connection.cursor() as cursor:
        cursor.execute("SELECT * FROM players")
        res = cursor.fetchall()
        players = [Player(**u) for u in res]
        connection.commit()
        return players

def get_player_by_id(id):
    with get_db_connection() as connection, connection.cursor() as cursor:
        cursor.execute("SELECT * FROM players WHERE id = %s", (id,))
        res = cursor.fetchone()
        player = Player(**res)
        connection.commit()
        return player

def create_player(player: Player) -> int:
    with get_db_connection() as connection, connection.cursor() as cursor:
        cursor.execute("""
            INSERT INTO players (player_name, player_id)
            VALUES (%s, %s)
            ON CONFLICT (player_id) DO NOTHING
            RETURNING id;
        """, (player.player_name, player.player_id))

        new_id = cursor.fetchone()
        if new_id is None:
            cursor.execute("""
                SELECT id FROM players WHERE player_id = %s;
            """, (player.player_id,))
            new_id = cursor.fetchone()

        connection.commit()
        return new_id["id"] if new_id else 0