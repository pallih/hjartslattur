# coding: utf-8

import requests
from lxml import etree
import lxml.html
import datetime

last_run = datetime.datetime.now()

ships_in_port_url = 'http://www.112.is/Stat/StatsService.asmx/RepPolice'

post_data = {"Content-Length": 0}
r = requests.post(ships_in_port_url, post_data)
xml = r.content.encode('utf-8')
police_reports_24_hours = []
parser = etree.XMLParser()
tree = etree.XML(xml, parser)
for node in tree.iter('{http://tempuri.org/}RepPolice'):
    police_reports = {}
    for item in node.iter('{http://tempuri.org/}CurrDate'):
        police_reports['Date'] = item.text #, item.nsmap
    for item in node.iter('{http://tempuri.org/}HourFrom'):
        police_reports['Hour from'] = item.text
    for item in node.iter('{http://tempuri.org/}HourTo'):
        police_reports['Hour to'] = item.text
    for item in node.iter('{http://tempuri.org/}Police'):
        police_reports['Police_reports'] = item.text
    police_reports_24_hours.append(police_reports)
print police_reports_24_hours