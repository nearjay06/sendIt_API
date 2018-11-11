import json
import unittest
from .view.endpoints import app


class TestEndpoints(unittest.TestCase):
    def setUp(self):
      self.app = app.test_client()
       
def test_get_all_parcel_delivery_orders(self):
     response = self.app.get('api/v1/parcels')
     self.assertEqual(response.status_code,200)
     self.assertEqual(response.content_type,'application/json')






if __name__== '__main__':
  unittest.main()