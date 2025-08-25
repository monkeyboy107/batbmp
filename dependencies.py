import yaml
import os
from utils import database

settings_paths = [
'./config.yaml.example',
'/etc/batbmp/config.yaml',
'./config.yaml'
]


def load_settings():
  settings = {}
  for path in settings_paths:
    if os.path.exists(path):
      with open(path) as stream:
        data = yaml.safe_load(stream)
        settings = {**settings, **data}

  engine = database.generate_engine(settings['database']['uri'])
  db = database.db(engine)
  
  settings['engine'] = engine
  settings['database'] = db
  return settings


settings = load_settings()
