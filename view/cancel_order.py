from flask import Flask, jsonify, request,abort
from model.api_class import Orders
app = Flask(__name__)
	
delivery_orders=[]

@app.route('/api/v1/parcels/<int:parcelId>',methods=['DELETE'])
def cancel_specific_delivery_order_with_ID(parcelId):
    service = request.get_json()

    parcelId = len(delivery_orders)+1
    parcel_name = service.get('parcel_name')
    parcel_price = service.get('parcel_price')
    delivery_time = service.get('delivery_time')
    userId = len(delivery_orders)+1
    currentlocation =service.get('currentlocation')
    destination = service.get('destination')

    order = 0
    for order['parcelId'] in delivery_orders:
      if order['parcelId'] == parcelId:
         del delivery_orders[order] 
      return jsonify ({'message':'delivery order has been terminated'}), 410

      order +=1 
      return jsonify({"message": 'delivery order does not exit'}), 205







