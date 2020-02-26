import api
import json
import httplib2
import configparser
from oauth2client.service_account import ServiceAccountCredentials

config = configparser.ConfigParser()
config.read("settings.ini")
sheet_id = config['zadarma']['sheetid']
key = config["zadarma"]["key"]
secret = config["zadarma"]["secret"]


def meth(n):
    ncount = 0
    ncountk = 0
    nsec = 0
    nseck = 0
    for i in range(len(d)):
        dd = d[i]
        sip = dd['sip']
        sec = dd['seconds']
        if sip == n:
            ncount += 1
            nsec += sec
            if sec >= k:
                ncountk += 1
                nseck += sec
    return ncount, nsec, ncountk, nseck


def authg():
    credential_file = 'creds.json'
    credencials = ServiceAccountCredentials.from_json_keyfile_name(
        credential_file,
        ['https://www.googleapis.com/auth/spreadsheets'
         'https://www.googleapis.com/auth/drive'])
    httpauth = credencials.authorize(httplib2.Http())
    service = apiclient.discovery.build('sheets', 'v4', http=httpauth)
    return service


k = input()  # ввод k секунд
z_api = api.ZadarmaAPI(key=key, secret='SECRET')
res = z_api.call('/v1/statistics/pbx/', format='json')
data = json.loads(res)  # словарь из json строки
d = data['stats']
i = 1
authg()
for n in range (100, 199):
    ncount, nsec, ncountk, nseck = meth(n)

    values = authg.spreadsheets().values().bathUpdate(
        spreadsheetID=sheet_id,
        body={
            "valueInputOption": "USER_ENTERED",
            "data": [
                {"range": "A{}:E{}".format(i, i),
                 "majorDimension": "ROWS",
                 "values": [n, ncount, nsec, ncountk, nseck]}
            ]
        }
    ).execute()
    i+=1