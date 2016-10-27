import sqlite3
import os

class Resources:
    conn = None
    cursor = None
    dbName = "./data.db"

    @staticmethod
    def getConn():
        if Resources.conn == None:
            path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), Resources.dbName)
            print(path)
            Resources.conn = sqlite3.connect(path)
        return Resources.conn

    @staticmethod
    def getCursor():
        if Resources.cursor == None:
            Resources.cursor = Resources.getConn().cursor()
        return Resources.cursor
    
    @staticmethod
    def commit():
        Resources.getConn().commit()
