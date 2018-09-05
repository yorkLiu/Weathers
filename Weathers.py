#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import requests
import json
import re
from lxml import etree
from Config import get_header, APIS, get_timestamp
from bs4 import BeautifulSoup
import codecs
open = codecs.open



city_id = '101270101'



def get_today_weather(city_id):
    """
    Get today's weather
    :return:
    """

    # init the headers
    headers = get_header()

    today_API = APIS['today']

    url = today_API['url'].format(timestamp=get_timestamp(), city_id=city_id)

    # init the extra headers
    if today_API.has_key('extra_headers') and type(today_API['extra_headers']) is dict:
        headers.update(today_API['extra_headers'])

    r = requests.get(url, headers=headers)
    if r.status_code == 200:
        print r.content
        data = parseToJson(r.content)[0]
        print  data['cityname'], data['temp'], data['weather'], data['WD'],data['WS'], data['wse'], data['SD'], data['weathercode'], data['aqi'], data['aqi_pm25'], data['date']


json_patten = re.compile(r'=\s*(\{.*?\})')
def parseToJson(strContent):
    jsons = []
    json_data_array = re.findall(json_patten, strContent)
    for data in json_data_array:
        jsons.append(json.loads(data))

    return jsons


get_today_weather(city_id)