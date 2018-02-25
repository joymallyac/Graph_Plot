#@Jchakra
import codecs
from bs4 import BeautifulSoup 
import re
import os,glob
import csv

path = 'F:/genderedprofiles-26Jan'


fp1 = open('Org.csv', 'w' , newline='')
myFile1 = csv.writer(fp1)
column_names1 = ['loginName','organizations']
myFile1.writerow(column_names1)

fp2 = open('OrgLess.csv', 'w' , newline='')
myFile2 = csv.writer(fp2)
column_names2 = ['login']
myFile2.writerow(column_names2)

fp3 = open('Bio.csv', 'w' , newline='')
myFile3 = csv.writer(fp3)
column_names3 = ['login','bio','url']
myFile3.writerow(column_names3)
print("My Program Starts")
for infile in glob.glob (os.path.join(path, '*.*')):
	print (infile)
	try:
		f=codecs.open(infile,'r',encoding="utf8")	
		soup = BeautifulSoup(f, "lxml")
		bio = soup.find_all("div", class_="p-note user-profile-bio")
		uname = soup.find("span", class_="p-nickname vcard-username d-block")	
		if uname == None:
			continue	
		biostr = ""
		for res in bio:
			biostr = biostr + res.text
		url = soup.find_all("a", class_="u-url")	
		urlstr = ""
		for u in url:
			urlstr = urlstr + u['href']
		h2 = soup.find_all("a", class_="tooltipped tooltipped-n avatar-group-item")
		if len(h2) > 0:		
			length = len(h2)
			for a in (h2):			
				myFile1.writerow([uname.text,a['href']])
			myFile3.writerow([uname.text,biostr,urlstr])					  							
		else:
			myFile2.writerow([uname.text])
			myFile3.writerow([uname.text,biostr,urlstr])
	except:
		print("An exception occurred")
fp1.close()
fp2.close()
fp3.close()

