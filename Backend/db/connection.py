from mongoengine import connect
from dotenv import load_dotenv
import os

def connect_to(database: str):
    try:
        load_dotenv()

        connect (
            host = os.getenv("DB_HOST"),
            port = int(os.getenv("DB_PORT")),
            db = database
        )
        
        print(f"Successfully connected to db: {database}")

    except Exception:
        print("Some error occured!")