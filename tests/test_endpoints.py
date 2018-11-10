import unittest
from view.endpoints import app
import json


class TestEndpoints(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
       

    def test_get_all_parcel_delivery_orders(self):
        response = self.app.get('api/v1/parcels')
        self.assertEqual(response.status_code,200)
        self.assertEqual(response.content_type,'application/json')


    def test_create_parcel_delivery_order(self):
        response =self.app.post('/api/v1/parcels')
        self.assertEqual(response.status_code,201)
        self.assertEqual("delivery order created", response.json['message'])


    def test_to_cancel_specific_parcel_delivery_order(self):
        response = self.app.put('/api/v1/parcels/1')
        self.assertEqual(response.status_code,200)

    def test_post_endpoint_errors_that_returns_400(self):
        response = self.app.post ('/api/v1/parcels',
                    data=json.dumps( {'id': 0
                                        }
                                ),
                        content_type='application/json')
                    
        self.assertEqual(response.status_code,400)





# def test_get_specific_parcel_delivery_order(self):
#  response =self.app.get('/api/v1/parcels/<parcelId>')


 # def test_get_parcel_delivery_order_by_specific_user(self):



if __name__== '__main__':
 unittest.main()