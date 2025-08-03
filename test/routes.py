import unittest
import os
import asyncio
from dependencies import db
from utils import database
from routers import kickstart, register

class routes_tests(unittest.IsolatedAsyncioTestCase):
  @classmethod
  def setUp(cls):
    cls.example_mac = 'ab:cd:ef:12:34:56'
    cls.db_path = 'test.db'
    db.engine = database.generate_engine(f'sqlite:///{cls.db_path}')
    db.db = database.db(db.engine)
  
  @classmethod
  def tearDown(cls):
    os.remove(cls.db_path)
        
  async def test_kickstart(self):
    db.add_host(self.example_mac)
    host = kickstart.retrieve_kickstart(self.example_mac) 
    host = await host
    self.assertEqual(host, self.example_mac)

  async def test_registry(self):
    result = register.register_host(self.example_mac)
    result = await result
    self.assertEqual(result['status'], 'Success')

def suite():
  suite = unittest.TestSuite()
  suite.addTest(routes_test('test_kickstart'))
  suite.addTest(routes_test('test_registry'))
  return suite()

if __name__ == '__main__':
  unittest.main()
