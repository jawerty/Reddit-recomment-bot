import praw
import json
import urllib2
import password as password
from BeautifulSoup import BeautifulSoup

r = praw.Reddit(user_agent="user /u/original-comment-bot")
#r.login('original-comment-bot', password.getPassword())
subreddit = r.get_subreddit('funny')
for submission in subreddit.get_hot(limit=10):
	try:
		soup = BeautifulSoup(urllib2.urlopen('http://www.reddit.com/search?q=url:'+submission.url).read())
	except urllib2.HTTPError, e:
		soup = None

	if str(soup).find("") >= 0:
		print "not a repost"
	else:
		print "repost"

	print submission.url

	print '\n'