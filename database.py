import mysql.connector

config = {
    'user' : 'root',
    'password' :'12101996',
    'host':'localhost',
    'database':'acme'
}

db = mysql.connector.connect(**config)
cursor = db.cursor()
