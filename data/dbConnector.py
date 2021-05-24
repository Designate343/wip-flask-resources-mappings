import mariadb 
import sys

def connectToDb():
    try:
        conn = mariadb.connect(
            user="root",
            password="root",
            host="127.0.0.1",
            port=3310,
            database="persons"
        )
        return conn
    except mariadb.Error as e:
        print(f"Error connecting to MariaDB Platform: {e}")
        #todo: throw internal server error or something like that
    except:
        e = sys.exc_info()[0]
        print (e)


