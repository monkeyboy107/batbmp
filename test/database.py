import unittest
from utils import database

class render_template(unittest.TestCase):
  def test_database(self):
    engine = database.generate_engine('sqlite:///file.db')
    db = database.db(engine)
    
    example_mac = 'ab:cd:ef:12:34:56'
    db.add_host(example_mac)
    
    host = db.find_host(example_mac).all()
    self.assertTrue(len(host) == 1)
    self.assertEqual(host[0].mac, example_mac)

if __name__ == '__main__':
  unittest.main()
