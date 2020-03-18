from fireo.fields import IDField, TextField
from fireo.models import Model


class Translation(Model):
    id = IDField()
    ayah_id = TextField()
    edition_id = TextField()
    text = TextField()