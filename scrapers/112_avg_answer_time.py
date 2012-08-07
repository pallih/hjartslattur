# coding: utf-8

import requests
from lxml import etree
import lxml.html
import datetime

last_run = datetime.datetime.now()

ships_in_port_url = 'http://www.112.is/Stat/StatsService.asmx/AvgAnswerTimes'

post_data = {"Content-Length": 0}
r = requests.post(ships_in_port_url, post_data)
xml = r.content.encode('utf-8')
avg_answer_time_24_hours = []
parser = etree.XMLParser()
tree = etree.XML(xml, parser)
for node in tree.iter('{http://tempuri.org/}AvgAnswerTime'):
    answer_time = {}
    for item in node.iter('{http://tempuri.org/}CurrDate'):
        answer_time['Date'] = item.text #, item.nsmap
    for item in node.iter('{http://tempuri.org/}HourFrom'):
        answer_time['Hour from'] = item.text
    for item in node.iter('{http://tempuri.org/}HourTo'):
        answer_time['Hour to'] = item.text
    for item in node.iter('{http://tempuri.org/}AvgAnswerTimeInSec'):
        answer_time['Avg_answer_time_sec'] = item.text
    avg_answer_time_24_hours.append(answer_time)
print avg_answer_time_24_hours