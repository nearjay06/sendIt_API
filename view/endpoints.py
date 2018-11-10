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
    
    # if not isinstance(delivery_time,str):
    #   return jsonify({'message':'delivery time cannot be a string'}),403

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
def all_parcel_delivery_orders():
   if delivery_orders == []:
      return jsonify ({"message":"delivery_orders list is empty"}),400
   else:
      return jsonify({'delivery_orders': delivery_orders}),200
    
          
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



#Fetch all parcel delivery orders by a specific user GET /users/<userId>/parcels
@app.route('/api/v1/users/<userId>/parcels',methods=['GET'])
def get_delivery_order_by_specific_user(userId):
  for order in delivery_orders:
    pass




@app.route('/api/v1/parcels/<int:parcelId>',methods=['PUT'])
def cancel_specific_delivery_order(parcelId):
    service = request.get_json()
    
    parcelId = service.get('parcelId')
    parcel_name = service.get('parcel_name')
    parcel_price = service.get('parcel_price')
    delivery_time = service.get('delivery_time')
    userId = service.get('userId')
    currentlocation =service.get('currentlocation')
    destination = service.get('destination')   

    if not parcel_name:
           return jsonify({
                   'message': 'sorry!parcel_name is required'
           }),400

    a=0
    for parcelId in delivery_orders:
      if delivery_orders['parcelId'] == parcelId:
        del delivery_orders[a] 
        return jsonify ({'message':'delivery order terminated'}), 200
      a+=1
             
    return jsonify({"message": 'delivery order does not exit'}), 205








