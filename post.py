import urllib.parse
import random
import js2py
import requests
import json
from requests.structures import CaseInsensitiveDict
from py.blowfish import blowfish

#URL from Berhard-Gaul
url = "https://www.bernhard-gaul.de/spiele/reaktion/reaktion.php"
headers = CaseInsensitiveDict()
headers["Content-Type"] = "application/x-www-form-urlencoded"
class postTime:
    def __init__(self,username,timeMS):
        self.username = username
        self.timeMS = timeMS
    def getKey(x):
        keyRaw = str(requests.Session().get('http://bernhard-gaul.de/spiele/reaktion/reaktion.php').cookies.get_dict())
        keyRaw = keyRaw.replace("'",'"')
        keyRaw = json.loads(keyRaw)
        keyP = keyRaw["Schl"]
        return keyP
    def remark(x):
        if(x.timeMS < 100):
            responseString="Extrem!Zeit nur in Lev2 einzutragen!"
        if x.timeMS >= 100 and x.timeMS < 200:
            responseString="Super reagiert!"
        if(x.timeMS >=200 and x.timeMS < 300):
            responseString="Gut reagiert!"
        if(x.timeMS >=300 and x.timeMS < 450):
            responseString="Durchschnittliche Reaktionszeit"
        if(x.timeMS >= 450 and x.timeMS < 600):
            responseString="Unterdurchschnittliche Reaktionszeit"
        if(x.timeMS >= 600 and x.timeMS < 1000):
            responseString="Hast Du Alkohol getrunken?"
        if(x.timeMS >= 1000):
            responseString="Bist Du eingeschlafen?"
        return urllib.parse.quote_plus(responseString)
    def encrypt(x):
        return urllib.parse.quote_plus(blowfish.encrypt(x.getKey(),str(x.timeMS/1000)))      
    def send(self):
        data = "nzeit="+str(self.timeMS/1000)+"&nkommentar="+self.remark()+"&user="+self.username+"&nhidden="+self.encrypt()+"&nfp="+str(random.randint(1000000000,9999999999))+"&submitprompt=ja"
        resp = requests.post(url, headers=headers, data=data)
        print(resp.status_code)
