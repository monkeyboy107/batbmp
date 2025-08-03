from utils import database

# TODO: This needs to pull the connection string from a config
engine = database.generate_engine('sqlite:///file.db')
db = database.db(engine)
