# -*- coding: utf-8 -*-
import twitter
import requests
import re

def gettext(id):
	page1 = requests.get('http://t.co/%s' % id)
	t = re.findall('<textarea id=".*?" .*?>(.*?)</textarea>',page1.text,re.S)
	f = open(id + '.txt','w')
	if len(t) > 0:
		f.write(t[0])
	f.close()
file = open('spider.txt', 'w')
api = twitter.Api(consumer_key='LHHL6A3TbtspuYyyZzGfZxVlX', 
consumer_secret='z2cvLoPROQeb1YhmDUHPROgY7NN9cXRJY2ZfN5WxYDLnSoK4W2', 
access_token_key='3318355362-p3FYuDgyIPu6DdrrWTDhhE41r740k8nw3qzj7l0', 
access_token_secret='p2lCjfZznPXMTwclLvL6cL0zDcaVeTcaqnozxnMW5J1pi')
tweets = []
tweets = usertimelines = api.GetUserTimeline(screen_name = 'PastebinLeaks', count = 200)
id1 = tweets[-1].id - 1
while len(usertimelines) > 0:
	usertimelines = api.GetUserTimeline(screen_name = 'PastebinLeaks', max_id = id1, count = 200)
	tweets.extend(usertimelines)
	id1 = usertimelines[-1].id - 1
index = 0
for tweet in tweets:
	index += 1
	text = tweet.text
	s = text.split('http://t.co/')
	title = s[0]
	id = s[1]
	s = id.split(' #')
	id = s[0]
	file.write(title + '\t' + id + '\n')
	#gettext(id)
print(index)
file.close()