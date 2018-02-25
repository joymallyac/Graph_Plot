#@Author Jchakra
import MySQLdb
import csv
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pymysql
import os
#import config(I am not using config file anymore)

# Open database connection taking credentials from config file

# def connect_db(dbname):
#     if dbname != config.DATABASE_CONFIG['dbname']:
#         raise ValueError("Couldn't not find DB with given name")
#     conn = pymysql.connect(host=config.DATABASE_CONFIG['host'],
#                            user=config.DATABASE_CONFIG['user'],
#                            password=config.DATABASE_CONFIG['password'],
#                            port=config.DATABASE_CONFIG['port'],
#                            db=config.DATABASE_CONFIG['dbname'])
#     return conn

# db = connect_db('ghtorrent')

# Open database connection taking credentials from environment variable

username = os.environ["MYSQL_USERNAME"]
password = os.environ["MYSQL_PASSWORD"]

db = MySQLdb.connect("eb2-2291-fas01.csc.ncsu.edu",username,password,"ghtorrent",4747 )

# prepare a cursor object using cursor() method

cur = db.cursor()

query = ("select pc.merger_closer_gender as merger_closer_gender,    pc.gender as creator_gender,    count(1) as total,    count(if(pc.state = 'merged', 1, null)) as merged,    count(if(pc.state = 'closed', 1, null)) as closed, format(0.0 + count(if(pc.state = 'merged', 1, null))/count(1), 4) as percent_merged   from g_pull_closes2 pc  where pc.gender in ('Male', 'Female') and pc.merger_closer_gender in ('Male', 'Female')  and pc.state in ('merged', 'closed', 'open')  and pc.creator_id <> pc.merger_closer_id   and creator_type = 'Outsider' group by pc.gender, merger_closer_gender order by pc.merger_closer_gender, pc.gender ")

cur.execute(query)

rows = cur.fetchall()
column_names = [i[0] for i in cur.description]
fp = open('Tug_of_war.csv', 'w' , newline='')
myFile = csv.writer(fp)
myFile.writerow(column_names)
myFile.writerows(rows)
fp.close()

# Closing database connection
cur.close()
db.close()

#---------Creating Graph---------------------

# Reading the .csv file
df = pd.read_csv('Tug_of_war.csv')

# Printing data
print(df)

# Grouping Female and Male data separately
female_merger = (df['percent_merged'].groupby(df['creator_gender']).head()[0],df['percent_merged'].groupby(df['creator_gender']).head()[2])
male_merger = (df['percent_merged'].groupby(df['creator_gender']).head()[1],df['percent_merged'].groupby(df['creator_gender']).head()[3])
 
# data to plot
n_groups = 2
 
# create plot
fig, ax = plt.subplots()
index = np.arange(n_groups)
bar_width = 0.25
opacity = 0.8
female_color = '#009E73'
male_color = '#E69F00'
 
rects1 = plt.bar(index, female_merger, bar_width,
                 alpha=opacity,
                 color=female_color,
                 label='Female')
 
rects2 = plt.bar(index + bar_width, male_merger, bar_width,
                 alpha=opacity,
                 color=male_color,
                 label='Male')
 
plt.rcParams.update({'font.size': 30})
plt.yticks(fontsize=25)
plt.ylim(ymin=0.6)
plt.xlabel('Merger or Closer',fontsize=30)
plt.ylabel('Avg Merging Rate',fontsize=30)
#plt.title('Tug of War',fontsize=30)
plt.xticks(index + bar_width/2 , ('Female', 'Male'),fontsize=30)
plt.legend()
 
plt.tight_layout()
plt.show()
