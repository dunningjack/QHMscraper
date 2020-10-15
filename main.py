import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import datetime

file_name = 'data.txt'

today = datetime.date.today()
tomorrowdate = datetime.datetime.today() + datetime.timedelta(days=1)
tomorrow = tomorrowdate.strftime("%d/%m/%y")
url = 'https://www.royalnavy.mod.uk/qhm/portsmouth/shipping-movements/daily-movements?date=' + tomorrow

page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')
tables = soup.find("table")
vessel_list = tables.text

with open(file_name, 'w') as fh:
    fh.write(vessel_list)
fh.close()


def get_line_number():
    with open(file_name) as f:
        for i, line in enumerate(f, 1):
            if "HMS" in line:
                return i - 1



HMSLine = get_line_number()
TimeLine = HMSLine - 1

f = open('data.txt')
lines = f.readlines()

VesselName = lines[HMSLine]
VesselTime = lines[TimeLine]

print(VesselName, VesselTime)