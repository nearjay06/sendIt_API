import unittest
from view.endpoints import app,create_delivery_order,get_specific_parcel_delivery_order_with_ID
import json

class TestEndpoints(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
       
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






if __name__== '__main__':
 unittest.main()