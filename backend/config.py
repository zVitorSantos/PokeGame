import os

user = os.getenv('DB_USER')
password = os.getenv('DB_PASSWORD')
host = os.getenv('DB_HOST', 'localhost')
dbname = os.getenv('DB_NAME')

SQLALCHEMY_DATABASE_URI = f'postgresql://{user}:{password}@{host}/{dbname}'
