
import sqlite3 as mydb
import sys

def output():
	 #connect to database
     con = mydb.connect('/home/pi/Tests/temperature.db')
     with con:
                 cur = con.cursor()
                 cur.execute("SELECT * FROM TempData")
                 for row in cur:
                     print(row)
output()


