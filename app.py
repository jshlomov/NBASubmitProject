from flask import Flask
from repository.database import create_tables
from repository.load_to_db import load_players_from_api

app = Flask(__name__)

if __name__ == '__main__':
    #create_tables()
    #load_players_from_api()
    app.register_blueprint(fighter_blueprint, url_prefix="/api/fighters")
    app.run(debug=True)