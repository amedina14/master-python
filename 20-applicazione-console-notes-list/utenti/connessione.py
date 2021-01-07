import mysql.connector

def connettere():
    database = mysql.connector.connect(
        host = "localhost",
        user = "root",
        passwd = "",
        port = 3308,
        database = "master_python"
    )
    #print(database)
    cursor = database.cursor(buffered=True)

    return [database, cursor]