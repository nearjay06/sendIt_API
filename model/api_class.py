class Orders:
    def __init__(self,parcelId,name,price,time,userId):
       self.parcelId = parcelId
       self.parcel_name = name
       self.parcel_price = price
       self.delivery_time = time
       self.userId = userId


    def make_delivery_order(self):
       service ={
          "parcelId": self.parcelId,
          "parcel_name": self.parcel_name,
          "parcel_price": self.parcel_price,
          "delivery_time":self.delivery_time,
          "userId":self.userId

         }

        
       return service