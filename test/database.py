import unittest
from utils import database

class render_template(unittest.TestCase):
  def test_database(self):
    engine = database.generate_engine()
    db = database.db(engine)
    
    example_mac = 'ab:cd:ef:12:34:56'
    db.add_host(example_mac)
    
    print(db.find_host(example_mac))

if __name__ == '__main__':
  unittest.main()
