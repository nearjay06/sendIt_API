from flask import Flask, jsonify, request,abort
from model.api_class import Orders
app = Flask(__name__)

delivery_orders=[]

#Fetch all parcel delivery orders by a specific user GET /users/<userId>/parcels
@app.route('/api/v1/users/<userId>/parcels',methods=['GET'])
def get_delivery_order_by_specific_user(userId):
  for order in delivery_orders:
    pass
