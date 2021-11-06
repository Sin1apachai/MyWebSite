import psycopg2
import configparser
import os

class psqlHealper(self):
    def setConfig(self, value):
        config = configparser.ConfigParser()
        __config = config.read( os.path.dirname(__file__).replace("/psqlHelper", "/").replace("\psqlHelper", "\\") + "settings.conf" )
        return __config['DATABASE'][value]

    def __init__(self):
        self.user = self.setConfig('user')
        self.password = self.setConfig('password')
        self.host = self.setConfig('host')
        self.port = self.setConfig('port')
        self.database = self.setConfig('database')

    def connectionCreate(self):
        connection = psycopg2.connect(user=self.user,
                                        password=self.password,
                                        host=self.host,
                                        port=self.port,
                                        database=self.database)

    def listToString(dataList):
        result = ""
        for index in range (0, len(dataList)):
            if index == len(dataList) - 1:
                result += dataList[index]
            else:
                result += dataList[index] + ", "
        return result 

    def equalList(dataList):
        if len(dataList) < 2:
            try:
                raise Exception(dataList)
            except Exception:
                print("""Data Length isn't Equal 2 """)
                raise
        elif len(dataList) == 2:
            return " = ".join(dataList)
        else:
            return col = dataList[0] + " in " + str(tuple(dataList[1:]))

    def fetchQuery(self, query):
        try:
            connection = self.connectionCreate()
            cursor = connection.cursor()
            cursor.execute(query)
            datas = cursor.fetchall()
        except psycopg2.DatabaseError as error:
            print(error)
            datas = None

        cursor.close()
        connection.close()
        return datas

    def insertQuery(self, cols, value)
        try:
            connection = self.connectionCreate()
            cursor = connection.cursor()
            query =  " INSERT INTO " + table + "(" + self.dataList(cols) + ") VALUES (" + self.dataList(value) + ")"
            cursor.execute(query)
            connection.commit()
            print(cursor.rowcount + " rows: Insert Complete !!")
        except psycopg2.DatabaseError as error:
            print(error)
            connection.rollback()

        cursor.close()
        connection.close()

    def updateQuery(self, table, setData, condition=None):
        try:
            connection = self.connectionCreate()
            cursor = connection.cursor()
            cursor.execute("Update set " + table + self.equalList(setData) + if condition : "where " + self.equalList(condition) + ")"
            connection.commit()
            print(cursor.rowcount + " rows: Update Complete !!")
        except psycopg2.DatabaseError as error:
            print(error)
            datas = None

        cursor.close()
        connection.close()
        return datas

    def delQuery(self, table, condition=None):
        try:
            connection = self.connectionCreate()
            cursor = connection.cursor()
            query =  " DELETE FROM " + table + if condition : "where " + self.equalList(condition) + ")"
            cursor.execute(query)
            connection.commit()
            print(cursor.rowcount + " rows: Del Complete !!")
        except psycopg2.DatabaseError as error:
            print(error)
            connection.rollback()

        cursor.close()
        connection.close()