from pymysql import *
import pymysql

if __name__ == "__main__":
    connection = pymysql.connect(host='localhost', user='root', password='nguyen0612', db='NewsCollection', 
                            cursorclass=pymysql.cursors.DictCursor)
    print("Connection establish!")  
    try:
        with connection.cursor() as cursor:
            # SQL
            sql = "SELECT * FROM Author "
            # Thực thi câu lệnh truy vấn (Execute Query).
            cursor.execute(sql)
            print("cursor.description: ", cursor.description)
            
            print()
            try:
                sql = "INSERT INTO Author "\
                        +"VALUES (%s, %s, %s) "
                cursor.execute(sql,("nhat tung","con cac nung lon",1223))
                connection.commit()
            except:
                pass

            # SQL
            sql = "SELECT * FROM Author "
            # Thực thi câu lệnh truy vấn (Execute Query).
            cursor.execute(sql)
                
        for row in cursor:
            print(row,type(row))
    finally:
        # Đóng kết nối (Close connection).
        connection.close()