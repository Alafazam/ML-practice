import os
from bs4 import BeautifulSoup

FULL_NAME_CLASS = "vcard-fullname"
USERNAME_CLASS = "vcard-username"




cwd = os.getcwd()

user_profiles_dir = os.path.join(cwd,'crawled','users')

# get list of all files

files = os.listdir(user_profiles_dir)

# print files
files = files[:5]

for f in files:
	read = open(os.path.join(user_profiles_dir,f),'r').read()
	# print read
	soup = BeautifulSoup(read, 'html.parser')
	# print soup.title.string
	# 
	name =  soup.find_all("div", class_= FULL_NAME_CLASS)[0].text
	username = soup.find_all("div", class_= USERNAME_CLASS)[0].text