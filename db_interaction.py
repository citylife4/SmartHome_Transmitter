import sqlite3 as sql
from datetime import datetime

path_db = "/home/jdv/projects/website/SmartHome_PortoWeb/app/Database/database.db"


def insert_state(state):
    con = sql.connect(path_db, isolation_level=None)
    cur = con.cursor()
    with con:
        cur.execute('INSERT INTO palacoulo_garage_door (date, door_status) VALUES (?, ?)',
                    (datetime.now(), str(state)))
    con.close()
    return con, cur


def insert_porto_door(state):
    con = sql.connect(path_db, isolation_level=None)
    cur = con.cursor()
    with con:
        cur.execute('INSERT INTO porto_door_status (date, door_status) VALUES (?, ?)',
                    (datetime.now(),  str(state)))
    con.close()
    return con, cur
