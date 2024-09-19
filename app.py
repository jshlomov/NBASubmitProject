from flask import Flask

from controllers.player_controller import player_blueprint
from repository.database import create_tables, drop_tables
from repository.load_to_db import load_players_from_api

app = Flask(__name__)

if __name__ == '__main__':
    # create_tables()
    # load_players_from_api()
    # drop_tables()
    app.register_blueprint(player_blueprint, url_prefix="/api/players")
    app.run(debug=True)