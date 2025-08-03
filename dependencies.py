import yaml
import os
from utils import database

settings_paths = [
'/etc/batbmp/config/yaml',
'./config.yaml'
]


def load_settings():
  settings = {}
  for path in settings_paths:
    if os.path.exists(path):
      with open(path) as stream:
        data = yaml.safe_load(stream)
        settings = {**settings, **data}

  connection_uri = ''
  database_method = settings['database']['method']
  connection_uri = f'{database_method}://{connection_uri}'
  if 'username' in settings['database']:
    database_username = settings['database']['username']
    connection_uri = f'{connection_uri}{database_username}'
  if 'password' in settings['database']:
    databse_password = settings['database']['password']
    connection_uri = f'{connection_uri}@{database_password}'
  database_host = settings['database']['host']
  connection_uri = f'{connection_uri}{database_host}'

  settings['connection_uri'] = connection_uri

  engine = database.generate_engine(settings['connection_uri'])
  db = database.db(engine)
  
  settings['engine'] = engine
  settings['database'] = db
  return settings


settings = load_settings()
