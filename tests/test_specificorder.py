import unittest
from view.endpoints import app,create_delivery_order,get_specific_parcel_delivery_order_with_ID
import json

class TestEndpoints(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
       
    def test_get_specific_parcel_delivery_order_with_ID(self):
        response =self.app.get('/api/v1/parcels/1')
        self.assertEqual(response.status_code,200)



if __name__== '__main__':
 unittest.main()
