from flask import Flask, render_template
from bs4 import BeautifulSoup
import requests
import json
import sys 
import re
import numpy as np
from datetime import datetime, date, time
import mapping as city
BASE_URL="https://www.makemytrip.com/"
def get_random_ua():
    random_ua = ''
    ua_file = 'ua_file.txt'
    try:
        with open(ua_file) as f:
            lines = f.readlines()
        if len(lines) > 0:
            prng = np.random.RandomState()
            index = prng.permutation(len(lines) - 1)
            idx = np.asarray(index, dtype=np.integer)[0]
            random_proxy = lines[int(idx)]
    except Exception as ex:
        print('Exception in random_ua')
        print(str(ex))
    finally:
        return random_ua
def get_data(url):
    print(url)
    USer_agent=get_random_ua()
    headers = {
        'user-agent': user_agent,
    }
    source = requests.get(url,headers=headers).text

    soup = BeautifulSoup(source, 'lxml')

    print(soup)
    #head = soup.find('main').select_one('article:nth-of-type(4)').div.text
    #print(head)
    #author = soup.find('main').select_one('p').text
    #print(author)
def journey_roundtrip(origin, destination, depart_date, return_date, adult=1, children=0, infant=0):
        new_url = BASE_URL + 'flight/search?itinerary=' + origin+'-'+destination +'-'+depart_date+'_'+ destination+'-'+origin+'-'+return_date+'&tripType=R&paxType=A-'+str(adult)+'_C-'+str(children)+'_I-'+str(infant)+'&intl=false&cabinClass=E'
        return new_url
if __name__=="__main__":
    #print sys.argv[0], sys.argv[1], sys.argv[2]
    origin = "MAA"
    destination = "CCJ"
    j_date = date.today()
    j_date = str(j_date.day) + "/" + str(j_date.month) + "/" + str(j_date.year)
    e_date = date.today()
    e_date = str(e_date.day) + "/" + str(e_date.month) + "/" + str(e_date.year)
    for i in range(len(sys.argv)):
        if i == 1:
            tmp = sys.argv[1].lower()
            origin = city.city_code[tmp]
        if i == 2:
            tmp = sys.argv[2].lower()
            destination = city.city_code[tmp]
        if i == 3:
            j_date = sys.argv[3]
        if i == 4:
            e_date = sys.argv[4]
    print("="*30)
    #bro = MakeMyTrip()
    
    # To print on console
    #bro.print_json(bro.journey_oneway(origin,destination,"12-12-2014"))
    
    # To return the JSON response from roundtrip API
    print(j_date,e_date)
    url = journey_roundtrip(origin, destination, str(j_date), str(e_date))
    get_data(url)
    # print temp_jsn
    # for x in range(len(temp_jsn['departureFlights'])):
    #     revised_rate = temp_jsn['departureFlights'][x]['raf'] if temp_jsn['departureFlights'][x]['raf'] != 0.0 else temp_jsn['departureFlights'][x]['af']
    #     print temp_jsn['departureFlights'][x]['fi'], revised_rate, temp_jsn['departureFlights'][x]['td']
    # print 
    #print temp_jsn['departureFlights'][1]['td']
