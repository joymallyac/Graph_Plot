#@Jchakra
import codecs
from bs4 import BeautifulSoup 
import re
import os,glob
import csv

path = 'C:/Users/jchakra/Downloads/profiles/dl'

fp = open('Webscrap.csv', 'w' , newline='')
myFile = csv.writer(fp)
column_names = ['UserId','Organizations','Number_Of_Organizations','Bio','URL']
myFile.writerow(column_names)

for infile in glob.glob (os.path.join(path, '*.*')):
	print ("current file is" + infile)
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
		str = ""
		length = len(h2)
		for a in (h2):			
			str = str + a['href']
		myFile.writerow([uname.text,str,length,biostr,urlstr])					  							
	else:
		myFile.writerow([uname.text,'None','0',biostr,urlstr])			
fp.close()

