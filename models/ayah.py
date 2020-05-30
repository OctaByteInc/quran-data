from fireo.fields import IDField, NumberField, BooleanField, TextField
from fireo.models import Model


class Ayah(Model):
    id = IDField()
    surah_id = TextField()
    number = NumberField(int_only=True)
    number_in_surah = NumberField(int_only=True)
    juz = NumberField(int_only=True)
    manzil = NumberField(int_only=True)
    ruku = NumberField(int_only=True)
    hizb_quarter = NumberField(int_only=True)
    sajda = BooleanField()
    arabic = TextField()

    class Meta:
        collection_name = "ayahs"
