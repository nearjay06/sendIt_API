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
    currentlocation =service.get('currentlocation')
    destination = service.get('destination') 
          

    if parcel_name == " ":
      return jsonify({"message":"you cant post an empty string"}),204
    
    if not isinstance(parcel_price, int):
      return jsonify({'message':'invalid input'}),401
    

    if not isinstance(parcel_name,str):
      return jsonify({"message":"parcel name should be a string"})
    
    
    # if not isinstance(delivery_time,str):
    #   return jsonify({'message':'delivery time cannot be a string'}),403

    if destination  not in delivery_orders or destination.isspace:
      return jsonify ({'message':'destination for delivery order is required'}),400

    if not isinstance(destination,int):
      return jsonify ({'message':'invalid input'}),400

    # if delivery_time > 16:
    #   return jsonify({'message':'delivery should be in less than 16 hours'})


    order = Orders(parcelId,parcel_name,parcel_price,delivery_time,userId,currentlocation,destination)

    delivery_orders.append(order.make_delivery_order())
    return jsonify(delivery_orders),201
