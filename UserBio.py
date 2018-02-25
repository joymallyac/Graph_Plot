#@Jchakra
import codecs
from bs4 import BeautifulSoup 
import re
import os,glob
import csv
import string

#return ''.join([i if ord(i) < 128 else ' ' for i in text])
def remove_non_ascii(text):
	new_txt = ""
	for c in text:
		if 0 >= ord(c) or ord(c) >= 127:			
			new_txt = new_txt + "@"
		else:
			new_txt = new_txt + c			
	return new_txt


#path = 'F:/genderedprofiles-26Jan'
path = 'C:/Users/jchakra/Downloads/profiles/dl'


fp = open('UserBio.csv', 'w' , newline='')
myFile = csv.writer(fp)
column_names = ['login','bio','url','company','location']
myFile.writerow(column_names)
print("My Program Starts")
for infile in glob.glob (os.path.join(path, '*.*')):	
	try:
		f=codecs.open(infile,'r',encoding="utf8")	
		soup = BeautifulSoup(f, "lxml")
		bio = soup.find_all("div", class_="p-note user-profile-bio")
		uname = soup.find("span", class_="p-nickname vcard-username d-block")
		org = soup.find("span", class_="p-org")
		location = soup.find("span", class_="p-label")			
		if uname == None:
			continue	
		biostr = ""
		for res in bio:
			biostr = biostr + res.text			
		url = soup.find_all("a", class_="u-url")	
		urlstr = ""
		for u in url:
			urlstr = urlstr + u['href']
		orgstr =""
		if org != None:
			orgstr = org.text
		locationstr = ""
		if location != None:
			locationstr = location.text		
		locationstr = remove_non_ascii(locationstr)
		orgstr = remove_non_ascii(orgstr)
		biostr = remove_non_ascii(biostr)		
		myFile.writerow([uname.text,biostr,urlstr,orgstr,locationstr])
	except:
		print("An exception occurred")
fp.close()

