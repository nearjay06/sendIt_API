import json
import unittest
from api.view.endpoints import app


class TestEndpoints(unittest.TestCase):
  def setUp(self):
    self.app = app.test_client()

def test_get_parcel_delivery_order_by_specific_user():
  pass




if __name__== '__main__':
 unittest.main() 