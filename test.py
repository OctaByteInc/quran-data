lines = [
    "",
    "#=====================================================================",
    "#",
    "#  Quran Translation",
    "#  Name: Ahmed Raza Khan",
    "#  Translator: Ahmed Raza Khan",
    "#  Language: English",
    "#  ID: en.ahmedraza",
    "#  Last Update: July 17, 2011",
    "#  Source: Tanzil.net",
    "#",
    "#=====================================================================",
    ""
]

for line in lines:

    if not line.strip():
        continue

    if line[0] == '#':
        if "Name" in line:
            translator_name = line.split(':')[1]
            print(translator_name)
        elif "Language" in line:
            language = line.split(':')[1]
            print(language)
        elif "ID" in line:
            edition_id = line.split(':')[1].strip()
            print(edition_id)
        else:
            continue
