import unittest
import os
from utils import database

class database_tests(unittest.TestCase):
  @classmethod
  def setUp(cls):
    cls.example_mac = 'ab:cd:ef:12:34:56'
    cls.db_path = 'test.db'
    cls.engine = database.generate_engine(f'sqlite:///{cls.db_path}')
    cls.db = database.db(cls.engine)
  
  @classmethod
  def tearDown(cls):
    os.remove(cls.db_path)
    
  def test_creating_and_retrieving_data(self):
    self.db.add_host(self.example_mac)
    
    host = self.db.find_host(self.example_mac)['host']['mac']
    self.assertEqual(host, self.example_mac)

if __name__ == '__main__':
  unittest.main()
