from os import listdir
from os.path import isfile, join

import fireo
from models.edition import Edition
from models.translation import Translation


mypath = './data'
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

for single_file in onlyfiles:
    detail = single_file.replace('.txt', '')
    # print(detail)
    edition_id, language, name, translator, direction = detail.split('_')

    edition = Edition()
    edition.id = edition_id
    edition.language = language
    edition.name = name
    edition.translator = translator
    edition.type = 'Text'
    edition.format = 'translation'
    edition.direction = direction
    edition.save()

    file_location = './data/' + single_file
    f = open(file_location, "r")

    trans_batch = fireo.batch()
    count = 0
    line_count = 0

    for line in f:

        if not line.strip():
            print('file end')
            break

        # print(line)
        surah_number, ayat_number, *line_text = line.split('|')
        text = ' '.join(line_text)
        print('For File '+edition_id +
              ' writing line...' + str(line_count))
        line_count += 1

        trans_id = surah_number + '-' + ayat_number

        translation = Translation()
        translation.id = edition_id + "_" + trans_id
        translation.ayah_id = trans_id
        translation.edition_id = edition_id
        translation.text = text.strip()
        translation.save(batch=trans_batch)

        count += 1

        if(count >= 400):
            trans_batch.commit()
            count = 0

    print('============Complete=============================')
    trans_batch.commit()
