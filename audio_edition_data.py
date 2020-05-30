from fireo.fields import IDField, TextField
from fireo.models import Model
import fireo


class Edition(Model):
    id = IDField()
    language = TextField()
    name = TextField()
    english_name = TextField()
    type = TextField()

    class Meta:
        to_lowercase = True
        collection_name = "editions"

data = [
{
"id": "ar.abdulbasitmurattal",
"language": "ar",
"name": "عبد الباسط عبد الصمد المرتل",
"english_name": "Abdul Basit",
"format": "audio",
"type": "translation",
"direction": None
},
{
"id": "ar.abdullahbasfar",
"language": "ar",
"name": "عبد الله بصفر",
"english_name": "Abdullah Basfar",
"format": "audio",
"type": "versebyverse",
"direction": None
},
{
"id": "ar.abdurrahmaansudais",
"language": "ar",
"name": "عبدالرحمن السديس",
"english_name": "Abdurrahmaan As-Sudais",
"format": "audio",
"type": "versebyverse",
"direction": None
},
{
"id": "ar.abdulsamad",
"language": "ar",
"name": "عبدالباسط عبدالصمد",
"english_name": "Abdul Samad",
"format": "audio",
"type": "versebyverse",
"direction": None
},
{
"id": "ar.shaatree",
"language": "ar",
"name": "أبو بكر الشاطري",
"english_name": "Abu Bakr Ash-Shaatree",
"format": "audio",
"type": "versebyverse",
"direction": None
},
{
"id": "ar.ahmedajamy",
"language": "ar",
"name": "أحمد بن علي العجمي",
"english_name": "Ahmed ibn Ali al-Ajamy",
"format": "audio",
"type": "versebyverse",
"direction": None
},
{
"id": "ar.alafasy",
"language": "ar",
"name": "مشاري العفاسي",
"english_name": "Alafasy",
"format": "audio",
"type": "versebyverse",
"direction": None
},
{
"id": "ar.hanirifai",
"language": "ar",
"name": "هاني الرفاعي",
"english_name": "Hani Rifai",
"format": "audio",
"type": "versebyverse",
"direction": None
},
{
"id": "ar.husary",
"language": "ar",
"name": "محمود خليل الحصري",
"english_name": "Husary",
"format": "audio",
"type": "versebyverse",
"direction": None
},
{
"id": "ar.husarymujawwad",
"language": "ar",
"name": "محمود خليل الحصري (المجود)",
"english_name": "Husary (Mujawwad)",
"format": "audio",
"type": "versebyverse",
"direction": None
},
{
"id": "ar.hudhaify",
"language": "ar",
"name": "علي بن عبدالرحمن الحذيفي",
"english_name": "Hudhaify",
"format": "audio",
"type": "versebyverse",
"direction": None
},
{
"id": "ar.ibrahimakhbar",
"language": "ar",
"name": "إبراهيم الأخضر",
"english_name": "Ibrahim Akhdar",
"format": "audio",
"type": "versebyverse",
"direction": None
},
{
"id": "ar.mahermuaiqly",
"language": "ar",
"name": "ماهر المعيقلي",
"english_name": "Maher Al Muaiqly",
"format": "audio",
"type": "versebyverse",
"direction": None
},
{
"id": "ar.minshawi",
"language": "ar",
"name": "محمد صديق المنشاوي",
"english_name": "Minshawi",
"format": "audio",
"type": "translation",
"direction": None
},
{
"id": "ar.minshawimujawwad",
"language": "ar",
"name": "محمد صديق المنشاوي (المجود)",
"english_name": "Minshawy (Mujawwad)",
"format": "audio",
"type": "translation",
"direction": None
},
{
"id": "ar.muhammadayyoub",
"language": "ar",
"name": "محمد أيوب",
"english_name": "Muhammad Ayyoub",
"format": "audio",
"type": "versebyverse",
"direction": None
},
{
"id": "ar.muhammadjibreel",
"language": "ar",
"name": "محمد جبريل",
"english_name": "Muhammad Jibreel",
"format": "audio",
"type": "versebyverse",
"direction": None
},
{
"id": "ar.saoodshuraym",
"language": "ar",
"name": "سعود الشريم",
"english_name": "Saood bin Ibraaheem Ash-Shuraym",
"format": "audio",
"type": "versebyverse",
"direction": None
},
{
"id": "en.walk",
"language": "en",
"name": "Ibrahim Walk",
"english_name": "Ibrahim Walk",
"format": "audio",
"type": "versebyverse",
"direction": None
},
{
"id": "fa.hedayatfarfooladvand",
"language": "fa",
"name": "Fooladvand - Hedayatfar",
"english_name": "Fooladvand - Hedayatfar",
"format": "audio",
"type": "translation",
"direction": None
},
{
"id": "ar.parhizgar",
"language": "ar",
"name": "شهریار پرهیزگار",
"english_name": "Parhizgar",
"format": "audio",
"type": "versebyverse",
"direction": None
},
{
"id": "ur.khan",
"language": "ur",
"name": "Shamshad Ali Khan",
"english_name": "Shamshad Ali Khan",
"format": "audio",
"type": "versebyverse",
"direction": None
},
{
"id": "zh.chinese",
"language": "zh",
"name": "中文",
"english_name": "Chinese",
"format": "audio",
"type": "versebyverse",
"direction": None
},
{
"id": "fr.leclerc",
"language": "fr",
"name": "Youssouf Leclerc",
"english_name": "Youssouf Leclerc",
"format": "audio",
"type": "versebyverse",
"direction": None
},
{
"id": "ar.aymanswoaid",
"language": "ar",
"name": "أيمن سويد",
"english_name": "Ayman Sowaid",
"format": "audio",
"type": "versebyverse",
"direction": None
}
]

edition_batch = fireo.batch()

for e in data:

    edition = Edition()
    edition.id = e["id"]
    edition.language = e["language"]
    edition.name = e["name"]
    edition.english_name = e["english_name"]
    edition.type = 'Audio'
    edition.save(batch=edition_batch)


edition_batch.commit()