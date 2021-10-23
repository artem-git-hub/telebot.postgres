# for PostgreSQL
host = "127.0.0.1"
user = "shopbot"
password = "shopmebot"
db_name = "shop"
port = 5432




# for telegram
from helper import select_db

TOKEN = select_db("value", "settings", "name = 'bot_token'")[0][0]
TOKEN_MANAGER = select_db("value", "settings", "name = 'bot_manager_token'")[0][0]



