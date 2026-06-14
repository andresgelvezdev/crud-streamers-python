import sqlite3 as sql



def get_connection():
    return sql.connect("streamers.db")