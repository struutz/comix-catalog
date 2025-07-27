from mongoengine import Document, StringField, BooleanField

class ComicDocument(Document):
    title = StringField(required=True)
    isbn = StringField(required=True, unique=True)
    publisher = StringField(required=True)
    description = StringField()
    is_deleted = BooleanField(default=False)
