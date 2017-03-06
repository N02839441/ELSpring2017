#!/usr/bin/python
import os
import time
import sqlite3 as mydb
import sys

""" Log Current Time, Temperature in Celsius and Fahrenheit
     To an Sqlite3 database """

def readTemp():
     tempfile = open("/sys/bus/w1/devices/28-00044a3d8eff/w1_slave")
     tempfile_text = tempfile.read()
     currentTime=time.strftime('%x %X %Z')
     tempfile.close()
     tempC=float(tempfile_text.split("\n")[1].split("t=")[1])/1000
     tempF=tempC*9.0/5.0+32.0
     return [currentTime, tempC, tempF]

def logTemp():
     con = mydb.connect('/home/pi/Tests/temperature.db')
     with con:
         try:
             [t,C,F]=readTemp()
             print "Current temperature is: %s F" %F
             cur = con.cursor()
             #sql = "insert into TempData values(?,?,?)"
             cur.execute('insert into TempData values(?,?,?)', (t,C,F))
             print "Temperature logged"
         except:
             print "Error!!"


#print readTemp()
logTemp()

### RUN THE FOLLOWING CODE IN TERMINAL LINE TO LOG TEMPERATURE EVERY 30S AND AFTER 10 MINUTE USE CTRL + C TO EXIT
# while true ; do sudo python logTemperature.py & sleep 30; done