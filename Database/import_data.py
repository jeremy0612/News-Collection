import pymysql
from pymysql import * 


def CONNECT(host_, user_, password_, db_):
    try:
        connection = pymysql.connect(host=host_, user=user_, password=password_, db=db_, 
                                cursorclass=pymysql.cursors.DictCursor)
        print("Connection establish!")
        return connection
    except:
        print("Connection fail!")

def QUERY(script):
    cursor.execute(script)
    print("cursor.description: ", cursor.description)
