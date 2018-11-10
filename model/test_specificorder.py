import json
import unittest
from .view.endpoints import app


class TestEndpoints(unittest.TestCase):
  def setUp(self):
    self.app = app.test_client()
       
def test_get_specific_parcel_delivery_order(self):
  response =self.app.get('/api/v1/parcels/<parcelId>')
   pass



if __name__== '__main__':
  unittest.main()         