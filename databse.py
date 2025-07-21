import mysql.connector
database = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="python",
    port=3308
)
print("Connection Established")
