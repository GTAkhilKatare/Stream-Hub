from mongoengine import document, EmbeddedDocument
from mongoengine import StringField, DateField, EmbeddedDocumentField
from datetime import date


class Settings(EmbeddedDocument):
    
    themes = StringField (
        required = True,
        default = "dark"
    )


class Users(document):
    """The ODM for users collection."""

    email = StringField (
        required = True,
        unique = True,
        index = True
    )

    username = StringField (
        required = True,
        unique = True,
        index = True
    )

    password = StringField (
        required = True
    )

    user_type = StringField (
        required = True,
        default = "viewer"
    )

    created_at = DateField (
        required = True,
        default = date.today
    )

    settings = EmbeddedDocumentField(Settings)