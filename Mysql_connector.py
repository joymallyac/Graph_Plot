#@Author Jchakra
import mysql.connector
import csv
#import pandas as pd
#import socket


conn = mysql.connector.connect(
         user='',
         password='',
         host='',
         port='',
         database='',
         buffered = True)

cur = conn.cursor()

query = ("select pc.merger_closer_gender as merger_closer_gender,    pc.gender as creator_gender,    count(1) as total,    count(if(pc.state = 'merged', 1, null)) as merged,    count(if(pc.state = 'closed', 1, null)) as closed, format(0.0 + count(if(pc.state = 'merged', 1, null))/count(1), 4) as percent_merged   from g_pull_closes2 pc  where pc.gender in ('Male', 'Female') and pc.merger_closer_gender in ('Male', 'Female')  and pc.state in ('merged', 'closed', 'open')	 and pc.creator_id <> pc.merger_closer_id   and creator_type = 'Outsider' group by pc.gender, merger_closer_gender order by pc.merger_closer_gender, pc.gender ")

cur.execute(query)

#data = cur.fetchone();
#print(data);

rows = cur.fetchall()
#column_names = [i[0] for i in cur.description]
fp = open('C:/Users/jchakra/Desktop/file.csv', 'w')
myFile = csv.writer(fp)
#myFile.writerow(column_names)
myFile.writerows(rows)
fp.close()

#for (id, name, dept, salary) in cur:
 # print("{}, {}, {}, {}".format(id, name,dept,salary))

cur.close()
conn.close()

