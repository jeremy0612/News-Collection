import pymysql
from pymysql import * 


def CONNECT(host_, user_, password_, db_):
    try:
        connection = pymysql.connect(host=host_, user=user_, password=password_, db=db_, 
                                cursorclass=pymysql.cursors.DictCursor, local_infile=True)
        print("Connection establish!")
        return connection
    except:
        print("Connection fail!")

def QUERY(connection,script):
    with connection.cursor() as cursor:
        cursor.execute(script)
        connection.commit()
        
        print("cursor.description: ", cursor.description)
        return cursor.fetchall()
        '''
        # Process the results
        for row in results:
            # Do something with the row data
            print(row)
        '''