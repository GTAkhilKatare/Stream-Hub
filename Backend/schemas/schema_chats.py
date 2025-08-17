from mongoengine import document, ObjectIdField, StringField

class Chats(document):
    """The ODM for storing the live chats"""

    streamer_id = ObjectIdField()

    user_id = ObjectIdField()

    message = StringField (
        required = True,
    )
