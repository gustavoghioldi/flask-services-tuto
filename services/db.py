import sqlite3

class DBConnection:
    def __init__(self) -> None:
        self.__conn = sqlite3.connect("./persons.sqlite3")
        self.__cursor = self.__conn.cursor()

    def excecute_sql(self, sql_script:str):
        self.__cursor.execute(sql_script)
        self.__conn.commit()
    
    def get_cursor(self):
        return self.__cursor
        
    def close_connection(self):
        self.__conn.close()