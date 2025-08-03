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
    
  def setUp(self):
    pass

  def retrieve_database_without_populating(self):
    pass
        
  def test_creating_and_retrieving_data(self):
    pass

if __name__ == '__main__':
  unittest.main()
