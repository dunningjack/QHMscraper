from lxml import html
import requests
from time import datetime


page = requests.get('https://www.royalnavy.mod.uk/qhm/portsmouth/shipping-movements/daily-movements?date=' + datetime.date)