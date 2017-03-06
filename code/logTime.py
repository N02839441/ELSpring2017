#!/usr/bin/python 
import os
import time
import sqlite3 as mydb
import sys

def logTime():
	 #connect to database
     con = mydb.connect('/home/pi/Tests/testTime.db')
     with con:
                 cur = con.cursor()
                 #get current Date
                 currentDate=time.strftime('%Y-%m-%d')
                 #get current time
                 currentTime=time.strftime('%H-%M-%S')
                 #insert current date and current time to tempData table
                 cur.execute('insert into TempData(xDate,xTime) values(?,?)', (currentDate,currentTime))
                 #commit the changes
                 con.commit()
                 #displays all data inside TempData tables
                 #cur.execute("SELECT * FROM TempData")
                 #for row in cur:
                 #    print(row)
                 return [currentDate,currentTime]
#print the current date and time that logged into the database
print logTime()



