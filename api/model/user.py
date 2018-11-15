from flask import Flask, jsonify
from api.model.parcels import Orders, delivery_orders

parcelId = len(delivery_orders)+1
users = [] 
userId =  len(users)+1

class Users:
    def __init__(self,userId,username,user_email,user_password):
       self.userId = userId
       self.username = username
       self.user_email = user_email
       self.user_password = user_password
       

    def deliver_to_user(self):
       trades = {
          "userId": self.userId,
          "username": self.username,
          "user_email": self.user_email,
          "user_password" : self.user_password
          
         }

       return trades
    def get_user_by_id(userId):
      for user in users:
        existing_user = [user for user in users if user['userId'] == userId]
        if not existing_user:
          return jsonify({'message':'user is not in the list'}),204
        else:
          return (existing_user),200 
       
    def make_delivery_order(self):
      service = {
          "parcelId": parcelId,
          "userId": userId,
          "parcel_name": self.parcel_name,
          "parcel_price": self.parcel_price,
          "delivery_time":self.delivery_time,
          "destination" : self.destination
         
        }

      delivery_orders.append(service)
      return delivery_orders

    def retrieve_delivery_orders(self):
      return delivery_orders
     
    def return_single_order_with_id():
      for parcel in delivery_orders:
        if parcel["parcelId"] == parcelId:
          return jsonify({'message':'it is there'}),400
        return jsonify({'message':'parcel does not exist'}),400
      # current_parcel = [parcel for parcel in delivery_orders if parcel["parcelId"] == parcelId]
      # # if not current_parcel:
      # #   return jsonify({'message':'parcel does not exist'}),400
      # # else:
      # return jsonify(current_parcel)

    def delete_order_by_id(self,parcelId):
      remove_parcel = [parcel for parcel in delivery_orders if parcel['parcelId']==parcelId]
      if not remove_parcel:
        return jsonify ({'message':'parcel is not in list'}),400
      else:
        return jsonify ({'message':'parcel order has been deleted'}),400