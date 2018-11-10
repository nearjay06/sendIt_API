

@app.route('/api/v1/parcels/<int:parcelId>',methods=['PUT'])
def cancel_specific_delivery_order(parcelId):
    service = request.get_json()
    
    parcelId = service.get('parcelId')
    parcel_name = service.get('parcel_name')
    parcel_price = service.get('parcel_price')
    delivery_time = service.get('delivery_time')
    userId = service.get('userId')  

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





