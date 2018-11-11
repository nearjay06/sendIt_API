from flask import Flask, jsonify, request,abort
from model.api_class import Orders
app = Flask(__name__)

delivery_orders=[]

@app.route('/api/v1/parcels/<int:parcelId>', methods =['GET'])
def get_specific_parcel_delivery_order_with_ID(parcelId):
    for order in delivery_orders:
      if order['parcelId'] == parcelId:
        return jsonify(order)
      else:
        return jsonify({'message':'delivery order not found'}),400

      if len(delivery_orders) != 0:
        return jsonify(order[0])
      else:
        return jsonify({"message":"you  dont have order in the list yet"})

      if order['parcelId'] is None:
        return jsonify({'message':'delivery order is not in the list'})

      if order['parcelId'] is str:
        return jsonify({'message':'parcelId cannot be a string'})

      if isinstance (parcelId,str):
        return jsonify({'message':'parcelId cannot be a string'}),400

      if order['parcelId'] == parcelId:
        return jsonify(Orders.make_delivery_order()),200

      if parcelId <= 0:
        return jsonify({'message':'parcelId does not exist'}),205
      else:
        return jsonify({'message':'parcelId is available'}),200

