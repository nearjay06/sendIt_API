from flask import Flask, jsonify, request,abort
from model.api_class import Orders
app = Flask(__name__)

delivery_orders=[]

@app.route('/api/v1/parcels/<int:parcelId>', methods =['GET'])
def fetch_specific_parcel_delivery_order(parcelId):

  if delivery_orders['parcelId'] not in delivery_orders:
    return jsonify({'message':'parcel id is not in delivery_orders'}),400
  else:
    if delivery_orders[parcelId] == parcelId:
      return jsonify(Orders.make_delivery_order()),200

  for delivery_orders in delivery_orders:
    if parcelId < 1:
      return jsonify({'message':'order_id does not exist'}),400
    else:
      return jsonify({'message':'order_id is available'}),200

  a=0
  for order in delivery_orders:
    if order['parcelId'] == parcelId:
      return jsonify ({'delivery_order': order}), 200
    a+=1
             
    return jsonify({"message": 'delivery order does not exit'}), 205
