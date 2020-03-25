from models.audio import Audio
from models.ayah import Ayah
from models.edition import Edition
from models.image import Image
from models.surah import Surah
from models.translation import Translation


# import data for Audio
audio = Audio()
audio = 'audio-ayah-1-edition-1'
audio.ayah_id = 'ayah-1'
audio.edition_id = 'edition-1'
audio.type = 'Translation'
audio.audio = 'Translation Audio for Ayah-1 Edition-1'
audio.save()

audio = Audio()
audio = 'audio-ayah-1-edition-2'
audio.ayah_id = 'ayah-1'
audio.edition_id = 'edition-2'
audio.type = 'Translation'
audio.audio = 'Translation Audio for Ayah-1 Edition-2'
audio.save()

audio = Audio()
audio = 'audio-ayah-1-edition-1'
audio.ayah_id = 'ayah-1'
audio.edition_id = 'edition-1'
audio.type = 'Arabic'
audio.audio = 'Translation Audio for Ayah-1 Edition-1'
audio.save()

audio = Audio()
audio = 'audio-ayah-2-edition-1'
audio.ayah_id = 'ayah-2'
audio.edition_id = 'edition-1'
audio.type = 'Translation'
audio.audio = 'Translation Audio for Ayah-2 Edition-1'
audio.save()

#import data for Ayah
ayah = Ayah()
ayah.id = 'ayah-1'
ayah.surah_id = 'surah-1'
ayah.number = 1
ayah.number_in_surah = 1
ayah.juz = 1
ayah.manzil = 1
ayah.ruku = 1
ayah.hizb_quarter = 1
ayah.sajda = False
ayah.arabic = 'Arabic for ayah-1'
ayah.save()

ayah = Ayah()
ayah.id = 'ayah-2'
ayah.surah_id = 'surah-1'
ayah.number = 2
ayah.number_in_surah = 2
ayah.juz = 1
ayah.manzil = 1
ayah.ruku = 1
ayah.hizb_quarter = 1
ayah.sajda = False
ayah.arabic = 'Arabic for ayah-2'
ayah.save()


# import data for edition
edition = Edition()
edition.id = 'edition-1'
edition.language = 'en'
edition.name = 'edition-name-1'
edition.translator = 'edition-translator-1'
edition.type = 'Translation'
edition.format = 'format1'
edition.direction = 'ltr'
edition.save()

edition = Edition()
edition.id = 'edition-2'
edition.language = 'en'
edition.name = 'edition-name-2'
edition.translator = 'edition-translator-2'
edition.type = 'Translation'
edition.format = 'format1'
edition.direction = 'ltr'
edition.save()


# import data for image
image = Image()
image.ayah_id = 'ayah-1'
image.image = 'Image link for ayah-1'
image.save()

image = Image()
image.ayah_id = 'ayah-2'
image.image = 'Image link for ayah-2'
image.save()


# import data for surah
surah = Surah()
surah.id = 'surah-1'
surah.number = 1
surah.name = 'surah-1-name'
surah.english_name = 'surah-1-english-name'
surah.number_of_ayahs = 7
surah.revelation_type = 'Mecca'
surah.save()

surah = Surah()
surah.id = 'surah-2'
surah.number = 2
surah.name = 'surah-2-name'
surah.english_name = 'surah-2-english-name'
surah.number_of_ayahs = 7
surah.revelation_type = 'Mecca'
surah.save()


# import data for translation
translation = Translation()
translation.id = 'translation-ayah-1-edition-1'
translation.ayah_id = 'ayah-1'
translation.edition_id = 'edition-1'
translation.text = 'Translation for ayah-1 edition-1'
translation.save()

translation = Translation()
translation.id = 'translation-ayah-1-edition-2'
translation.ayah_id = 'ayah-1'
translation.edition_id = 'edition-2'
translation.text = 'Translation for ayah-1 edition-2'
translation.save()

translation = Translation()
translation.id = 'translation-ayah-2-edition-1'
translation.ayah_id = 'ayah-2'
translation.edition_id = 'edition-1'
translation.text = 'Translation for ayah-2 edition-1'
translation.save()