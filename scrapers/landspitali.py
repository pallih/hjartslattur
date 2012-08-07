#!/usr/bin/env python
# -*- coding: utf-8 -*-
import lxml.html
import time
import datetime
import requests

url = 'http://landspitali.is'

def landspitali():
	html = requests.get(url).text
	root = lxml.html.fromstring(html)
	space = ' '
	strings = root.xpath('//div[@class="activityNumbers activityNumbersNew"]')
	for s in strings:
		record = {}
		record['date'] = time.strftime("%d.%m.%Y", time.gmtime())
		record['time'] = time.strftime("%H:%M", time.gmtime())
		for d in s[1:]:
			record[d.attrib['class']] =  d[1].text
	return record
