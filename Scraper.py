import requests
import pandas as pd
import datetime
import lxml
from textmagic.rest import TextmagicRestClient

username = "your_textmagic_username"
token = "your_apiv2_key"
client = TextmagicRestClient(username, token)


today = datetime.date.today()
tomorrowdate = datetime.datetime.today() + datetime.timedelta(days=1)
tomorrow = tomorrowdate.strftime("%d/%m/%y")
url = 'https://www.royalnavy.mod.uk/qhm/portsmouth/shipping-movements/daily-movements?date=' + tomorrow

page = requests.get(url)
MovementTable = pd.read_html(url)
numberofdf = len(MovementTable)
df1 = MovementTable[0]


ShipTime = []
Vessel = []
movingFrom = []
movingTo = []

dfn = df1
dfn.Time = df1.Time.astype(str)

for entries in (dfn.Ser -1):
    if "MV" not in dfn.at[entries, 'Ship']:
        ShipTime.append(dfn.at[entries, 'Time'])
        Vessel.append(dfn.at[entries, 'Ship'])
        movingFrom.append(dfn.at[entries, 'From'])
        movingTo.append(dfn.at[entries, 'To'])
    else:
        entries += 1

texttosend = []

for i in range(0, (len(Vessel))):
    texttosend = Vessel[i] + " is moving from " + movingFrom[i] + " to " + movingTo[i] + " at " + ShipTime[i] + "\n")

message = client.messages.create(phones="9990001001", text=)