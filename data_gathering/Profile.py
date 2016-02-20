import os
from bs4 import BeautifulSoup

FULL_NAME_CLASS = "vcard-fullname"
USERNAME_CLASS = "vcard-username"
CONTRIBURIONS_COUNT_CLASS = "contrib-number"
VCARD_STATS_CLASS = "vcard-stat-count"



def thousand_check(args):
	if 'k' in args:
		args = args.replace('k', '')
		return int(float(args)*1000)
	elif ',' in args:
		args = args.replace(',', '')
		return int(args)
	else:
		return int(args)


class Profile(object):
	"""Github Profile"""
	def __init__(self, soup):
		self.soup = soup
		self.name = soup.find_all("div", class_= FULL_NAME_CLASS)[0].text
		self.username = soup.find_all("div", class_= USERNAME_CLASS)[0].text

		vcard_stats = soup.find_all("strong", class_= VCARD_STATS_CLASS)
		contribution_counts = soup.find_all("span", class_= CONTRIBURIONS_COUNT_CLASS)
		
		self.total_contributions =  thousand_check(contribution_counts[0].text.split(' ')[0])
		self.longest_streak = thousand_check(contribution_counts[1].text.split(' ')[0])
		self.current_streak = thousand_check(contribution_counts[2].text.split(' ')[0])
		self.followers = thousand_check(vcard_stats[0].text)
		self.starred = thousand_check(vcard_stats[1].text)
		self.following = thousand_check(vcard_stats[2].text)

		self.get_contributions_data()


	def get_contributions_data(self):
		cal = self.soup.find_all("svg", class_= 'js-calendar-graph-svg')
		if not len(cal)>0:
			self.contribution_data = None
			return

		cd = []
		days = self.soup.find_all("rect", class_= 'day')
		for day in days:
			d = (day['data-count'],day['data-date'])
			cd.append(d)
		
		self.contribution_data = cd
	def __str__(self):
		return "{ 'username': '%s', 'total_contributions' : '%s', 'longest_streak' : '%s', 'current_streak' : '%s', 'followers' : '%s', 'starred' : '%s', 'following' : '%s'}" \
		%(self.username, self.total_contributions, self.longest_streak, self.current_streak, self.followers, self.starred, self.following)
	
	def __repr__(self):
		return "{ 'username': '%s', 'total_contributions' : '%s', 'longest_streak' : '%s', 'current_streak' : '%s', 'followers' : '%s', 'starred' : '%s', 'following' : '%s'}" \
		%(self.username, self.total_contributions, self.longest_streak, self.current_streak, self.followers, self.starred, self.following)