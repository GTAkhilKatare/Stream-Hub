from mongoengine import document, ObjectIdField

class Likes(document):
    """The ODM for storing the user who liked the stream."""

    stream_id = ObjectIdField()

    user_id = ObjectIdField()