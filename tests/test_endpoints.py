import unittest
from api.view.endpoints import *
import json


class TestEndpoints(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
       

    def test_get_all_parcel_delivery_orders(self):
        response = self.app.get('api/v1/parcels')
        self.assertEqual(response.status_code,200)
        self.assertEqual(response.content_type,'application/json')

    # def test_delivery_time_exceeds_specified_time(self):
    #     with self.assertRaises(ValueError):
	# 	create_delivery_order(1,'water',3000,20,5,'ntinda','nakawa')

            
    def test_create_parcel_delivery_order(self):
        response = self.app.post('/api/v1/parcels',
               data=json.dumps( {'parcelId': 3,
                                 'parcel_name': 'cakes',
                                 'parcel_price': 6000,
                                 'delivery_time': 4,
                                 'userId': 8,
                                 'currentlocation':'bukoto',
                                 'destination':'najjera'
                                  }
                              ),
                    content_type='application/json')

        self.assertEqual(response.status_code,201)
        content= response.get_json()
        print(content)

    def test_create_parcel_delivery_order_returns_errors(self):
        response = self.app.post ('/api/v1/parcels',
                    data=json.dumps( {'parcelId': 3,
                                 'parcel_name': 'cakes',
                                 'parcel_price': "abcd",
                                 'delivery_time': 4,
                                 'userId': 8,
                                 'currentlocation':'bukoto',
                                 'destination':'najjera'
                                  }
                              ),
                    content_type='application/json')
                        
        self.assertEqual(response.status_code,401)
        content=response.get_json()
        print(content)

    def test_get_specific_parcel_delivery_order_with_ID(self):
        response =self.app.get('/api/v1/parcels/1')
        self.assertEqual(response.status_code,200)

    # def test_get_specific_delivery_order_with_id(self):
    #     response = self.app.get('/api/v1/parcels/1')
    #     response_json = json.loads(response.data.decode())
    #     self.assertIn("delivery order is not in the list", response_json[])


    def test_to_cancel_specific_parcel_delivery_order_with_ID(self):
        response = self.app.delete('/api/v1/parcels/1')
        self.assertEqual(response.status_code,500)

    def test_cancel_delivery_order_with_Specific_ID(self):
        response = self.app.put('/api/v1/entries/1')
        self.assertEqual(response.status_code, 404)












if __name__== '__main__':
 unittest.main()