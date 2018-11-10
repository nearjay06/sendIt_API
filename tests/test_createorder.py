import json
import unittest
from .view.endpoints import app

class TestEndpoints(unittest.TestCase):
  def setUp(self):
    self.app = app.test_client()

def test_create_parcel_delivery_order(self):
 response =self.app.post('/api/v1/parcels')
 self.assertEqual(response.status_code,201)
 self.assertEqual("delivery order created", response.json['message'])




if __name__== '__main__':
 unittest.main()