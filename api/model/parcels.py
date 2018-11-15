delivery_orders =[]

class Orders:
    def __init__(self, **args):
       self.parcelId = args.get('parcelId')
       self.parcel_name = args.get('parcel_name')
       self.parcel_price = args.get('parcel_price')
       self.delivery_time = args.get('delivery_time')
       self.destination = args.get('destination')


    def increment_id(self):
     if len(delivery_orders) == 0:
      ID = len(delivery_orders)+1
     return ID

