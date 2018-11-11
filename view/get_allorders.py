from flask import Flask, jsonify, request,abort
from model.api_class import Orders
app = Flask(__name__)

delivery_orders=[]

@app.route('/api/v1/parcels', methods=['GET'])
def get_all_parcel_delivery_orders():
   if delivery_orders == []:
      return jsonify ({"message":"delivery_orders list is empty"}),400
   else:
      return jsonify({'delivery_orders': delivery_orders}),200
    

    