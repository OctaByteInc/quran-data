from fireo.fields import IDField, TextField, NumberField
from fireo.models import Model


class Translation(Model):
    id = IDField()
    ayah_id = TextField()
    edition_id = TextField()
    ayah_number = NumberField()
    text = TextField()
    
    class Meta:
        collection_name = "translations"
