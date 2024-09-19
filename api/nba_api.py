import requests

def get_from_nba_api(season):
    NBA_URL = f"http://b8c40s8.143.198.70.30.sslip.io/api/PlayerDataTotals/query?season={season}&&pageSize=15"
    response = requests.get(NBA_URL)
    return response.json()


