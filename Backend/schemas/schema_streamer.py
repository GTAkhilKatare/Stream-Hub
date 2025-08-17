from mongoengine import document, ObjectIdField, StringField

class Streamer(document):
    """The ODM for streamer collection."""

    user_id = ObjectIdField (
        required = True,
        index = True
    )

    channel_name = StringField (
        required = True,
        unique = True,
        index = True
    )

    profile_pic = StringField (
        required = True,
    )

    description = StringField()

