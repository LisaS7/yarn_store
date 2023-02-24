import json
from pathlib import Path

USER_CONFIG_PATH = Path.cwd() / "config" / "user_config.json"
DB_CONFIG_PATH = Path.cwd() / "config" / "db_config.json"


def read_db_config():
    with open(DB_CONFIG_PATH) as f:
        return json.load(f)


def read_user_config():
    with open(USER_CONFIG_PATH) as f:
        return json.load(f)


def write_user_config(data):
    with open(USER_CONFIG_PATH, "w+") as f:
        json_data = json.dumps(data)
        f.write(json_data)
