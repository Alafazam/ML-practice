import os
from bs4 import BeautifulSoup

FULL_NAME_CLASS = "vcard-fullname"
USERNAME_CLASS = "vcard-username"
CONTRIBURIONS_COUNT_CLASS = "contrib-number"
VCARD_STATS_CLASS = "vcard-stat-count"

class Profile(object):
	"""Github Profile"""
	def __init__(self, soup):
		self.soup = soup
		self.name = soup.find_all("div", class_= FULL_NAME_CLASS)[0].text
		self.username = soup.find_all("div", class_= USERNAME_CLASS)[0].text

		vcard_stats = soup.find_all("strong", class_= VCARD_STATS_CLASS)
		contribution_counts = soup.find_all("span", class_= CONTRIBURIONS_COUNT_CLASS)
		
		self.total_contributions =  contribution_counts[0].text.split(' ')[0]
		self.longest_streak = contribution_counts[1].text.split(' ')[0]
		self.current_streak = contribution_counts[2].text.split(' ')[0]
		self.followers = vcard_stats[0].text
		self.starred = vcard_stats[1].text
		self.following = vcard_stats[2].text

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
		return "{ 'name': '%s', 'username': '%s', 'total_contributions' : '%s', 'longest_streak' : '%s', 'current_streak' : '%s', 'followers' : '%s', 'starred' : '%s', 'following' : '%s'}" \
		%(self.name, self.username, self.total_contributions, self.longest_streak, self.current_streak, self.followers, self.starred, self.following)
	
	def __repr__(self):
		return "{ 'name': '%s', 'username': '%s', 'total_contributions' : '%s', 'longest_streak' : '%s', 'current_streak' : '%s', 'followers' : '%s', 'starred' : '%s', 'following' : '%s'}" \
		%(self.name, self.username, self.total_contributions, self.longest_streak, self.current_streak, self.followers, self.starred, self.following)