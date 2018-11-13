from flask import Flask, jsonify, request,abort
from api.model.api_class import Orders
from api import app

delivery_orders=[]
user = []

@app.route('/api/v1/parcels', methods=['POST'])
def create_delivery_order():
    service = request.get_json()
    
    parcelId = len(delivery_orders)+1
    parcel_name = service.get('parcel_name')
    parcel_price = service.get('parcel_price')
    delivery_time = service.get('delivery_time')
    destination = service.get('destination')
    
     
    if parcel_name == " ":
      return jsonify({"message":" please add parcel name"}),200
    	
    if not isinstance(parcel_price, int):
      return jsonify({'message':'invalid input'}),401
    
    if not isinstance(parcel_name,str):
      return jsonify({"message":"parcel name should be a string"}),400
    
    if not destination:
      return jsonify ({'message':'destination for delivery order required'}),400

    if delivery_time > 16:
      return jsonify({'message':'delivery should be in less than 16 hours'})

    order = Orders(parcelId,parcel_name,parcel_price,delivery_time,destination)
    delivery_orders.append(order.make_delivery_order())
    return jsonify(delivery_orders),201


@app.route('/', methods=['GET'])
def Home():
  return "welcome to SENDIT"

@app.route('/api/v1/parcels', methods=['GET'])
def get_all_parcel_delivery_orders():
   if delivery_orders == []:
      return jsonify ({"message":"delivery_orders list is empty"}),400
   else:
      return jsonify({'delivery_orders': delivery_orders}),200
    
          
@app.route('/api/v1/parcels/<int:parcelId>', methods =['GET'])
def get_parcel_delivery_order_with_parcel_ID(parcelId):
    for order in delivery_orders:
      if order['parcelId'] == parcelId:
        return jsonify(order),200
      else:
        return jsonify({'message':'delivery order not found'}),400

      if order['parcelId'] is None:
        return jsonify({'message':'delivery order is not in the list'})

      if isinstance (parcelId,str):
        return jsonify({'message':'parcelId cannot be a string'}),400

      if order['parcelId'] == parcelId:
        return jsonify(Orders.make_delivery_order()),200

      if parcelId <= 0:
        return jsonify({'message':'parcelId does not exist'}),205
      

  
@app.route('/api/v1/users/<int:userId>/parcels',methods=['GET'])
def get_delivery_order_by_user_with_user_ID(userId):
       trades = request.get_json()

       userId = len(user)+1
       username = trades.get('username')
       user_email = trades.get('user_email')
       user_location = trades.get('user_location')
    
       for client in user:
         if client['userId'] == userId:
           return jsonify(user),200
       else:
        return jsonify({'message':'user not found'}),400

        if isinstance(userId,str):
           return jsonify({'message':'userId cannot be a string'}),400

       








    
@app.route('/api/v1/parcels/<int:parcelId>',methods=['DELETE'])
def cancel_specific_delivery_order_with_ID(parcelId):
    service = request.get_json()

    parcelId = len(delivery_orders)+1
    parcel_name = service.get('parcel_name')
    parcel_price = service.get('parcel_price')
    delivery_time = service.get('delivery_time')
    destination = service.get('destination')


    order = 0
    for order['parcel_name'] in delivery_orders:
      if order['parcel_name'] == parcel_name:
         del delivery_orders[order] 
      return jsonify ({'message':'delivery order has been terminated'}), 410

      order +=1 
      return jsonify({"message": 'delivery order does not exit'}), 205

@app.route('/api/v1/parcels/<int:parcelId>/cancel',methods=['PUT'])
def modify_specific_delivery_order_with_ID(parcelId):
      service = request.get_json()

      parcelId = len(delivery_orders)+1
      parcel_name = service.get('parcel_name')
      parcel_price = service.get('parcel_price')
      delivery_time = service.get('delivery_time')
      destination = service.get('destination')







      order = Orders(parcelId,parcel_name,parcel_price,delivery_time,destination)
      delivery_orders.append(order.make_delivery_order())
      return jsonify({"message": "delivery_orders cancelled"}),200


    


