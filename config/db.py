from sqlalchemy import create_engine, MetaData
from decouple import config

DB_USER = config('DB_USER')
DB_PASSWORD = config('DB_PASSWORD')
DB_HOST = config('DB_HOST', default='localhost')
DB_PORT = config('DB_PORT', default=5432, cast=int)
DB_DATABASE = config('DB_DATABASE')


engine = create_engine(
    f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_DATABASE}")

meta = MetaData()

conn = engine.connect()
