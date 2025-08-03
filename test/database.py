import unittest
import os
from utils import database

class database_tests(unittest.TestCase):
  @classmethod
  def setUpClass(cls):
    cls.example_mac = 'ab:cd:ef:12:34:56'
    cls.db_path = 'test.db'
    cls.engine = database.generate_engine(f'sqlite:///{cls.db_path}')
    cls.db = database.db(cls.engine)
  
  @classmethod
  def tearDownClass(cls):
    os.remove(cls.db_path)
    
  def retrieve_database_without_populating(cls):
    host = cls.db.find_host(cls.example_mac)
    cls.assertTrue(len(host) == 0)
    cls.assertFalse(host[0].mac == cls.example_mac)
    
  def test_creating_and_retrieving_data(cls):
    cls.db.add_host(cls.example_mac)
    
    host = cls.db.find_host(cls.example_mac)['host']
    cls.assertEqual(host.mac, cls.example_mac)

if __name__ == '__main__':
  unittest.main()
