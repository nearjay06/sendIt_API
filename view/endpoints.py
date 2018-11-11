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
      return jsonify({"message":" please add parcel name"})
      
    if not isinstance(parcel_price, int):
      return jsonify({'message':'invalid input'}),401
    
    if not isinstance(parcel_name,str):
      return jsonify({"message":"parcel name should be a string"}),400
    
    if "destination" not in service:
            return jsonify({"message":"no input for delivery destination"}),400

    if "parcel_price" not in service:
            return jsonify({"message":"invalid"}),400

    if type (service["delivery_time"]) is not int:
            return jsonify ({"message": "delivery time should not be a string"}),400     

    if not destination:
      return jsonify ({'message':'destination for delivery order required'}),400

    if isinstance(destination,int):
      return jsonify ({'message':'invalid input'}),400

    if delivery_time > 16:
      return jsonify({'message':'delivery should be in less than 16 hours'})

    order = Orders(parcelId,parcel_name,parcel_price,delivery_time,userId,currentlocation,destination)

    delivery_orders.append(order.make_delivery_order())
    return jsonify(delivery_orders),201

@app.route('/api/v1/parcels', methods=['GET'])
def get_all_parcel_delivery_orders():
   if delivery_orders == []:
      return jsonify ({"message":"delivery_orders list is empty"}),400
   else:
      return jsonify({'delivery_orders': delivery_orders}),200
    
          
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

  
@app.route('/api/v1/users/<int:userId>/parcels',methods=['GET'])
def get_delivery_order_by_specific_user_with_ID(userId):
  for order in delivery_orders:
    if order['userId'] == userId:
      return jsonify(order)
    else:
        return jsonify({'message':'order not found'}),400

    if order['userId'] is int:
      return jsonify(order),200

    if order['userId'] is str:
      return jsonify({'message':'userId must not be a string'}),400

    if isinstance (userId,str):
      return jsonify({'message':'userId must not be a string'}),400

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



    

   

