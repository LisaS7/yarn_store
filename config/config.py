import json
from pathlib import Path
from dataclasses import dataclass

USER_CONFIG_PATH = Path.cwd() / "config" / "user_config.json"
DB_CONFIG_PATH = Path.cwd() / "config" / "db_config.json"


@dataclass
class Config:
    def __post_init__(self):
        self.read_db_config()
        self.read_user_config()
        self.get_stock_threshold()

    def read_db_config(self):
        with open(DB_CONFIG_PATH) as f:
            self.db_data = json.load(f)

    def read_user_config(self):
        with open(USER_CONFIG_PATH) as f:
            self.user_data = json.load(f)

    @staticmethod
    def write_user_config(data):
        with open(USER_CONFIG_PATH, "w+") as f:
            json_data = json.dumps(data)
            f.write(json_data)

    def get_stock_threshold(self):
        self.low_stock_threshold = int(self.user_data["low_stock_threshold"])


config = Config()
