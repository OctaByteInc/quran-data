from fireo.fields import IDField, TextField
from fireo.models import Model


class Audio(Model):
    id = IDField()
    ayah_id = TextField()
    edition_id = TextField()
    type = TextField()  # Translation or Arabic
    audio = TextField()
