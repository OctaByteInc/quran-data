import requests
import fireo
from models.ayah import Ayah
from models.surah import Surah


resp = requests.get('http://api.alquran.cloud/v1/ayah/1161')

data = resp.json()['data']

if type(data["sajda"]) is bool:
    is_sajda = data["sajda"]
else:
    is_sajda = True

print(is_sajda)