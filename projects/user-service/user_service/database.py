"""
This module is responsible for holding the database connection instance.
In this case we are going to use SQLite.

Useful Links
 - https://www.digitalocean.com/community/tutorials/how-to-use-the-sqlite3-module-in-python-3
"""

import sqlite3
from os import makedirs


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]


class Database(metaclass=Singleton):

    path = "db/user-service-db.sqlite"

    def __init__(self) -> None:
        print(f"Connecting to {self.path} database...", end=" ")
        makedirs("db/", exist_ok=True)
        self.conn = sqlite3.connect(self.path)
        self.conn.row_factory = sqlite3.Row
        print("✅")

    def execute(self, query: str) -> None:
        cursor = self.conn
        cursor.execute(query)
        self.conn.commit()

    def select(self, query: str) -> list:
        cursor = self.conn
        rows = cursor.execute(query).fetchall()
        return [dict(row) for row in rows]

    def __del__(self) -> None:
        self.conn.close()
