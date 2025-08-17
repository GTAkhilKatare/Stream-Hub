from mongoengine import document, ObjectIdField, StringField, DateTimeField, IntField
from datetime import datetime

class Stream(document):
    """The ODM for storing metadata of live streams."""

    # About stream
    streamer_id = ObjectIdField (
        required = True,
        index = True
    )

    title = StringField (
        required = True,
        max_length = 50
    )

    thumbnail_url = StringField (
        required = True
    )

    stream_key = StringField (
        required = True,
        unique = True
    )

    likes = IntField (
        required = True,
        default = 0
    )

    # Stream URLs
    rtmp_url = StringField (
        required = True,
        unique = True
    )

    hls_url = StringField (
        required = True,
        unique = True
    )

    recording_path = StringField (
        required = True,
        unique = True,
    )

    # Timings
    started_at = DateTimeField (
        required = True,
        default = datetime.utcnow
    )

    ended_at = DateTimeField (
        required = True,
        default = None
    )

    duration = StringField (
        required = True,
        default = None
    )