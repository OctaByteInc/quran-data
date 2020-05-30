from fireo.fields import IDField, TextField, NumberField
from fireo.models import Model


class Audio(Model):
    id = IDField()
    ayah_id = TextField()
    ayah_number = NumberField()
    edition_id = TextField()
    type = TextField()  # Translation or Arabic
    link = TextField()

    class Meta:
        collection_name = "audios"
