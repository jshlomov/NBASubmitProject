from api.nba_api import get_from_nba_api
from models.Player import Player
from repository.database import get_db_connection


# def get_user_from_json(json):
#     return User(**{
#         "first" : get_in(["name", "first"], json),
#         "last": get_in(["name", "last"], json),
#         "email": get_in(["email"], json)
#     })

def get_all_players():
    with get_db_connection() as connection, connection.cursor() as cursor:
        cursor.execute("SELECT * FROM players")
        res = cursor.fetchall()
        players = [Player(**u) for u in res]
        connection.commit()
        return players

def get_user_by_id(id):
    with get_db_connection() as connection, connection.cursor() as cursor:
        cursor.execute("SELECT * FROM players WHERE id = %s", (id,))
        res = cursor.fetchone()
        player = Player(**res)
        connection.commit()
        return player

def create_user(player: Player) -> int:
    with get_db_connection() as connection, connection.cursor() as cursor:
        cursor.execute("""
            INSERT INTO players (playerName, playerId)
            VALUES (%s, %s)
            ON CONFLICT (player_id) DO NOTHING
            RETURNING id;
        """, (player.player_name, player.player_id))
        new_id = cursor.fetchone()['id']
        connection.commit()
        return new_id