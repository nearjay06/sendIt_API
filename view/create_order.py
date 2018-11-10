from flask import Flask, jsonify, request,abort
from model.api_class import Orders
app = Flask(__name__)

delivery_orders=[]

@app.route('/api/v1/parcels', methods=['POST'])
def create_delivery_order():
    service = request.get_json()
    
    parcelId = len(delivery_orders)+1
    parcel_name = service.get('parcel_name')
    parcel_price = service.get('parcel_price')
    delivery_time = service.get('delivery_time')
    userId = len(delivery_orders)+1 
          

    if parcel_name == " ":
      return jsonify({"message":"you cant post an empty string"})
    
    if not isinstance(parcel_price, int):
      return jsonify({'message':'invalid input'}),401
    

    if not isinstance(parcel_name,str):
      return jsonify({"message":"parcel name should be a string"})
    
    if delivery_time > 16:
      return jsonify({'message':'delivery should be in less than 16 hours'})

    for parcel_name in delivery_orders:
       if parcel_name in delivery_orders:
         return jsonify(Orders.make_delivery_order()),201

    order = Orders(parcelId,parcel_name,parcel_price,delivery_time,userId)

    delivery_orders.append(order.make_delivery_order())
    return jsonify(delivery_orders),201
