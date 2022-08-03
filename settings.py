from dotenv import load_dotenv
load_dotenv()
import os

EMAIL=os.getenv("EMAI")
PASSWORD=os.getenv("hgtwcprjwmhonxls")

DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_USERNAME = os.getenv("DB_USERNAME")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")