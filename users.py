import os
from bs4 import BeautifulSoup

FULL_NAME_CLASS = "vcard-fullname"
USERNAME_CLASS = "vcard-username"




cwd = os.getcwd()

user_profiles_dir = os.path.join(cwd,'crawled','users')

# get list of all files

files = os.listdir(user_profiles_dir)

# print files
files = files[:2]

for f in files:
	read = open(os.path.join(user_profiles_dir,f),'r').read()
	# print read
	soup = BeautifulSoup(read, 'html.parser')
	# print soup.title.string
	# 
	name =  soup.find_all("div", class_= FULL_NAME_CLASS)[0].text
	username = soup.find_all("div", class_= USERNAME_CLASS)[0].text
	print username,name

	cal = soup.find_all("svg", class_= 'js-calendar-graph-svg')
	
	if not len(cal)>0:
		continue

	days = soup.find_all("rect", class_= 'day')
	contribution_data = []
	for day in days:
		d = (day['data-count'],day['data-date'])
		contribution_data.append(d)
	print len(contribution_data)	
	print contribution_data[0]		
	

