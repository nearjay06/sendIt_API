class Orders:
    def __init__(self,parcelId,userId,name,price,time,destination):
       self.parcelId = parcelId
       self.userId = userId
       self.parcel_name = name
       self.parcel_price = price
       self.delivery_time = time
       self.destination = destination
       
    def make_delivery_order(self):
      service ={
          "parcelId": self.parcelId,
          "userId": self.userId,
          "parcel_name": self.parcel_name,
          "parcel_price": self.parcel_price,
          "delivery_time":self.delivery_time,
          "destination" : self.destination
         
        }
      return service

class Users:
    def __init__(self,userId,username,user_email,user_location):
       self.userId = userId
       self.username = username
       self.user_email = user_email
       self.user_location = user_location
       

    def deliver_to_user(self):
       trades = {
          "userId": self.userId,
          "username": self.username,
          "user_email": self.user_email,
          "user_location" : self.user_location
          
         }

       return trades
