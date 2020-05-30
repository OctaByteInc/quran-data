from fireo.fields import IDField, TextField
from fireo.models import Model


class Image(Model):
    ayah_id = IDField()
    link = TextField()
    
    class Meta:
        collection_name = "images"
