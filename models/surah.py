from fireo.fields import IDField, NumberField, TextField
from fireo.models import Model


class Surah(Model):
    id = IDField()
    number = NumberField(int_only=True)
    name = TextField()
    english_name = TextField()
    english_name_translation = TextField()
    number_of_ayahs = NumberField(int_only=True)
    revelation_type = TextField()

    class Meta:
        to_lowercase = True
        collection_name = "surahs"
