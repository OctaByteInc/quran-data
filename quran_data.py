import requests
import fireo
from models.ayah import Ayah
from models.surah import Surah


ayah_batch = fireo.batch()
ayah_count = 0

surah_batch = fireo.batch()
surah_count = 0
init_surah_number = 0


#6237

for n in range(1, 6237):
    resp = requests.get('http://api.alquran.cloud/v1/ayah/' + str(n))

    if resp.status_code == 200:

        print("Ayah Nunber Complete", n)

        data = resp.json()['data']

        ayah = Ayah()
        ayah.id = str(data["surah"]["number"]) + '-' + str(data["numberInSurah"])
        ayah.surah_id = str(data["surah"]["number"])
        ayah.number = data["number"]
        ayah.number_in_surah = data["numberInSurah"]
        ayah.juz = data["juz"]
        ayah.manzil = data["manzil"]
        ayah.ruku = data["ruku"]
        ayah.hizb_quarter = data["hizbQuarter"]

        if type(data["sajda"]) is bool:
            ayah.sajda = data["sajda"]
        else:
            ayah.sajda = True

        ayah.arabic = data["text"]

        ayah.save(batch=ayah_batch)
        ayah_count += 1

        if(ayah_count >= 400):
            ayah_batch.commit()
            ayah_count = 0

        if data["surah"]["number"] != init_surah_number:

            surah = Surah()
            surah.id = str(data["surah"]["number"])
            surah.number = data["surah"]["number"]
            surah.name = data["surah"]["name"]
            surah.english_name = data["surah"]["englishName"]
            surah.english_name_translation = data["surah"]["englishNameTranslation"]
            surah.number_of_ayahs = data["surah"]["numberOfAyahs"]
            surah.revelation_type = data["surah"]["revelationType"]

            surah.save(batch=surah_batch)
            surah_count += 1

        if(surah_count >= 400):
            surah_batch.commit()
            surah_count = 0

    else:
        print("unable to get data")

print('============Complete=============================')
ayah_batch.commit()
surah_batch.commit()