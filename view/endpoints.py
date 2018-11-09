from flask import Flask, jsonify, request,abort
from run import app
from model.api_class import Orders,create_delivery_order


delivery_orders=[]

@app.route('/api/v1/parcels', methods =['POST'])
def create_delivery_order():
    service = request.get_json()
    
    parcelId = service.get('parcelId')
    parcel_name = service.get('parcel_name')
    parcel_price = service.get('parcel_price')
    delivery_time = service.get('delivery_time') 

          

    if 'parcelId' == 0:
      return jsonify ({'message':'cannot create order'}),401
    if parcel_name == " ":
      return jsonify({"message":"you cant post an empty string"})

    
    if 'parcel_price'is not int:
      return jsonify({'message':'invalid input'}),401
    else:
      return jsonify({'message':'delivery order created'}),201

    if "parcel_price" not in delivery_orders:
            return jsonify ({"message":"order price required"}),402

    if 'delivery_time' > 16:
      return jsonify({'message':'delivery should be in less than 16 hours'})

    for 'parcel_name' in delivery_orders:
       if delivery_orders['parcel_name'] in delivery_orders:
         return jsonify(delivery_orders.ser),201

    order = Orders(parcelId,parcel_name,parcel_price,delivery_time)

    delivery_orders.append(order)
    return jsonify({"message": "delivery_order created"}), 201

@app.route('/api/v1/parcels', methods=['GET'])
def all_parcel_delivery_orders():
  if request.method == 'GET':
    if delivery_orders == []:
      return jsonify ({"message":"delivery_orders is empty"}),400
    return jsonify({delivery_orders}),200
    
          

#Get a specific parcel delivery order GET /parcels/<parcelId>
@app.route('/api/v1/parcels/<int:parcelId>', methods =['GET'])
def fetch_specific_parcel_delivery_order(parcelId):

  if delivery_orders['parcelId'] not in delivery_orders:
    return jsonify({'message':'parcel id is not in delivery_orders'}),400
  else:
    if delivery_orders[parcelId] == parcelId:
      return jsonify({delivery_orders}),200

  for delivery_orders in delivery_orders:
    if parcelId < 1:
      return jsonify({'message':'order_id does not exist'}),400
    else:
      return jsonify({'message':'order_id is available'}),200

  if len(delivery_orders) != 1:
    return jsonify({delivery_orders[1]}),200



#Fetch all parcel delivery orders by a specific user GET /users/<userId>/parcels
@app.route('/api/v1/users/<userId>/parcels',methods=['GET'])
















# #Cancel a specific parcel delivery order PUT /parcels/<parcelId>/cancel
# @app.route('/api/v1/parcels/<int:parcelId/cancel>',methods=['PUT'])
# def cancel_specific_delivery_order(order_id):
#   service = request.get_json()
    
#   delivery_orders = {
#                 "parcelId": service['parcelId'],
#                 "parcel_name": service['parcel_name'],
#                 "parcel_price": service['parcel_price'],
#                 "delivery_time":service['delivery_time'] 
            
#             }
#         if not 'order_name':
#            return jsonify({
#                    'message': 'sorry!book_id is required and cannot be less than 1'
#            }),400

#     for delivery_orders in delivery_orders:
#       if delivery_orders['parcelId'] == id:
#         delivery_orders['id'] = request_['id']
#         delivery_orders['name'] = request_data['name']
     
#       return jsonify ({'message':'deivery order terminated'}), 200
#       return jsonify({'message':'delivery order not found'}),405

     
#         delivery_orders.append(service)
#         return jsonify({"message": "delivery_order cancelled"}), 201














# if __name__ == '__main__':
#        pass




