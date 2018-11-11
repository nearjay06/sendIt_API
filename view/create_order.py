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
