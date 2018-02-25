import csv
import MySQLdb
import pymysql
import os

username = os.environ["MYSQL_USERNAME"]
password = os.environ["MYSQL_PASSWORD"]

db = MySQLdb.connect("eb2-2291-fas01.csc.ncsu.edu",username,password,"ghtorrent",4747 )

# prepare a cursor object using cursor() method

cur = db.cursor()

f=open('C:/Users/jchakra/Downloads/UserBio.csv','r') # open the csv data file
next(f, None) # skip the header row
reader = csv.reader(f)

for row in reader:
	try:
		cur.execute("INSERT INTO ghtorrent_extension.user_bio VALUES (%s,%s,%s,%s,%s)", row)
	except:
		print("An exception occurred")		

f.close()
db.commit()
db.close()