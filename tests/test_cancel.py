import unittest
from view.endpoints import app,create_delivery_order,get_specific_parcel_delivery_order_with_ID
import json	
	
class TestEndpoints(unittest.TestCase):
  def setUp(self):
    self.app = app.test_client()
       
def test_to_cancel_specific_parcel_delivery_order_with_ID(self):
        response = self.app.delete('/api/v1/parcels/1')
        self.assertEqual(response.status_code,500)



if __name__== '__main__':
 unittest.main()