import json
import unittest
from .view.endpoints import app


class TestEndpoints(unittest.TestCase):
  def setUp(self):
    self.app = app.test_client()
       
def test_to_cancel_specific_parcel_delivery_order(self):
    response = self.app.put('/api/v1/parcels/1')
    self.assertEqual(response.status_code,200)


if __name__== '__main__':
 unittest.main()