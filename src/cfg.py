# from dotenv import load_dotenv
# from dotenvy import load_env, read_file
# from os import environ
import os
from time import strftime  # Load just the strftime Module from Time

# load_dotenv()
# load_env(read_file('.env'))
# my_var = environ.get('SOLR_PASS')
# print(my_var)

SOLR_HOST = os.getenv("SOLR_HOST", "localhost")
SOLR_PORT = os.getenv("SOLR_PORT", 8983)
SOLR_COLL = os.getenv("SOLR_COLL", "files1")
SOLR_USER = os.getenv("SOLR_USER", "solr")
SOLR_PASS = os.getenv("SOLR_PASS", "Ghbdtn123!")

DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = os.getenv("DB_PORT", 5432)
DB_NAME = os.getenv("DB_NAME", "geodex2")
DB_SCHEMA = os.getenv("DB_SCHEMA", "public")
DB_USER = os.getenv("DB_USER", "geodex2")
DB_PASS = os.getenv("DB_PASS", "geodex2pwd")
DB_DSN = f"postgresql+asyncpg://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
# print(DATABASE_URL)

DATETIME_CURRENT = str(strftime("%Y-%m-%d-%H-%M-%S"))

FILE_LOG_NAME = 'pg2solr'
FILE_LOG = DATETIME_CURRENT + '_' + FILE_LOG_NAME + '.log'
FILE_LOG_FORMAT = '%(asctime)s %(levelname)s %(message)s'
FOLDER_OUT = 'log'
FOLDER_BASE = os.getenv("FOLDER_BASE", "C:\\Glory\\Projects\\Python\\zsniigg\\pg2solr\\src")
